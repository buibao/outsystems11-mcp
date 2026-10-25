from pathlib import Path
import json
OUT=Path(__file__).parent
lines=['eSpace => {']
def emit(s): lines.append(s)
def q(s): return json.dumps(s,ensure_ascii=False)
def lit(s): return '"'+s.replace('"','""')+'"'
N='OutSystems.Model.Logic.Nodes.'
W='ServiceStudio.Plugin.NRWidgets.'
M='OutSystems.Model.UI.Mobile.Widgets.'
counter=0
def uid(p='v'):
 global counter
 counter+=1
 return p+str(counter)
def var(owner,name,typ,inp=False,default=None):
 v=uid(); emit(f'var {v} = {owner}.Create'+('InputParameter' if inp else 'LocalVariable')+f'({q(name)}); {v}.DataType = {typ};')
 if inp: emit(f'{v}.IsMandatory = true;')
 if default is not None: emit(f'{v}.SetDefaultValue({q(default)});')
 return v
def widget(parent,typ,name=None):
 v=uid();emit(f'var {v} = {parent}.CreateWidget<{typ}>({q(name or v)});');return v
def box(parent,cls):
 v=widget(parent,W+'IContainer');emit(f'{v}.SetStyle({q(lit(cls))});');return v
def text(parent,s):
 v=widget(parent,M+'ITextWidget');emit(f'{v}.Text = {q(s)};');return v
def expr(parent,s):
 v=widget(parent,W+'IExpression');emit(f'{v}.SetValue({q(s)});');return v
def prop(v,k,val):
 p=uid();emit(f'var {p}={v}.CreateExtendedProperty(); {p}.Property={q(k)}; {p}.SetValue({q(val)});')
def event(owner,name,params):
 v=uid('ev');emit(f'var {v}={owner}.CreateEvent({q(name)});')
 for n,t in params: var(v,n,t,True)
 return v
def action(owner,name,assigns=(),params=(),ev=None,args=None,measure=False):
 v=uid('act');emit(f'var {v}={owner}.CreateScreenAction({q(name)});')
 for n,t in params: var(v,n,t,True)
 emit(f'foreach(var n in {v}.Nodes.ToList()) n.Delete();')
 start=uid();emit(f'var {start}={v}.CreateNode<{N}IStartNode>(); {start}.HorizontalPosition=0; {start}.VerticalPosition=0;')
 prev=start
 if measure:
  j=uid();emit(f'var {j}={v}.CreateNode<{N}IJavaScriptNode>("MeasureFile").ConnectedBelow({prev});');prev=j
  emit(f'{j}.JavaScript='+q('var b=$parameters.Content; $parameters.Size=b && typeof b.byteLength === "number" ? b.byteLength : b && typeof b.size === "number" ? b.size : typeof b === "string" ? Math.max(0,Math.floor(b.length*3/4)-(b.endsWith("==")?2:b.endsWith("=")?1:0)) : 10485761;')+';')
  p=var(j,'Content','eSpace.BinaryDataType',True);emit(f'{j}.SetArgumentValue({p},"Content"); var measured={j}.CreateOutputParameter("Size"); measured.DataType=eSpace.LongIntegerType;')
 if assigns:
  a=uid();emit(f'var {a}={v}.CreateNode<{N}IAssignNode>("UpdateState").ConnectedBelow({prev});');prev=a
  for name,value in assigns: emit(f'{a}.CreateAssignment({q(name)},{q(value)});')
 if ev:
  t=uid();emit(f'var {t}={v}.CreateNode<{N}ITriggerNode>("NotifyOwner").ConnectedBelow({prev}); {t}.Event={ev};');prev=t
  for name,value in (args or {}).items(): emit(f'{t}.SetArgumentValue({ev}.InputParameters.Named({q(name)}),{q(value)});')
 if measure:
  clear=uid();emit(f'var {clear}={v}.CreateNode<{N}IAssignNode>("ReleaseBinary").ConnectedBelow({prev}); {clear}.CreateAssignment("Content","NullBinary()");');prev=clear
 emit(f'{v}.CreateNode<{N}IEndNode>().ConnectedBelow({prev});')
 return v
def button(parent,label,act,cls='btn',expression=False,link=False):
 v=widget(parent,W+('ILink' if link else 'IButton'))
 emit(f'foreach(var child in {v}.Widgets.ToList()) child.Delete();')
 if expression: expr(v,label)
 else:text(v,label)
 emit(f'{v}.SetStyle({q(lit(cls))}); {v}.OnClick.Destination={act};')
 return v
