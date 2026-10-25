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

def icon(parent,name,cls=''):
 v=widget(parent,W+'IIcon');emit(f'{v}.Icon={q(name)}; {v}.IconSize=ServiceStudio.Plugin.NRWidgets.Enumerations.IconSize.FontSize;')
 if cls:emit(f'{v}.SetStyle({q(lit(cls))});')
 return v
def jsaction(owner,name,script,bindings,after=()):
 a=uid('act');emit(f'var {a}={owner}.CreateScreenAction({q(name)}); foreach(var n in {a}.Nodes.ToList()) n.Delete();')
 st=uid();j=uid();emit(f'var {st}={a}.CreateNode<{N}IStartNode>(); var {j}={a}.CreateNode<{N}IJavaScriptNode>("ScopedBehavior").ConnectedBelow({st}); {j}.JavaScript={q(script)};')
 for n,t,v in bindings:
  p=var(j,n,t,True);emit(f'{j}.SetArgumentValue({p},{q(v)});')
 prev=j
 if after:
  an=uid();emit(f'var {an}={a}.CreateNode<{N}IAssignNode>("RememberLifecycle").ConnectedBelow({j});');prev=an
  for n,v in after:emit(f'{an}.CreateAssignment({q(n)},{q(v)});')
 emit(f'{a}.CreateNode<{N}IEndNode>().ConnectedBelow({prev});');return a

emit('if(eSpace.Name!="WHT_Request") throw new Exception("Guard: WHT_Request required");')
emit('var flow=eSpace.MobileFlows.Single(x=>x.Name=="TestComponent"); var screen=flow.Nodes.OfType<OutSystems.Model.UI.Mobile.IMobileScreen>().Single(x=>x.Name=="WHTDocumentsPrototype");')
names=['PrototypeDocumentHeader','PrototypeYearCard','PrototypeUpload','PrototypeFileRow','PrototypeTracking','PrototypeDialogs']
owners=['header','card','upload','file','tracking','dialogs']
for owner,name in zip(owners,names):emit(f'var {owner}=flow.Nodes.OfType<OutSystems.Model.UI.Mobile.IMobileBlock>().Single(x=>x.Name=={q(name)});')
expectedKeys={'screen':'rgGzB72tVkW2rxXtLW41gw','header':'reDM3Adrdk6sCH6p+vG1xQ','upload':'JeuU9JeskUqqHdYQs81eeQ','card':'Dyhf+wE_w0C5l71RpAqJng','file':'MpmKDYGa6UWfwwrVGb_+1Q','tracking':'jOr5mUsw90eHrkZNMitz2w','dialogs':'1+Dc2V13xESziRlQcjvVyQ'}
for owner,key in expectedKeys.items():emit(f'if({owner}.Key.ToString()!={q(key)}) throw new Exception("Guard: B01 key changed for {owner}");')
emit('var year=eSpace.Structures.Single(x=>x.Name=="PrototypeYear"); if(year.Attributes.Any(x=>x.Name=="IsEditing") || !year.Attributes.Any(x=>x.Name=="C2029")) throw new Exception("Guard: requires unexpanded B01 structure; inspect before retry");')
originalFields={'DocumentType':'Text','Year':'Integer','Status':'Text','Expanded':'Boolean','TrackingExpanded':'Boolean','ShowUpload':'Boolean','ShowFile':'Boolean','ShowCoverage':'Boolean','ShowHistory':'Boolean','FileName':'Text','FileSize':'LongInteger','Notice':'Text','History':'Text','Submitted':'Boolean','ResetVersion':'Integer'}|{f'C{y}':'Boolean' for y in range(2024,2030)}
emit(f'if(year.Attributes.Count()!={len(originalFields)}) throw new Exception("Guard: PrototypeYear B01 schema drift");')
for field,typ in originalFields.items():emit(f'if(!year.Attributes.Any(x=>x.Name=={q(field)} && x.DataType.Equals(eSpace.{typ}Type))) throw new Exception("Guard: PrototypeYear.{field} changed");')
emit('if(card.InputParameters.Count()!=1 || card.InputParameters.First().Name!="State" || !screen.ScreenActions.Any(x=>x.Name=="LoadRepresentative")) throw new Exception("Guard: B01 contract drift");')
emit('var osui=eSpace.References.Named("OutSystemsUI"); var tag=osui.MobileFlows.SelectMany(x=>x.Nodes).OfType<OutSystems.Model.UI.Mobile.IMobileBlockSignature>().Single(x=>x.Name=="Tag");')
# Remove feature instances first, then action/event/parameter contracts. Preserve object keys.
for owner in ['screen']+owners:emit(f'foreach(var w in {owner}.Widgets.ToList()) w.Delete();')
for owner in ['screen']+owners:
 emit(f'{owner}.OnInitialize.Destination=null; {owner}.OnReady.Destination=null; {owner}.OnRender.Destination=null; {owner}.OnDestroy.Destination=null;')
 if owner!='screen':emit(f'{owner}.OnParametersChanged.Destination=null;')
 emit(f'foreach(var a in {owner}.ScreenActions.ToList()) a.Delete(); foreach(var l in {owner}.LocalVariables.ToList()) l.Delete();')
 if owner!='screen':emit(f'foreach(var ev in {owner}.Events.ToList()) ev.Delete(); foreach(var p in {owner}.InputParameters.ToList()) p.Delete();')
fields={'DocumentType':'Text','Year':'Integer','Status':'Text','Expanded':'Boolean','TrackingExpanded':'Boolean','ShowUpload':'Boolean','ShowFile':'Boolean','ShowCoverage':'Boolean','ShowHistory':'Boolean','FileName':'Text','FileSize':'LongInteger','Notice':'Text','History':'Text','Submitted':'Boolean','ResetVersion':'Integer'}
fields.update({f'C{y}':'Boolean' for y in range(2024,2030)})
extra={'IsEditing':'Boolean','ShowResubmit':'Boolean','ShowReview':'Boolean','Reviewer':'Boolean','CompactUpload':'Boolean','ReminderSuspended':'Boolean','Callout':'Text','Event1Title':'Text','Event1Detail':'Text','Event1Date':'Text','Event1Tone':'Text','Event2Title':'Text','Event2Detail':'Text','Event2Date':'Text','Event2Tone':'Text','BackupFileName':'Text','BackupFileSize':'LongInteger','BackupShowFile':'Boolean','BackupShowUpload':'Boolean','BackupShowCoverage':'Boolean'}
extra.update({f'BackupC{y}':'Boolean' for y in range(2024,2030)})
extra['DisplayCoverageYears']='Boolean'
backupFields=['Status','FileName','FileSize','ShowFile','ShowUpload','ShowCoverage','DisplayCoverageYears','ShowHistory','TrackingExpanded','ShowReview','ShowResubmit','CompactUpload','ReminderSuspended','Callout','IsEditing']+[f'Event{i}{f}' for i in [1,2] for f in ['Title','Detail','Date','Tone']]+[f'C{y}' for y in range(2024,2030)]
for field in backupFields:extra['Backup'+field]=(fields|extra)[field]
for n,t in extra.items():emit(f'year.CreateAttribute({q(n)}).DataType=eSpace.{t}Type;')
fields.update(extra)

# Native Upload, local binary only, two reference variants.
var('upload','Content','eSpace.BinaryDataType');var('upload','Name','eSpace.TextType');var('upload','ResetVersion','eSpace.IntegerType',True);var('upload','Compact','eSpace.BooleanType',True)
ue=event('upload','Selected',[('Name','eSpace.TextType'),('Size','eSpace.LongIntegerType')])
ua=action('upload','FileSelected',ev=ue,args={'Name':'Name','Size':'MeasureFile.Size'},measure=True)
reset=action('upload','ResetSelection',[('Name','""'),('Content','NullBinary()')]);emit(f'upload.OnParametersChanged.Destination={reset};')
ub=box('upload','wht-upload');emit(f'{ub}.SetStyle({q(lit("wht-upload ")+" + If(Compact,"+lit("is-compact")+","+lit("")+")")});')
icon(ub,'paperclip','wht-upload-icon')
u=widget(ub,W+'IUpload','BrowseDocument');emit(f'{u}.SetFileName("Name"); {u}.SetFileContent("Content"); {u}.OnChange.Destination={ua}; foreach(var w in {u}.Widgets.ToList()) w.Delete();')
browse=text(u,'Browse');emit(f'{browse}.SetStyleClasses({q(lit("wht-inline"))});')
hint=box(visible(ub,'not Compact'),'wht-upload-hint');text(hint,'Supported: PDF, DOC, DOCX, JPG, JPEG, PNG · maximum 10 MB')

# File row.
var('file','State','year',True);fe=event('file','Command',[('Kind','eSpace.TextType')])
fo=action('file','OpenFile',ev=fe,args={'Kind':'"Open"'});fr=action('file','RemoveFile',ev=fe,args={'Kind':'"Remove"'})
fb=box('file','wht-file');icon(fb,'paperclip');button(fb,'State.FileName',fo,'wht-inline wht-filename',True,True)
edit=visible(fb,'State.ShowCoverage or State.IsEditing');success=box(edit,'wht-file-success');icon(success,'check','text-success');remove=button(success,'×',fr,'btn wht-remove');prop(remove,'aria-label','"Remove " + State.DocumentType + " file for " + IntegerToText(State.Year)')

# Two-event synthetic timeline; new simulated event pushes prior latest into second slot.
var('tracking','State','year',True);te=event('tracking','Toggle',[]);ta=action('tracking','ToggleTracking',ev=te)
tb=box('tracking','wht-tracking');toggle=button(tb,'Tracking Details',ta,'btn wht-disclosure');prop(toggle,'aria-expanded','If(State.TrackingExpanded,"true","false")')
timeline=box(visible(tb,'State.TrackingExpanded'),'wht-timeline')
for i in [1,2]:
 evbox=box(visible(timeline,f'State.Event{i}Title<>""'),'wht-event');emit(f'{evbox}.SetStyle({q(lit("wht-event ")+f" + State.Event{i}Tone")});')
 title=box(evbox,'wht-event-title');expr(title,f'State.Event{i}Title')
 detail=box(evbox,'wht-event-detail');expr(detail,f'State.Event{i}Detail')
 date=box(evbox,'wht-event-date');expr(date,f'State.Event{i}Date')

# Shared mounted native Popup for coverage/reminder/review/unavailability.
for n,t in [('State','year'),('IsOpen','eSpace.BooleanType'),('Kind','eSpace.TextType'),('FocusKey','eSpace.TextType'),('FallbackKey','eSpace.TextType')]:var('dialogs',n,t,True)
var('dialogs','Draft','year');var('dialogs','Reason','eSpace.TextType')
de=event('dialogs','Confirm',[('Value','year'),('Kind','eSpace.TextType'),('Reason','eSpace.TextType')]);dc=event('dialogs','Cancel',[])
di=action('dialogs','InitializeDraft',[('Draft','State'),('Reason','""')]);emit(f'dialogs.OnParametersChanged.Destination={di}; dialogs.OnInitialize.Destination={di};')
da=action('dialogs','ConfirmDialog',ev=de,args={'Value':'Draft','Kind':'Kind','Reason':'Reason'});cancel=action('dialogs','CancelDialog',ev=dc)
dialogHost=box('dialogs','wht-dialog-host');emit(f'{dialogHost}.Name="DialogHost";')
pop=widget(dialogHost,W+'IPopup','PrototypePopup');emit(f'{pop}.SetShowPopup("IsOpen"); {pop}.SetStyle('+q(lit('popup-dialog wht-ui001-popup'))+');')
prop(pop,'aria-label','If(Kind="Coverage","Select coverage years",If(Kind="Reminder","Suspend reminders",If(Kind="Unavailable","Request unavailability review",Kind+" document")))')
heading=box(pop,'wht-dialog-heading');expr(heading,'If(Kind="Coverage","Select coverage years",If(Kind="Reminder","Suspend reminders",If(Kind="Unavailable","Request unavailability review",Kind+" document")))')
expr(pop,'State.DocumentType + " · Document for " + IntegerToText(Draft.Year) + " · Local simulation only"')
choices=visible(pop,'Kind="Coverage" or Kind="Reminder"')
for y in range(2024,2030):
 row=box(choices,'wht-choice');cb=widget(row,W+'ICheckbox',f'Coverage{y}');emit(f'{cb}.SetVariable("Draft.C{y}"); {cb}.SetEnabled('+q(f'Kind <> "Coverage" or State.Year <> {y}')+');')
 lab=widget(row,W+'ILabel');emit(f'{lab}.TargetWidget={cb}; {lab}.Widgets.OfType<{M}ITextWidget>().First().Text="{y}";')