def inst(parent,block,args,handlers=()):
 v=widget(parent,M+'IMobileBlockInstanceWidget');emit(f'{v}.SourceBlock={block};')
 for name,value in args.items():emit(f'{v}.SetArgumentValue({block}.InputParameters.Named({q(name)}),{q(value)});')
 for ename,act,arguments in handlers:
  h=uid();emit(f'var {h}={v}.EventHandlers.Single(x=>x.Event.Name=={q(ename)}); {h}.Handler={act};')
  for n,value in arguments.items():emit(f'{h}.SetArgumentValue({act}.InputParameters.Named({q(n)}),{q(value)});')
 return v
def visible(parent,condition):
 v=widget(parent,M+'IIfWidget');emit(f'{v}.SetCondition({q(condition)});');return v+'.TrueBranch'

emit('if(eSpace.Name != "WHT_Request") throw new Exception("Guard: WHT_Request required");')
emit('var flow=eSpace.MobileFlows.Single(x=>x.Name=="TestComponent");')
emit('var baseY=flow.Nodes.Any()?flow.Nodes.Max(x=>x.VerticalPosition)+1500:700;')
names=['WHTDocumentsPrototype','PrototypeDocumentHeader','PrototypeYearCard','PrototypeUpload','PrototypeFileRow','PrototypeTracking','PrototypeDialogs']
emit('var names=new[]{'+','.join(q(n) for n in names)+'};')
emit('if(eSpace.MobileFlows.SelectMany(x=>x.Nodes).OfType<OutSystems.Model.UI.Mobile.IMobileScreen>().Any(x=>names.Contains(x.Name)) || eSpace.MobileFlows.SelectMany(x=>x.Nodes).OfType<OutSystems.Model.UI.Mobile.IMobileBlock>().Any(x=>names.Contains(x.Name)) || eSpace.Structures.Any(x=>x.Name=="PrototypeYear")) throw new Exception("Guard: prototype name collision; inspect state, do not replay");')
emit('var osui=eSpace.References.Named("OutSystemsUI"); var tag=osui.MobileFlows.SelectMany(x=>x.Nodes).OfType<OutSystems.Model.UI.Mobile.IMobileBlockSignature>().Single(x=>x.Name=="Tag");')
emit('var year=eSpace.CreateStructure("PrototypeYear");')
fields={'DocumentType':'Text','Year':'Integer','Status':'Text','Expanded':'Boolean','TrackingExpanded':'Boolean','ShowUpload':'Boolean','ShowFile':'Boolean','ShowCoverage':'Boolean','ShowHistory':'Boolean','FileName':'Text','FileSize':'LongInteger','Notice':'Text','History':'Text','Submitted':'Boolean','ResetVersion':'Integer'}
fields.update({f'C{y}':'Boolean' for y in range(2024,2030)})
for n,t in fields.items():emit(f'year.CreateAttribute({q(n)}).DataType=eSpace.{t}Type;')
for i,n in enumerate(names):
 v='screen' if i==0 else ['header','card','upload','file','tracking','dialogs'][i-1]
 emit(f'var {v}=flow.Create'+('Screen' if i==0 else 'Block')+f'({q(n)}); {v}.HorizontalPosition={800+(i%3)*2600}; {v}.VerticalPosition=baseY+{(i//3)*1500}; foreach(var w in {v}.Widgets.ToList()) w.Delete();')
emit('screen.Roles.Add(eSpace.RegisteredRole); screen.SetTitle('+q(lit('WHT Documents — Prototype'))+');')

# Upload sends only filename/size; binary never leaves this component.
var('upload','Content','eSpace.BinaryDataType');var('upload','Name','eSpace.TextType');var('upload','ResetVersion','eSpace.IntegerType',True)
ue=event('upload','Selected',[('Name','eSpace.TextType'),('Size','eSpace.LongIntegerType')])
ua=action('upload','FileSelected',ev=ue,args={'Name':'Name','Size':'MeasureFile.Size'},measure=True)
reset=action('upload','ResetSelection',[('Name','""'),('Content','NullBinary()')]);emit(f'upload.OnParametersChanged.Destination={reset};')
ub=box('upload','wht-upload');text(ub,'Attach a document')
u=widget(ub,W+'IUpload','BrowseDocument');emit(f'{u}.SetFileName("Name"); {u}.SetFileContent("Content"); {u}.OnChange.Destination={ua};')
emit(f'foreach(var w in {u}.Widgets.ToList()) w.Delete();');text(u,'Browse')
text(ub,'PDF, DOC, DOCX, JPG, JPEG, PNG · maximum 10 MB · local simulation')