reasonrow=box(visible(pop,'Kind="Reject" or Kind="Unavailable"'),'wht-reason');inp=widget(reasonrow,W+'ITextArea','ReasonInput');emit(f'{inp}.SetVariable("Reason");')
lab=widget(reasonrow,W+'ILabel');emit(f'{lab}.TargetWidget={inp}; {lab}.Widgets.OfType<{M}ITextWidget>().First().Text="Optional reason (synthetic)";')
yearChoices=box(visible(pop,'Kind="Unavailable"'),'wht-target-years');text(yearChoices,'Choose document year: ')
for y in range(2024,2030):
 choose=action('dialogs',f'ChooseYear{y}',[('Draft.Year',str(y))]);yb=button(yearChoices,str(y),choose,'btn wht-preset');prop(yb,'aria-pressed',f'If(Draft.Year={y},"true","false")')
df=box(pop,'wht-dialog-actions');button(df,'Cancel',cancel);button(df,'Confirm',da,'btn btn-primary')
behavior='''var host=document.getElementById($parameters.HostId);if(!host)return;var wasOpen=host.__whtOpen===true;host.__whtOpen=$parameters.Open;
if(!$parameters.Open&&wasOpen){var key=$parameters.FocusKey,fallback=$parameters.FallbackKey;requestAnimationFrame(function(){var target=Array.from(document.querySelectorAll('[data-wht-focus]')).find(x=>x.getAttribute('data-wht-focus')===key&&x.getClientRects().length);if(!target)target=Array.from(document.querySelectorAll('[data-wht-year]')).find(x=>x.getAttribute('data-wht-year')===fallback&&x.getClientRects().length);if(target)target.focus();});}
var el=document.getElementById($parameters.PopupId); if(!el) return;
if(!el.__whtKeys){ el.__whtKeys=function(e){ if(!el.getClientRects().length) return;
if(e.key==='Escape'){e.preventDefault();e.stopPropagation();$actions.CancelDialog();return;}
if(e.key==='Tab'){var items=Array.from(el.querySelectorAll('button,a[href],input,textarea,select,[tabindex]')).filter(x=>!x.disabled&&x.tabIndex>=0&&x.getClientRects().length);if(!items.length)return;var first=items[0],last=items[items.length-1];if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}}
}; el.addEventListener('keydown',el.__whtKeys);}
if($parameters.Open&&!wasOpen){requestAnimationFrame(function(){var first=Array.from(el.querySelectorAll('input,button,textarea,select,[tabindex]')).find(x=>!x.disabled&&x.tabIndex>=0&&x.getClientRects().length);if(first)first.focus();});}
'''
render=jsaction('dialogs','DialogLifecycle',behavior,[('HostId','eSpace.TextType','DialogHost.Id'),('PopupId','eSpace.TextType','PrototypePopup.Id'),('Open','eSpace.BooleanType','IsOpen'),('FocusKey','eSpace.TextType','FocusKey'),('FallbackKey','eSpace.TextType','FallbackKey')]);emit(f'dialogs.OnRender.Destination={render};')

# Header supports tabs and standalone heading, separate reviewer instructions.
for n,t in [('ActiveType','eSpace.TextType'),('Standalone','eSpace.BooleanType'),('Reviewer','eSpace.BooleanType')]:var('header',n,t,True)
he=event('header','Command',[('Kind','eSpace.TextType')]);hb=box('header','wht-header')
tabs=box(visible(hb,'not Standalone'),'wht-tabs');prop(tabs,'aria-label','"Document type"')
for t,label in [('COR','Certificate of Tax Residence (COR)'),('PEL','Permanent Establishment Letter (PEL)')]:
 a=action('header','Select'+t,ev=he,args={'Kind':lit(t)});b=button(tabs,label,a,'btn wht-tab');emit(f'{b}.SetStyle({q(lit("btn wht-tab ")+" + If(ActiveType="+lit(t)+","+lit("is-active")+","+lit("")+")")});');prop(b,'aria-pressed',f'If(ActiveType="{t}","true","false")');prop(b,'data-wht-tab',lit(t))
stand=box(visible(hb,'Standalone'),'wht-standalone');expr(stand,'If(ActiveType="COR","Certificate of Tax Residence (COR)","Permanent Establishment Letter (PEL)")')
submitter=visible(hb,'not Reviewer');spec=action('header','Specimen',ev=he,args={'Kind':'"Specimen"'});button(submitter,'Download specimen',spec,'btn btn-outline')
i1=box(submitter,'wht-instruction');text(i1,'• Please upload the document for the relevant year.')
i2=box(submitter,'wht-instruction');text(i2,'• If you cannot provide the document, ');un=action('header','Unavailable',ev=he,args={'Kind':'"Unavailable"'});ul=button(i2,'request an unavailability review',un,'wht-inline',False,True);prop(ul,'data-wht-focus','"header-"+ActiveType+"-Unavailable"')
reviewer=box(visible(hb,'Reviewer'),'wht-review-intro');text(reviewer,'Please review the documents below and verify that they meet the requirements. ');rem=action('header','SuspendReminder',ev=he,args={'Kind':'"Reminder"'});rl=button(reviewer,'Suspend Reminder',rem,'wht-reminder-link',False,True);prop(rl,'data-wht-focus','"header-"+ActiveType+"-Reminder"')
tabscript='''var root=document.getElementById($parameters.RootId);if(!root||root.__whtTabs)return;root.__whtTabs=true;root.addEventListener('keydown',function(e){var current=e.target.closest('[data-wht-tab]');if(!current)return;var tabs=Array.from(root.querySelectorAll('[data-wht-tab]'));var i=tabs.indexOf(current),next=i;if(e.key==='ArrowRight'||e.key==='ArrowDown')next=(i+1)%tabs.length;else if(e.key==='ArrowLeft'||e.key==='ArrowUp')next=(i+tabs.length-1)%tabs.length;else if(e.key==='Home')next=0;else if(e.key==='End')next=tabs.length-1;else return;e.preventDefault();tabs[next].focus();tabs[next].click();});'''
# Name root so its stable widget id can be passed to the lifecycle action.
emit(f'{hb}.Name="HeaderRoot";');hr=jsaction('header','KeyboardDocumentSelection',tabscript,[('RootId','eSpace.TextType','HeaderRoot.Id')]);emit(f'header.OnRender.Destination={hr};')

# Controlled year component: committed/draft/backup fields live in the screen record.
var('card','State','year',True);var('card','Draft','year');var('card','DialogOpen','eSpace.BooleanType');var('card','DialogKind','eSpace.TextType')
ce=event('card','Changed',[('Value','year')])
def ca(name,changes,params=()):return action('card',name,[('Draft','State')]+changes,params,ce,{'Value':'Draft'})
def newevent(title,detail,tone='"success"'):
 return [(f'Draft.Event2{f}',f'State.Event1{f}') for f in ['Title','Detail','Date','Tone']]+[('Draft.Event1Title',title),('Draft.Event1Detail',detail),('Draft.Event1Date','"24 Oct 2026 · Synthetic user"'),('Draft.Event1Tone',tone),('Draft.ShowHistory','True'),('Draft.TrackingExpanded','True')]
tog=ca('ToggleYear',[('Draft.Expanded','not State.Expanded')]);track=ca('ToggleTracking',[('Draft.TrackingExpanded','not State.TrackingExpanded')])
clear=[('Draft.FileName','""'),('Draft.FileSize','0'),('Draft.ShowFile','False'),('Draft.DisplayCoverageYears','False'),('Draft.ResetVersion','State.ResetVersion+1'),('Draft.Notice','"Draft cleared."')]+[(f'Draft.C{y}',f'State.Year={y}') for y in range(2024,2030)]
cl=ca('ClearAll',clear)
fl=ca('FileCommand',[('Draft.FileName','If(Kind="Remove","",State.FileName)'),('Draft.ShowFile','If(Kind="Remove",False,State.ShowFile)'),('Draft.Notice','If(Kind="Remove","File removed.","Simulated file preview; no document is downloaded.")'),('Draft.ResetVersion','State.ResetVersion+1')],[('Kind','eSpace.TextType')])
valid='Size <= 10485760 and ('+' or '.join(f'If(Length(Name)>={len(ext)},Substr(ToLower(Name),Max(0,Length(Name)-{len(ext)}),{len(ext)})="{ext}",False)' for ext in ['.pdf','.doc','.docx','.jpg','.jpeg','.png'])+')'
sel=ca('AcceptFile',[('Draft.FileName',f'If({valid},Name,State.FileName)'),('Draft.FileSize',f'If({valid},Size,State.FileSize)'),('Draft.ShowFile',f'If({valid},True,State.ShowFile)'),('Draft.Notice',f'If({valid},"File selected locally.","Choose an allowed file up to 10 MB (prototype constraint).")')],[('Name','eSpace.TextType'),('Size','eSpace.LongIntegerType')])
backup=backupFields
begin=ca('BeginResubmit',[(f'Draft.Backup{f}',f'State.{f}') for f in backup]+[('Draft.IsEditing','True'),('Draft.ShowResubmit','False'),('Draft.ShowUpload','True'),('Draft.ShowCoverage','True'),('Draft.Callout','""'),('Draft.Notice','"Choose a replacement file; Cancel restores the previous document."')])
cancelEdit=ca('CancelResubmit',[(f'Draft.{f}',f'State.Backup{f}') for f in backup]+[('Draft.ResetVersion','State.ResetVersion+1'),('Draft.Notice','"Replacement cancelled; previous document restored."')])
coverageText=' + '.join(f'If(State.C{y},"{y} ","")' for y in range(2024,2030))
submitChanges=[('Draft.Submitted','State.FileName<>""'),('Draft.Status','If(State.FileName<>"","Pending Review",State.Status)'),('Draft.ShowUpload','If(State.FileName<>"",False,State.ShowUpload)'),('Draft.ShowCoverage','If(State.FileName<>"",False,State.ShowCoverage)'),('Draft.ShowResubmit','False'),('Draft.IsEditing','If(State.FileName<>"",False,State.IsEditing)'),('Draft.Callout','""'),('Draft.Notice','If(State.FileName<>"","Submitted in this simulation.","Choose a file before submitting.")')]
submitChanges+= [(n,f'If(State.FileName<>"",{v},State.{n.split(".")[1]})') for n,v in newevent('"Document uploaded"','"Synthetic file · covers " + '+coverageText)]
sub=ca('Submit',submitChanges)
resume=ca('ResumeReminder',[('Draft.ReminderSuspended','False'),('Draft.Notice','"Reminders resumed in this simulation."')]+newevent('"Reminder resumed"','"No notification or scheduled job was created."'))
info=ca('ReminderInfo',[('Draft.Notice','"Reminders are suspended for this document year."')])
opens={}
for kind in ['Coverage','Approve','Reject']:
 opens[kind]=action('card','Open'+kind,[('DialogKind',lit(kind)),('DialogOpen','True')])