# File row owns no data and emits intent.
var('file','State','year',True);fe=event('file','Command',[('Kind','eSpace.TextType')])
fo=action('file','OpenFile',ev=fe,args={'Kind':'"Open"'});fr=action('file','RemoveFile',ev=fe,args={'Kind':'"Remove"'})
fb=box('file','wht-file');text(fb,'📎  ');button(fb,'State.FileName',fo,'wht-inline',True,True);check=text(fb,'✓');emit(f'{check}.SetStyleClasses({q(lit("text-success"))});');button(fb,'Remove',fr,'btn wht-unboxed')

# Tracking disclosure forwards intent; title/history stay typed input data.
var('tracking','State','year',True);te=event('tracking','Toggle',[])
ta=action('tracking','ToggleTracking',ev=te)
tb=box('tracking','wht-tracking');toggle=button(tb,'Tracking Details',ta,'btn wht-disclosure');prop(toggle,'aria-expanded','If(State.TrackingExpanded,"true","false")')
expr(visible(tb,'State.TrackingExpanded'),'State.History')

# Native always-mounted coverage dialog. Draft initialized only when input changes.
var('dialogs','State','year',True);var('dialogs','IsOpen','eSpace.BooleanType',True);var('dialogs','Draft','year')
de=event('dialogs','Confirm',[('Value','year')]);dc=event('dialogs','Cancel',[])
di=action('dialogs','InitializeDraft',[('Draft','State')]);emit(f'dialogs.OnParametersChanged.Destination={di}; dialogs.OnInitialize.Destination={di};')
da=action('dialogs','ConfirmChoices',ev=de,args={'Value':'Draft'});cancel=action('dialogs','CancelChoices',ev=dc)
pop=widget('dialogs',W+'IPopup','CoveragePopup');emit(f'{pop}.SetShowPopup("IsOpen"); {pop}.SetStyle('+q(lit('popup-dialog wht-ui001-popup'))+');')
prop(pop,'aria-label','"Select coverage years"');text(pop,'Select coverage years')
for y in range(2024,2030):
 row=box(pop,'wht-choice');cb=widget(row,W+'ICheckbox',f'Coverage{y}');emit(f'{cb}.SetVariable("Draft.C{y}"); {cb}.SetEnabled("State.Year <> {y}");')
 lab=widget(row,W+'ILabel');emit(f'{lab}.TargetWidget={cb}; {lab}.Widgets.OfType<{M}ITextWidget>().First().Text="{y}";')
button(pop,'Cancel',cancel);button(pop,'Confirm',da,'btn btn-primary')

# Header has semantic links and separate unboxed tab buttons.
var('header','ActiveType','eSpace.TextType',True);he=event('header','Command',[('Kind','eSpace.TextType')])
hb=box('header','wht-header');tabs=box(hb,'wht-tabs')
for t,label in [('COR','Certificate of Residence (COR)'),('PEL','Permanent Establishment Letter (PEL)')]:
 a=action('header','Select'+t,ev=he,args={'Kind':lit(t)});b=button(tabs,label,a,'btn wht-tab');emit(f'{b}.SetStyle({q(lit("btn wht-tab ")+" + If(ActiveType="+lit(t)+","+lit("is-active")+","+lit("")+")")});');prop(b,'aria-pressed',f'If(ActiveType="{t}","true","false")')
spec=action('header','Specimen',ev=he,args={'Kind':'"Specimen"'});button(hb,'Download specimen',spec,'btn btn-outline')
instruction1=box(hb,'wht-instruction');text(instruction1,'• Upload the document for the relevant year.')
instruction2=box(hb,'wht-instruction');text(instruction2,'• If a document cannot be provided, ')
un=action('header','Unavailable',ev=he,args={'Kind':'"Unavailable"'});button(instruction2,'request unavailability review',un,'wht-inline',False,True)

# Year card is a controlled component. Every state change returns a full typed record.
var('card','State','year',True);var('card','Draft','year');var('card','DialogOpen','eSpace.BooleanType')
ce=event('card','Changed',[('Value','year')])
def ca(name,changes,params=()):return action('card',name,[('Draft','State')]+changes,params,ce,{'Value':'Draft'})
tog=ca('ToggleYear',[('Draft.Expanded','not State.Expanded')]);track=ca('ToggleTracking',[('Draft.TrackingExpanded','not State.TrackingExpanded')])
clear=[('Draft.FileName','""'),('Draft.FileSize','0'),('Draft.ShowFile','False'),('Draft.ResetVersion','State.ResetVersion+1'),('Draft.Notice','"Draft cleared."')]+[(f'Draft.C{y}',f'State.Year={y}') for y in range(2024,2030)]
cl=ca('ClearAll',clear)
fl=ca('FileCommand',[('Draft.FileName','If(Kind="Remove","",State.FileName)'),('Draft.ShowFile','If(Kind="Remove",False,State.ShowFile)'),('Draft.Notice','If(Kind="Remove","File removed.","Simulated file preview; no document is downloaded.")'),('Draft.ResetVersion','State.ResetVersion+1')],[('Kind','eSpace.TextType')])
valid='Size <= 10485760 and ('+' or '.join(f'If(Length(Name)>={len(ext)},Substr(ToLower(Name),Max(0,Length(Name)-{len(ext)}),{len(ext)})="{ext}",False)' for ext in ['.pdf','.doc','.docx','.jpg','.jpeg','.png'])+')'
sel=ca('AcceptFile',[('Draft.FileName',f'If({valid},Name,State.FileName)'),('Draft.FileSize',f'If({valid},Size,State.FileSize)'),('Draft.ShowFile',f'If({valid},True,State.ShowFile)'),('Draft.Notice',f'If({valid},"File selected locally.","Choose an allowed file up to 10 MB.")')],[('Name','eSpace.TextType'),('Size','eSpace.LongIntegerType')])
sub=ca('Submit',[('Draft.Submitted','State.FileName <> ""'),('Draft.Status','If(State.FileName <> "","Pending Review",State.Status)'),('Draft.ShowUpload','State.FileName = ""'),('Draft.ShowCoverage','State.FileName = ""'),('Draft.ShowHistory','State.FileName <> ""'),('Draft.History','"Document submitted — synthetic event; no backend transaction."'),('Draft.Notice','If(State.FileName <> "","Submitted in this simulation.","Choose a file before submitting.")')])
od=action('card','OpenCoverage',[('DialogOpen','True')]);cd=action('card','CancelCoverage',[('DialogOpen','False')])
conf=action('card','ConfirmCoverage',[('Draft','Value'),('DialogOpen','False')],[('Value','year')],ce,{'Value':'Draft'})
root=box('card','wht-year');head=box(root,'wht-year-heading');b=button(head,'"Document for " + IntegerToText(State.Year)',tog,'btn wht-disclosure',True);prop(b,'aria-expanded','If(State.Expanded,"true","false")')
taginst=inst(head,'tag',{'Color':'Entities.Color.Neutral8','Size':'Entities.Size.Small','Shape':'Entities.Shape.Rounded','IsLight':'True','ExtendedClass':'If(State.Status="Not Providable","wht-status neutral","wht-status pending")'})
emit(f'if(!{taginst}.PlaceholdersContent.Any(x=>x.Placeholder.Name=="Tag")) throw new Exception("Guard: native Tag placeholder changed"); var tagContent={taginst}.PlaceholdersContent.Single(x=>x.Placeholder.Name=="Tag");');expr('tagContent','State.Status')
body=visible(root,'State.Expanded');inner=box(body,'wht-year-body')
inst(visible(inner,'State.ShowUpload'),'upload',{'ResetVersion':'State.ResetVersion'},[('Selected',sel,{'Name':'Name','Size':'Size'})])
inst(visible(inner,'State.ShowFile'),'file',{'State':'State'},[('Command',fl,{'Kind':'Kind'})])
cov=box(visible(inner,'State.ShowCoverage'),'wht-coverage');text(cov,'Does this document cover multiple years? ')
expr(cov,' + '.join(f'If(State.C{y},"{y} ","")' for y in range(2024,2030)));button(cov,'Select another year',od,'wht-inline',False,True)
footer=box(visible(inner,'State.ShowCoverage'),'wht-actions');button(footer,'Clear All',cl);button(footer,'Submit',sub,'btn btn-primary')
inst(visible(inner,'State.ShowHistory'),'tracking',{'State':'State'},[('Toggle',track,{})])
notice=box(inner,'wht-notice');prop(notice,'aria-live','"polite"');expr(notice,'State.Notice')
inst('card','dialogs',{'State':'State','IsOpen':'DialogOpen'},[('Confirm',conf,{'Value':'Value'}),('Cancel',cd,{})])