cd=action('card','CancelDialog',[('DialogOpen','False')])
reviewChanges=[('Draft','State'),('DialogOpen','False'),('Draft.DisplayCoverageYears','If(Kind="Coverage",True,State.DisplayCoverageYears)')]
reviewChanges += [(f'Draft.C{y}',f'If(Kind="Coverage",Value.C{y},State.C{y})') for y in range(2024,2030)]
reviewChanges += [('Draft.Status','If(Kind="Approve",If(State.Status="Not Providable Review","Not Providable","Accepted"),If(Kind="Reject",If(State.Status="Not Providable Review","Pending Upload","Rejected"),State.Status))'),('Draft.ShowReview','If(Kind="Coverage",State.ShowReview,False)'),('Draft.Callout','If(Kind="Coverage",State.Callout,"")'),('Draft.Notice','If(Kind="Coverage","Coverage updated.",Kind+" completed in this simulation.")')]
reviewChanges += [(n,f'If(Kind="Coverage",State.{n.split(".")[1]},{v})') for n,v in newevent('If(Kind="Approve","Unavailability request accepted","Unavailability request rejected")','If(Reason="","Synthetic review decision",Reason)','If(Kind="Approve","success","danger")')]
conf=action('card','ConfirmDialog',reviewChanges,[('Value','year'),('Kind','eSpace.TextType'),('Reason','eSpace.TextType')],ce,{'Value':'Draft'})
root=box('card','wht-year');emit(f'{root}.Name="YearRoot";');head=box(root,'wht-year-heading');b=button(head,'"Document for " + IntegerToText(State.Year)',tog,'btn wht-disclosure',True);prop(b,'aria-expanded','If(State.Expanded,"true","false")');prop(b,'data-wht-year','State.DocumentType+IntegerToText(State.Year)')
marker=box(visible(head,'State.ReminderSuspended'),'wht-reminder-marker');ib=button(marker,'',info,'btn wht-unboxed');icon(ib,'bell-slash-o');prop(ib,'aria-label','"Reminders suspended for " + IntegerToText(State.Year)')
tooltip=box(marker,'wht-tooltip');emit(f'{tooltip}.Name="ReminderTooltip";');text(tooltip,'Reminders are suspended for this document year.');prop(tooltip,'role','"tooltip"');prop(ib,'aria-describedby','ReminderTooltip.Id')
statusStyle='"wht-status " + If(State.Status="Accepted","accepted",If(State.Status="Rejected","rejected",If(State.Status="Not Providable","neutral","pending")))'
taginst=inst(head,'tag',{'Color':'Entities.Color.Neutral8','Size':'Entities.Size.Small','Shape':'Entities.Shape.Rounded','IsLight':'True','ExtendedClass':statusStyle})
emit(f'if(!{taginst}.PlaceholdersContent.Any(x=>x.Placeholder.Name=="Tag")) throw new Exception("Guard: Tag placeholder changed"); var tagContent={taginst}.PlaceholdersContent.Single(x=>x.Placeholder.Name=="Tag");');expr('tagContent','State.Status')
body=visible(root,'State.Expanded');inner=box(body,'wht-year-body')
uploadrow=box(visible(inner,'State.ShowUpload'),'wht-upload-row')
inst(uploadrow,'upload',{'ResetVersion':'State.ResetVersion','Compact':'State.CompactUpload'},[('Selected',sel,{'Name':'Name','Size':'Size'})])
button(visible(uploadrow,'State.ReminderSuspended and State.CompactUpload'),'Resume Reminder',resume,'btn btn-outline')
inst(visible(inner,'State.ShowFile'),'file',{'State':'State'},[('Command',fl,{'Kind':'Kind'})])
reviewrow=box(visible(inner,'State.Callout<>"" or State.ShowResubmit or State.ShowReview'),'wht-review-row')
callout=box(visible(reviewrow,'State.Callout<>""'),'wht-callout');icon(callout,'exclamation-triangle');expr(callout,'State.Callout')
res=visible(reviewrow,'State.ShowResubmit and not State.Reviewer');button(res,'Remove and Resubmit',begin,'btn btn-primary')
review=box(visible(reviewrow,'State.ShowReview'),'wht-review-actions')
for kind in ['Reject','Approve']:
 rb=button(review,kind,opens[kind],'btn wht-reject' if kind=='Reject' else 'btn btn-primary');prop(rb,'data-wht-focus','State.DocumentType+IntegerToText(State.Year)+'+lit(kind))
cov=box(visible(inner,'State.ShowCoverage'),'wht-coverage');text(cov,'Does this document cover multiple years? ');expr(visible(cov,'State.DisplayCoverageYears'),coverageText)
coveragebutton=button(cov,'Select another year',opens['Coverage'],'wht-inline',False,True);prop(coveragebutton,'data-wht-focus','State.DocumentType+IntegerToText(State.Year)+"Coverage"')
footer=box(visible(inner,'State.ShowCoverage'),'wht-actions');button(visible(footer,'not State.IsEditing'),'Clear All',cl);button(visible(footer,'State.IsEditing'),'Cancel',cancelEdit);button(footer,'Submit',sub,'btn btn-primary')
remfooter=box(visible(inner,'State.ReminderSuspended and not State.CompactUpload'),'wht-actions');button(remfooter,'Resume Reminder',resume,'btn btn-outline')
inst(visible(inner,'State.ShowHistory'),'tracking',{'State':'State'},[('Toggle',track,{})])
notice=box(inner,'wht-notice');prop(notice,'aria-live','"polite"');expr(notice,'State.Notice')
inst('card','dialogs',{'State':'State','IsOpen':'DialogOpen','Kind':'DialogKind','FocusKey':'State.DocumentType+IntegerToText(State.Year)+DialogKind','FallbackKey':'State.DocumentType+IntegerToText(State.Year)'},[('Confirm',conf,{'Value':'Value','Kind':'Kind','Reason':'Reason'}),('Cancel',cd,{})])
tooltipjs='''var root=document.getElementById($parameters.RootId);if(!root||root.__whtTooltip)return;root.__whtTooltip=true;root.addEventListener('keydown',function(e){var marker=e.target.closest('.wht-reminder-marker');if(marker&&e.key==='Escape'){marker.setAttribute('data-dismissed','true');e.preventDefault();}});root.addEventListener('focusin',function(e){var marker=e.target.closest('.wht-reminder-marker');if(marker)marker.removeAttribute('data-dismissed');});root.addEventListener('mouseover',function(e){var marker=e.target.closest('.wht-reminder-marker');if(marker&&(!e.relatedTarget||!marker.contains(e.relatedTarget)))marker.removeAttribute('data-dismissed');});'''
trender=jsaction('card','ReminderTooltipLifecycle',tooltipjs,[('RootId','eSpace.TextType','YearRoot.Id')]);emit(f'card.OnRender.Destination={trender};')