# Screen owns twelve records; event handlers close over an explicit identity.
var('screen','ActiveType','eSpace.TextType',default='"COR"');var('screen','Feedback','eSpace.TextType')
for t in ['COR','PEL']:
 for y in range(2024,2030):var('screen',f'{t}{y}','year')
init=[('ActiveType','"COR"'),('Feedback','""')]
for t in ['COR','PEL']:
 for y in range(2024,2030):
  prefix=f'{t}{y}.'
  vals={n:('""' if typ=='Text' else 'False' if typ=='Boolean' else '0') for n,typ in fields.items()}
  vals.update(DocumentType=lit(t),Year=str(y),Status=lit('Not Providable' if t=='COR' and y==2024 else 'Pending Upload'),Expanded=str(t=='COR' and y==2025),ShowUpload=str(y!=2024 or t=='PEL'),ShowCoverage=str(y!=2024 or t=='PEL'))
  vals.update({f'C{z}':str(z==y or (t=='COR' and y==2025 and z in [2026,2027,2028])) for z in range(2024,2030)})
  if t=='COR' and y==2025: vals.update(FileName=lit('Synthetic_COR_2025.pdf'),ShowFile='True',FileSize='102400')
  init.extend((prefix+n,v) for n,v in vals.items())
ia=action('screen','LoadRepresentative',init);emit(f'screen.OnInitialize.Destination={ia};')
hc=action('screen','HeaderCommand',[('ActiveType','If(Kind="COR" or Kind="PEL",Kind,ActiveType)'),('Feedback','If(Kind="Specimen","Simulated specimen download; no file sent.",If(Kind="Unavailable","Unavailability request is a local simulation. Review preset controls are added in the next fixture slice.",""))')],[('Kind','eSpace.TextType')])
rt=box('screen','wht-ui001');tools=box(rt,'wht-tools');text(tools,'Synthetic prototype · 022146 · no data is saved');button(tools,'Reset reference',ia)
panel=box(rt,'wht-panel');inst(panel,'header',{'ActiveType':'ActiveType'},[('Command',hc,{'Kind':'Kind'})])
for t in ['COR','PEL']:
 panelType=visible(panel,f'ActiveType="{t}"')
 for y in range(2024,2030):
  assigns=[(f'{t}{y}','Value'),(f'{t}{y}.Submitted','False')]
  for z in range(2024,2030):
   if z!=y:assigns.append((f'{t}{z}.Status',f'If(Value.Submitted and Value.C{z},"Pending Review",{t}{z}.Status)'))
  a=action('screen',f'Update{t}{y}',assigns,[('Value','year')]);inst(panelType,'card',{'State':f'{t}{y}'},[('Changed',a,{'Value':'Value'})])