# Screen state and all twelve deterministic reference fixtures.
for n,t,default in [('ActiveType','eSpace.TextType','"COR"'),('SelectedPreset','eSpace.TextType','"022146"'),('Standalone','eSpace.BooleanType',None),('Reviewer','eSpace.BooleanType',None),('Feedback','eSpace.TextType',None),('DialogOpen','eSpace.BooleanType',None),('DialogKind','eSpace.TextType',None),('DialogState','year',None)]:var('screen',n,t,default=default)
for t in ['COR','PEL']:
 for y in range(2024,2030):var('screen',f'{t}{y}','year')
presets=['022146','021855','021939','022033','021657','021744','021825','021920','022000','022019','022107','022129']
def baseRows():
 rows={}
 for t in ['COR','PEL']:
  for y in range(2024,2030):
   row={n:('' if typ=='Text' else False if typ=='Boolean' else 0) for n,typ in fields.items()}
   row.update(DocumentType=t,Year=y,Status='Not Providable' if t=='COR' and y==2024 else 'Pending Upload',ShowUpload=(y!=2024 or t=='PEL'),ShowCoverage=(y!=2024 or t=='PEL'))
   row[f'C{y}']=True;rows[f'{t}{y}']=row
 return rows
fixtures={}
for pid in presets:
 rows=baseRows();r=rows['COR2025'];r24=rows['COR2024'];r26=rows['COR2026'];reviewer=pid in ['021939','021657','021744','021920']
 for row in rows.values():row['Reviewer']=reviewer
 if pid in ['022146','021825']:
  r.update(Expanded=True,ShowFile=True,FileName='Synthetic_COR_2025.pdf',FileSize=102400,C2026=True,C2027=True,C2028=True)
 if pid=='022146':r['DisplayCoverageYears']=True
 if pid in ['021855','021939','021920','022107']:
  r.update(Expanded=True,ShowUpload=False,ShowCoverage=False,ShowFile=True,FileName='Synthetic_COR_2025.pdf',FileSize=102400,ShowHistory=True,TrackingExpanded=pid!='022107',Event2Title='Document uploaded',Event2Detail='Synthetic_COR_2025.pdf',Event2Date='20 Oct 2026 · Synthetic submitter',Event2Tone='muted')
 if pid in ['021855','021920','021825']:
  r['Status']='Rejected'
 if pid=='021855':r.update(ShowResubmit=True,Callout='The submitted document was rejected. Please review the details below.')
 if pid in ['021855','021920']:r.update(Event1Title='Document rejected',Event1Detail='Please upload a valid document. Synthetic review reason.',Event1Date='21 Oct 2026 · Synthetic reviewer',Event1Tone='danger')
 if pid=='021939':r.update(Status='Accepted',Event1Title='Document accepted',Event1Detail='Certificate of Residence accepted, covering 2026, 2027, 2028.',Event1Date='21 Oct 2026 · Synthetic reviewer',Event1Tone='success')
 if pid in ['022033','022000','022019']:
  r24.update(Expanded=True,ShowUpload=False,ShowCoverage=False,ShowFile=False,ShowHistory=True,TrackingExpanded=True,Event1Title='Unavailability requested',Event1Detail='Document could not be provided. Synthetic request.',Event1Date='20 Oct 2026 · Synthetic submitter',Event1Tone='muted')
 if pid=='022033':r24.update(Status='Not Providable Review',ShowReview=True,Callout='The submitter cannot provide this document. Please review this request.')
 if pid in ['022000','022019']:
  for f in ['Title','Detail','Date','Tone']:r24['Event2'+f]=r24['Event1'+f]
  r24.update(Status='Pending Upload' if pid=='022000' else 'Not Providable',Event1Title='Unavailability request rejected' if pid=='022000' else 'Unavailability request accepted',Event1Detail='Synthetic review decision',Event1Date='21 Oct 2026 · Synthetic reviewer',Event1Tone='danger' if pid=='022000' else 'success')
 if pid in ['021657','021744']:r['Status']='Accepted';r26['ReminderSuspended']=True
 if pid=='021744':r26.update(Expanded=True,CompactUpload=True,ShowCoverage=False,ShowHistory=True,TrackingExpanded=True,Event1Title='Reminder suspended',Event1Detail='Reminder suspended. Document automatically accepted.',Event1Date='21 Oct 2026 · Synthetic reviewer',Event1Tone='success')
 if pid=='021825':
  r.update(IsEditing=True,BackupFileName='Synthetic_COR_Previous.pdf',BackupFileSize=98304,BackupShowFile=True,BackupShowUpload=False,BackupShowCoverage=False,FileName='Synthetic_COR_Replacement.pdf',C2026=False,C2027=False,C2028=False)
  for y in range(2024,2030):r[f'BackupC{y}']=y==2025
 if pid=='022107':
  for y in [2025,2026,2027]:rows[f'COR{y}']['Status']='Pending Review'
  r.update(Event1Title='Document uploaded',Event1Detail='Synthetic_COR_2025.pdf · covers 2025, 2026, 2027',Event1Date='21 Oct 2026 · Synthetic submitter',Event1Tone='muted',Event2Title='',C2026=True,C2027=True)
 fixtures[pid]=rows
# The preloaded replacement fixture cancels to the exact rejected non-editing fixture.
for field in backupFields:fixtures['021825']['COR2025']['Backup'+field]=fixtures['021855']['COR2025'][field]
def osval(value):
 if isinstance(value,bool):return 'True' if value else 'False'
 if isinstance(value,str):return lit(value)
 return str(value)
def presetExpr(values):
 default=values[presets[0]];result=osval(default)
 for pid in reversed(presets[1:]):
  if values[pid]!=default:result=f'If(Id="{pid}",{osval(values[pid])},{result})'
 return result
init=[('SelectedPreset','Id'),('ActiveType','If(Id="022129","PEL","COR")'),('Standalone','Id="021744" or Id="022129"'),('Reviewer','Id="021939" or Id="021657" or Id="021744" or Id="021920"'),('Feedback','""'),('DialogOpen','False'),('DialogKind','""')]
for key in fixtures[presets[0]]:
 for field in fields:init.append((key+'.'+field,presetExpr({pid:fixtures[pid][key][field] for pid in presets})))
ia=action('screen','LoadPreset',init,[('Id','eSpace.TextType')]);emit(f'screen.OnInitialize.Destination={ia}; screen.OnInitialize.SetArgumentValue({ia}.InputParameters.Named("Id"),'+q(lit('022146'))+');')

# Header dialog targets are explicit and synthetic; user can edit unavailability year.
headerChanges=[('ActiveType','If(Kind="COR" or Kind="PEL",Kind,ActiveType)'),('Feedback','If(Kind="Specimen","Simulated specimen download; no file sent.","")'),('DialogState','If(ActiveType="COR",COR2024,PEL2024)'),('DialogKind','Kind'),('DialogOpen','Kind="Reminder" or Kind="Unavailable"')]
headerChanges += [(f'DialogState.C{y}','False') for y in range(2024,2030)]
hc=action('screen','HeaderCommand',headerChanges,[('Kind','eSpace.TextType')]);globalCancel=action('screen','CancelDialog',[('DialogOpen','False')])
anyChoice=' or '.join(f'Value.C{y}' for y in range(2024,2030))
gc=[('DialogOpen','False'),('Feedback',f'If(Kind="Reminder",If({anyChoice},"Reminder settings updated locally; no notification sent.","No years selected; no changes made."),"Unavailability request recorded locally; no business operation executed.")')]
for t in ['COR','PEL']:
 for y in range(2024,2030):
  key=f'{t}{y}';match=f'Value.DocumentType="{t}" and ((Kind="Reminder" and Value.C{y}) or (Kind="Unavailable" and Value.Year={y}))'
  gc.extend([(key+'.ReminderSuspended',f'If({match} and Kind="Reminder",True,{key}.ReminderSuspended)'),(key+'.Status',f'If({match} and Kind="Unavailable","Not Providable Review",{key}.Status)'),(key+'.ShowReview',f'If({match} and Kind="Unavailable",True,{key}.ShowReview)'),(key+'.ShowUpload',f'If({match} and Kind="Unavailable",False,{key}.ShowUpload)'),(key+'.ShowCoverage',f'If({match} and Kind="Unavailable",False,{key}.ShowCoverage)'),(key+'.ShowHistory',f'If({match},True,{key}.ShowHistory)'),(key+'.Expanded',f'If({match},True,{key}.Expanded)'),(key+'.TrackingExpanded',f'If({match},True,{key}.TrackingExpanded)')])
  for f in ['Title','Detail','Date','Tone']:gc.append((key+'.Event2'+f,f'If({match},{key}.Event1{f},{key}.Event2{f})'))
  for f,v in [('Title','If(Kind="Reminder","Reminder suspended","Unavailability requested")'),('Detail','If(Reason="","Synthetic local action",Reason)'),('Date','"24 Oct 2026 · Synthetic user"'),('Tone','"success"')]:gc.append((key+'.Event1'+f,f'If({match},{v},{key}.Event1{f})'))
globalConfirm=action('screen','ConfirmDialog',gc,[('Value','year'),('Kind','eSpace.TextType'),('Reason','eSpace.TextType')])
rt=box('screen','wht-ui001');tools=box(rt,'wht-tools');text(tools,'Synthetic prototype · no data is saved · select a reference')
for pid in presets:
 pb=button(tools,pid,ia,'btn wht-preset');emit(f'{pb}.OnClick.SetArgumentValue({ia}.InputParameters.Named("Id"),{q(lit(pid))});');prop(pb,'aria-pressed',f'If(SelectedPreset="{pid}","true","false")')
panel=box(rt,'wht-panel');inst(panel,'header',{'ActiveType':'ActiveType','Standalone':'Standalone','Reviewer':'Reviewer'},[('Command',hc,{'Kind':'Kind'})])
for t in ['COR','PEL']:
 panelType=visible(panel,f'ActiveType="{t}"')
 for y in range(2024,2030):
  assigns=[(f'{t}{y}','Value'),(f'{t}{y}.Submitted','False')]
  for z in range(2024,2030):
   if z!=y:assigns.append((f'{t}{z}.Status',f'If(Value.Submitted and Value.C{z},"Pending Review",{t}{z}.Status)'))
  a=action('screen',f'Update{t}{y}',assigns,[('Value','year')]);inst(panelType,'card',{'State':f'{t}{y}'},[('Changed',a,{'Value':'Value'})])
feedback=box(rt,'wht-feedback');prop(feedback,'aria-live','"polite"');expr(feedback,'Feedback')
inst(rt,'dialogs',{'State':'DialogState','IsOpen':'DialogOpen','Kind':'DialogKind','FocusKey':'"header-"+ActiveType+"-"+DialogKind','FallbackKey':'""'},[('Confirm',globalConfirm,{'Value':'Value','Kind':'Kind','Reason':'Reason'}),('Cancel',globalCancel,{})])