feedback=box(rt,'wht-feedback');prop(feedback,'aria-live','"polite"');expr(feedback,'Feedback')
css='''
.wht-ui001 {background:var(--color-neutral-2);padding:var(--space-base);font-size:12px;min-height:100vh;}
.wht-ui001 .wht-panel {max-width:892px;margin:auto;background:var(--color-neutral-0);border-radius:var(--border-radius-soft);padding:12px;}
.wht-ui001 .wht-tools {max-width:892px;margin:0 auto 12px;display:flex;justify-content:space-between;align-items:center;gap:8px;}
.wht-ui001 .wht-header {margin-bottom:12px;line-height:1.6;}
.wht-ui001 .wht-tabs {display:flex;border-bottom:1px solid var(--color-neutral-4);margin-bottom:10px;gap:24px;}
.wht-ui001 .btn.wht-tab {background:transparent;border:0;border-radius:0;box-shadow:none;color:var(--color-neutral-7);padding:6px 0;min-height:32px;height:auto;font-size:12px;}
.wht-ui001 .btn.wht-tab.is-active {color:var(--color-primary);border-bottom:2px solid var(--color-primary);}
.wht-ui001 .wht-year {border:1px solid var(--color-neutral-4);border-radius:8px;margin-bottom:6px;overflow:hidden;}
.wht-ui001 .wht-year-heading {position:relative;display:flex;align-items:center;padding:0 30px 0 10px;gap:8px;min-height:34px;}
.wht-ui001 .btn.wht-disclosure {background:transparent;border:0;box-shadow:none;color:var(--color-neutral-9);font-weight:700;padding:4px 0;min-height:32px;height:auto;text-align:left;flex:1;}
.wht-ui001 .wht-year-heading .wht-disclosure:after {content:'⌄';color:var(--color-primary);position:absolute;right:10px;top:8px;}
.wht-ui001 .wht-year-heading .wht-disclosure[aria-expanded=true]:after {content:'⌃';}
.wht-ui001 .wht-status {font-size:10px;padding:2px 8px;min-height:20px;}
.wht-ui001 .wht-status.pending {background:#fff4d6;color:#66552b;}
.wht-ui001 .wht-status.neutral {background:var(--color-neutral-3);color:var(--color-neutral-7);}
.wht-ui001 .wht-year-body {padding:4px 10px 10px;}
.wht-ui001 .wht-upload {background:var(--color-neutral-1);border:1px solid var(--color-neutral-4);border-radius:4px;min-height:98px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:var(--color-neutral-7);}
.wht-ui001 .wht-file {margin-top:10px;padding:4px 8px;background:var(--color-neutral-2);display:flex;align-items:center;gap:8px;overflow-wrap:anywhere;}
.wht-ui001 .wht-file .wht-unboxed {margin-left:auto;}
.wht-ui001 .btn.wht-unboxed {background:transparent;border:0;box-shadow:none;padding:0 4px;min-height:24px;height:auto;font-size:12px;}
.wht-ui001 .wht-inline {color:var(--color-primary);text-decoration:underline;cursor:pointer;}
.wht-ui001 .wht-coverage {padding:10px 0;line-height:1.6;}
.wht-ui001 .wht-actions {border-top:1px solid var(--color-neutral-4);padding-top:10px;display:flex;justify-content:flex-end;gap:8px;}
.wht-ui001 .wht-actions .btn,.wht-ui001 .wht-header>.btn {font-size:12px;min-height:28px;height:auto;padding:4px 12px;}
.wht-ui001 .wht-tracking {border:1px solid var(--color-neutral-4);margin-top:10px;padding:8px;}
.wht-ui001 .wht-notice:empty {display:none;}
.wht-ui001-popup .wht-choice {display:flex;align-items:center;gap:12px;margin:8px 0;}
.wht-ui001 :focus-visible,.wht-ui001-popup :focus-visible {outline:2px solid var(--color-primary);outline-offset:3px;}
@media(max-width:600px){.wht-ui001{padding:8px}.wht-ui001 .wht-tabs{gap:12px}.wht-ui001 .wht-tools{flex-wrap:wrap}.wht-ui001 .wht-file{flex-wrap:wrap}.wht-ui001 .wht-actions{flex-wrap:wrap}.wht-ui001 .wht-status{white-space:nowrap}}
'''
emit('screen.StyleSheet='+q(css)+';')
emit('''
// Full typed BFS layout pass, adapted from the installed LayoutActionFlow example.
foreach(var act in screen.ScreenActions.Concat(header.ScreenActions).Concat(card.ScreenActions).Concat(upload.ScreenActions).Concat(file.ScreenActions).Concat(tracking.ScreenActions).Concat(dialogs.ScreenActions)) {
    var start=act.Nodes.OfType<OutSystems.Model.Logic.Nodes.IStartNode>().Single();
    var depth=new Dictionary<OutSystems.Model.Logic.Nodes.IActionNode,int>();
    var queue=new Queue<OutSystems.Model.Logic.Nodes.IActionNode>();
    depth[start]=0; queue.Enqueue(start);
    while(queue.Count>0) {
        var current=queue.Dequeue();
        foreach(var connector in current.Connectors) {
            var next=connector.Target;
            if(next==null || depth.ContainsKey(next)) continue;
            depth[next]=depth[current]+1; queue.Enqueue(next);
        }
    }
    if(depth.Count!=act.Nodes.Count()) throw new Exception("Guard: unreachable node in new action "+act.Name);
    foreach(var node in depth.Keys) { node.HorizontalPosition=3200; node.VerticalPosition=800+depth[node]*1371; }
}
''')
emit('}')
OUT.joinpath('B01-representative.cs').write_text('\n'.join(lines),encoding='utf-8')
OUT.joinpath('B01-styles.css').write_text(css,encoding='utf-8')
print(f'Generated {len(lines)} lines; {counter} model declarations')