css=OUT.joinpath('B01-styles.css').read_text(encoding='utf-8')+'''
.wht-ui001 .wht-tools{justify-content:flex-start;flex-wrap:wrap;gap:6px;font-size:12px}
.wht-ui001 .wht-year{overflow:visible}
.wht-ui001 .wht-tools .wht-preset{font-size:11px;min-height:26px;height:auto;padding:3px 8px}
.wht-ui001 .wht-preset[aria-pressed=true]{border-color:var(--color-primary);color:var(--color-primary)}
.wht-ui001 .wht-upload-icon{font-size:22px;color:var(--color-neutral-7)}
.wht-ui001 .wht-upload.is-compact{min-height:38px;flex-direction:row;justify-content:flex-start;padding:6px 10px}
.wht-ui001 .wht-upload.is-compact .wht-upload-icon{font-size:16px}
.wht-ui001 .wht-upload-row{display:flex;align-items:center;gap:8px}
.wht-ui001 .wht-upload-row>div:first-child{flex:1;min-width:0}
.wht-ui001 .wht-upload-row>.btn{flex-shrink:0}
.wht-ui001 .wht-file-success{display:flex;align-items:center;gap:12px;margin-left:auto}
.wht-ui001 .wht-filename{overflow-wrap:anywhere;min-width:0}
.wht-ui001 .btn.wht-remove{padding:0 5px;min-height:22px;height:auto;background:transparent;border:0;box-shadow:none;font-size:18px}
.wht-ui001 .wht-status.accepted{background:#e5f4e9;color:#28643d}
.wht-ui001 .wht-status.rejected{background:#fce9e9;color:#a43838}
.wht-ui001 .wht-callout{display:flex;gap:8px;background:#fff2f2;border:1px solid #f2cccc;border-radius:4px;padding:8px;margin:10px 0;color:#a43838}
.wht-ui001 .wht-review-actions{display:flex;gap:8px;margin:10px 0}
.wht-ui001 .wht-review-row{display:flex;align-items:center;gap:12px;margin:10px 0;flex-wrap:wrap}
.wht-ui001 .wht-review-row .wht-callout{flex:1;min-width:200px;margin:0}
.wht-ui001 .wht-review-row .wht-review-actions{margin:0}
.wht-ui001 .btn.wht-reject{color:#b33838;border-color:#b33838;background:transparent}
.wht-ui001 .wht-standalone{font-weight:700;font-size:14px;margin:0 0 12px}
.wht-ui001 .wht-review-intro{line-height:1.6;margin:8px 0 12px}
.wht-ui001 .wht-reminder-link{color:var(--color-neutral-8);text-decoration:underline}
.wht-ui001 .wht-reminder-marker{position:relative}
.wht-ui001 .wht-reminder-marker .btn{color:var(--color-neutral-6)}
.wht-ui001 .wht-tooltip{display:none;position:absolute;bottom:100%;right:0;width:220px;background:var(--color-neutral-9);color:var(--color-neutral-0);padding:8px;border-radius:4px;z-index:10;font-size:11px}
.wht-ui001 .wht-reminder-marker:hover .wht-tooltip,.wht-ui001 .wht-reminder-marker:focus-within .wht-tooltip{display:block}
.wht-ui001 .wht-reminder-marker[data-dismissed=true] .wht-tooltip{display:none}
.wht-ui001 .wht-timeline{margin:10px 0 0 8px;border-left:1px dashed var(--color-neutral-5);padding-left:16px}
.wht-ui001 .wht-event{position:relative;padding-bottom:16px;color:var(--color-neutral-6)}
.wht-ui001 .wht-event:before{content:'';position:absolute;left:-21px;top:4px;width:8px;height:8px;border-radius:50%;background:currentColor}
.wht-ui001 .wht-event.success{color:var(--color-primary)}
.wht-ui001 .wht-event.danger{color:#b33838}
.wht-ui001 .wht-event-title{font-weight:600}
.wht-ui001 .wht-event-detail,.wht-ui001 .wht-event-date{font-size:11px;margin-top:3px}
.wht-ui001 .wht-notice{font-size:11px;color:var(--color-neutral-7);margin-top:4px}
.wht-ui001-popup{max-width:520px}
.wht-ui001-popup .wht-dialog-heading{font-weight:700;font-size:18px;margin-bottom:12px}
.wht-ui001-popup .wht-dialog-actions{display:flex;justify-content:flex-end;gap:8px;margin-top:16px}
.wht-ui001-popup .wht-reason{margin-top:12px}
.wht-ui001-popup .wht-target-years{display:flex;gap:6px;flex-wrap:wrap;margin-top:12px}
.wht-ui001-popup .wht-preset[aria-pressed=true]{border-color:var(--color-primary);color:var(--color-primary)}
@media(max-width:600px){.wht-ui001 .wht-upload-row{flex-wrap:wrap}.wht-ui001 .wht-upload-row>div:first-child{flex-basis:100%}.wht-ui001 .wht-year-heading{padding-left:8px}.wht-ui001 .wht-tooltip{right:-100px;width:200px}.wht-ui001-popup{width:calc(100vw - 32px)}.wht-ui001 .wht-tabs{gap:10px}.wht-ui001 .wht-tab{white-space:normal;text-align:left}}
'''
emit('screen.StyleSheet='+q(css)+';')
emit('''foreach(var act in screen.ScreenActions.Concat(header.ScreenActions).Concat(card.ScreenActions).Concat(upload.ScreenActions).Concat(file.ScreenActions).Concat(tracking.ScreenActions).Concat(dialogs.ScreenActions)) {
var start=act.Nodes.OfType<OutSystems.Model.Logic.Nodes.IStartNode>().Single();
var depth=new Dictionary<OutSystems.Model.Logic.Nodes.IActionNode,int>(); var queue=new Queue<OutSystems.Model.Logic.Nodes.IActionNode>(); depth[start]=0;queue.Enqueue(start);
while(queue.Count>0){var current=queue.Dequeue();foreach(var connector in current.Connectors){var next=connector.Target;if(next==null||depth.ContainsKey(next))continue;depth[next]=depth[current]+1;queue.Enqueue(next);}}
if(depth.Count!=act.Nodes.Count())throw new Exception("Unreachable new node: "+act.Name);
foreach(var node in depth.Keys){node.HorizontalPosition=3200;node.VerticalPosition=800+depth[node]*1371;}
}''')
emit('}')
OUT.joinpath('B02-expansion.cs').write_text('\n'.join(lines),encoding='utf-8');OUT.joinpath('B02-styles.css').write_text(css,encoding='utf-8')
OUT.joinpath('B02-fixtures.json').write_text(json.dumps(fixtures,indent=2),encoding='utf-8')
print(f'B02 generated {len(lines)} source entries')

