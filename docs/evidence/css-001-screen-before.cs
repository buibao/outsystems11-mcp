```csharp
(OutSystems.Model.UI.Mobile.IMobileFlow mainFlow) => {
    
    /*** creating IMobileScreen 'TaxDocumentsPreview' ***/
    var taxDocumentsPreview = mainFlow.CreateScreen("TaxDocumentsPreview");
    /*** Deleting Widgets that are created by default when instantiating an IMobileScreen ***/
    taxDocumentsPreview.Widgets.ToList().ForEach(x => x.Delete());
    taxDocumentsPreview.GetESpace().Roles.ToList().ForEach(x => x.Delete());
    var eSpace = mainFlow.GetESpace();
    var anonymous = eSpace.SystemRoles.OfType<OutSystems.Model.Logic.ISystemRole>().Named("Anonymous");
    taxDocumentsPreview.Roles.Add(anonymous);
    var registered = eSpace.SystemRoles.OfType<OutSystems.Model.Logic.ISystemRole>().Named("Registered");
    taxDocumentsPreview.Roles.Add(registered);
    taxDocumentsPreview.AnonymousAccess = false; // default value
    taxDocumentsPreview.CustomURL = false; // default value
    taxDocumentsPreview.Description = "Interactive frontend prototype with synthetic fixtures; no requests are sent or persisted.";
    taxDocumentsPreview.HorizontalPosition = 800;
    taxDocumentsPreview.Icon = null; // default value
    taxDocumentsPreview.IsDisabled = false; // default value
    taxDocumentsPreview.PageName = null; // default value
    taxDocumentsPreview.Public = false; // default value
    taxDocumentsPreview.Shareable = false; // default value
    taxDocumentsPreview.StyleSheet = ".tax-documents-preview{--td-blue:#0667f9;--td-border:#e4e7eb;color:#272b30;font:13px/1.5 Arial,sans-serif;background:#f5f7f9;min-height:100vh;padding:20px;box-sizing:border-box}\n.tax-documents-preview *{box-sizing:border-box}.tax-documents-preview .td-shell{max-width:1100px;margin:0 auto}.tax-documents-preview .td-panel{background:#fff;border:1px solid var(--td-border);border-radius:12px;padding:20px}\n.tax-documents-preview .td-preview-controls{background:#fff;border:1px dashed #b9c4d2;border-radius:8px;padding:12px 16px;margin-bottom:14px}.tax-documents-preview .td-preview-tools{display:flex;align-items:center;flex-wrap:wrap;gap:10px;margin-top:8px}.tax-documents-preview .td-preview-tools select{max-width:100%;min-width:240px;font-size:12px}\n.tax-documents-preview .td-tabs{display:flex;gap:8px;border-bottom:1px solid #cbd5e1;margin-bottom:18px;overflow:auto}.tax-documents-preview .td-tab{border:0;border-bottom:2px solid transparent;background:transparent;border-radius:0;padding:12px 10px;color:#747b85;font-weight:400;font-size:12px;white-space:normal;height:auto}.tax-documents-preview .td-tab-active{color:#252b32;border-bottom-color:var(--td-blue);font-weight:600}\n.tax-documents-preview .td-heading{font-size:18px;font-weight:600;margin:0 0 14px}.tax-documents-preview .td-intro{font-size:12px;margin:15px 0 20px}.tax-documents-preview .td-list{padding:0;margin:0;list-style:none;width:100%}.tax-documents-preview .td-card{background:#fff;border:1px solid var(--td-border);border-radius:12px;margin-top:10px;overflow:hidden}.tax-documents-preview .td-card-header{display:flex;align-items:center;gap:10px;min-height:58px;padding:0 16px}.tax-documents-preview .td-card-toggle{border:0;background:transparent;color:#252b32;flex:1;text-align:left;font-weight:600;padding:18px 0;height:auto;font-size:13px}.tax-documents-preview .td-card-body{padding:0 16px 16px}.tax-documents-preview .td-chevron{color:var(--td-blue);font-size:20px;margin-left:6px}.tax-documents-preview .td-badge{font-size:11px;line-height:1.3;display:inline-flex;width:auto!important;padding:4px 10px;border-radius:16px;border:1px solid transparent;white-space:nowrap}.tax-documents-preview .td-amber{background:#fff6e6;color:#ae7200;border-color:#ffdaa0}.tax-documents-preview .td-success{background:#edf8ee;color:#258b36;border-color:#b8e5c2}.tax-documents-preview .td-danger{background:#ffeded;color:#d52c36;border-color:#ffb7bf}.tax-documents-preview .td-neutral{background:#e9edf1;color:#444b55;border-color:#dfe4ea}\n.tax-documents-preview .td-button{height:auto;min-height:32px;border:1px solid #ccd3dd;border-radius:3px;padding:7px 15px;background:#fff;color:#5f6772;font-size:12px;font-weight:400;line-height:1.4;cursor:pointer;white-space:normal}.tax-documents-preview .td-primary{background:var(--td-blue);border-color:var(--td-blue);color:white}.tax-documents-preview .td-outline{border-color:#6c9dff;color:var(--td-blue)}.tax-documents-preview .td-reject{border-color:#ff6674;color:#d52c36}.tax-documents-preview .td-link{border:0;background:transparent;padding:0;color:var(--td-blue);text-decoration:underline;font-size:inherit;height:auto;min-height:24px;text-align:left;cursor:pointer}.tax-documents-preview .td-icon-button{background:transparent;border:0;color:#97a3b3;padding:4px 7px;height:auto;font-size:20px;cursor:pointer}.tax-documents-preview .td-actions{display:flex;justify-content:flex-end;flex-wrap:wrap;gap:10px;border-top:1px solid var(--td-border);padding-top:14px;margin-top:14px}.tax-documents-preview .td-action-bar{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-top:14px}.tax-documents-preview .td-notice{border:1px solid #ffb6c0;background:#fff0f1;border-radius:5px;padding:8px 12px;font-size:12px;flex:1;min-width:200px;color:#675b60}.tax-documents-preview .td-muted{color:#98a4b2;font-size:11px}.tax-documents-preview .td-feedback{font-size:12px;color:#315c8d;margin:10px 0;white-space:pre-line}.tax-documents-preview .td-feedback:empty{display:none}\n.tax-documents-preview .td-upload-area{border:1px solid var(--td-border);border-radius:8px;background:#f7f8fa;min-height:148px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#77818c;padding:18px;gap:8px;text-align:center}.tax-documents-preview .td-upload-compact .td-upload-area{min-height:36px;padding:6px 12px;flex-direction:row;justify-content:flex-start;font-size:12px}.tax-documents-preview .td-upload-area [data-upload]{width:auto}.tax-documents-preview .td-upload-area input[type=file]{cursor:pointer}.tax-documents-preview .td-paperclip{font-size:24px;color:#aeb8c4}.tax-documents-preview .td-upload-compact .td-paperclip{font-size:16px}.tax-documents-preview .td-upload-compact .td-upload-help{display:none}.tax-documents-preview .td-file-row{display:flex;align-items:center;gap:8px;margin-top:12px;padding:5px 10px;background:#f1f3f5;border:1px solid var(--td-border);border-radius:5px;min-width:0;color:#a3adb9}.tax-documents-preview .td-file-name{overflow-wrap:anywhere;min-width:0;flex:1}.tax-documents-preview .td-file-ok{color:#329d49;margin-left:auto}.tax-documents-preview .td-coverage{font-size:12px;margin-top:12px}\n.tax-documents-preview .td-tracking{border:1px solid var(--td-border);border-radius:6px;margin-top:14px;padding:0 10px}.tax-documents-preview .td-tracking-header{display:block;width:100%;border:0;background:#fff;padding:10px 0;text-align:left;font-size:12px;color:#292e33;height:auto}.tax-documents-preview .td-timeline-event{position:relative;margin:2px 0 12px 6px;padding:0 0 0 16px;border-left:1px dashed #b6bfca;color:#8d969f;font-size:12px;white-space:pre-line}.tax-documents-preview .td-timeline-event:before{content:\'\';position:absolute;width:6px;height:6px;left:-3.5px;top:5px;border-radius:50%;background:currentColor}.tax-documents-preview .td-event-danger{color:#eb3440}.tax-documents-preview .td-event-info{color:#1870ff}.tax-documents-preview .td-event-success{color:#1870ff}.tax-documents-preview .td-event-title{font-weight:500}.tax-documents-preview .td-event-date{font-size:11px}.tax-documents-preview .td-suspended{color:#289ac2;font-size:16px;cursor:help}\n.tax-documents-preview.td-modal-overlay{position:fixed;inset:0;z-index:1000;min-height:100%;background:#142a4666;display:flex;align-items:center;justify-content:center;padding:18px}.tax-documents-preview .td-dialog{background:#fff;border-radius:12px;box-shadow:0 20px 60px #142a4640;width:460px;max-width:100%;max-height:90vh;overflow:auto;padding:24px}.tax-documents-preview .td-dialog-title{font-size:18px;font-weight:600;margin-bottom:8px}.tax-documents-preview .td-year-choice{display:block;width:100%;border:1px solid var(--td-border);border-radius:5px;margin:7px 0;padding:8px 12px;text-align:left;background:white;color:#333;font-size:13px;height:auto}.tax-documents-preview .td-year-choice[aria-pressed=true]{border-color:#649aff;background:#f0f6ff;color:#0659c8}.tax-documents-preview textarea{width:100%;min-height:90px;margin-top:8px}.tax-documents-preview button:focus-visible,.tax-documents-preview input:focus-visible,.tax-documents-preview textarea:focus-visible,.tax-documents-preview select:focus-visible{outline:2px solid #0667f9;outline-offset:3px}.tax-documents-preview button:disabled{opacity:.65;cursor:default}\n@media(max-width:600px){.tax-documents-preview{padding:10px}.tax-documents-preview .td-panel{padding:12px}.tax-documents-preview .td-card-header{padding:0 10px;gap:6px}.tax-documents-preview .td-card-body{padding:0 10px 12px}.tax-documents-preview .td-card-toggle{font-size:12px}.tax-documents-preview .td-badge{font-size:10px;padding:4px 6px}.tax-documents-preview .td-tab{font-size:11px;padding:10px 6px}.tax-documents-preview .td-preview-tools select{min-width:0;width:100%}.tax-documents-preview .td-action-bar{align-items:stretch}.tax-documents-preview .td-upload-area{min-height:130px}.tax-documents-preview .td-upload-compact .td-upload-area{flex-wrap:wrap}.tax-documents-preview .td-dialog{padding:18px}}\n";
    taxDocumentsPreview.SetTitle("\"Tax Documents Preview\"");
    taxDocumentsPreview.URLStructure = OutSystems.Model.Enumerations.URLStructure.QueryString; // default value
    taxDocumentsPreview.VerticalPosition = 700;
    
    var demo = taxDocumentsPreview.CreateLocalVariable("Demo");
    var taxPreviewStateVM = eSpace.Structures.Named("TaxPreviewStateVM");
    demo.DataType = taxPreviewStateVM;
    demo.Description = null; // default value
    
    var scenarioChoice = taxDocumentsPreview.CreateLocalVariable("ScenarioChoice");
    scenarioChoice.DataType = eSpace.TextType;
    scenarioChoice.SetDefaultValue("\"all\"");
    scenarioChoice.Description = null; // default value
    taxDocumentsPreview.OnDestroy.Destination = null; // default value
    taxDocumentsPreview.OnReady.Destination = null; // default value
    taxDocumentsPreview.OnRender.Destination = null; // default value
    
    var changePreset = taxDocumentsPreview.CreateScreenAction("ChangePreset");
    changePreset.Description = null; // default value
    
    var startNode = changePreset.CreateNode<OutSystems.Model.Logic.Nodes.IStartNode>();
    startNode.HorizontalPosition = 3200;
    startNode.IsDisabled = false; // default value
    startNode.VerticalPosition = 800;
    
    var initializeDemo = taxDocumentsPreview.CreateScreenAction("InitializeDemo");
    initializeDemo.Description = null; // default value
    
    var startNode2 = initializeDemo.CreateNode<OutSystems.Model.Logic.Nodes.IStartNode>();
    startNode2.HorizontalPosition = 3200;
    startNode2.IsDisabled = false; // default value
    startNode2.VerticalPosition = 800;
    
    var applyPreviewIntent = initializeDemo.CreateNode<OutSystems.Model.Logic.Nodes.IExecuteClientActionNode>("ApplyPreviewIntent").ConnectedBelow(startNode2, 1371);
    applyPreviewIntent.IsDisabled = false; // default value
    
    var endNode = initializeDemo.CreateNode<OutSystems.Model.Logic.Nodes.IEndNode>().ConnectedBelow(applyPreviewIntent, 1371);
    endNode.IsDisabled = false; // default value
    taxDocumentsPreview.OnInitialize.Destination = initializeDemo;
    
    var applyPreviewIntent2 = changePreset.CreateNode<OutSystems.Model.Logic.Nodes.IExecuteClientActionNode>("ApplyPreviewIntent").ConnectedBelow(startNode, 1371);
    applyPreviewIntent2.IsDisabled = false; // default value
    
    var handleIntent = taxDocumentsPreview.CreateScreenAction("HandleIntent");
    handleIntent.Description = null; // default value
    
    var requestCommand = handleIntent.CreateInputParameter("RequestCommand");
    requestCommand.DataType = eSpace.TextType;
    requestCommand.Description = null; // default value
    requestCommand.IsMandatory = true; // default value
    
    var requestKey = handleIntent.CreateInputParameter("RequestKey");
    requestKey.DataType = eSpace.TextType;
    requestKey.Description = null; // default value
    requestKey.IsMandatory = true; // default value
    
    var requestPayload = handleIntent.CreateInputParameter("RequestPayload");
    requestPayload.DataType = eSpace.TextType;
    requestPayload.Description = null; // default value
    requestPayload.IsMandatory = true; // default value
    
    var startNode3 = handleIntent.CreateNode<OutSystems.Model.Logic.Nodes.IStartNode>();
    startNode3.HorizontalPosition = 3200;
    startNode3.IsDisabled = false; // default value
    startNode3.VerticalPosition = 800;
    
    var serializeState = handleIntent.CreateNode<OutSystems.Model.Logic.Nodes.IJSONSerializeNode>("SerializeState").ConnectedBelow(startNode3, 1371);
    serializeState.SetData("Demo");
    serializeState.DateFormat = OutSystems.Model.Enumerations.JSONDateFormat.ISO; // default value
    serializeState.Description = null; // default value
    serializeState.IsDisabled = false; // default value
    serializeState.SerializeDefaultValues = true;
    
    var reducePreviewState = handleIntent.CreateNode<OutSystems.Model.Logic.Nodes.IJavaScriptNode>("ReducePreviewState").ConnectedBelow(serializeState, 1371);
    reducePreviewState.Description = null; // default value
    reducePreviewState.IsDisabled = false; // default value
    reducePreviewState.JavaScript = "$parameters.ResultJSON=JSON.stringify(window.TaxDocumentsPrototype.reduce(JSON.parse($parameters.StateJSON),$parameters.Command,$parameters.DocumentKey,$parameters.Payload,{COR:$parameters.COR,PEL:$parameters.PEL,PendingUpload:$parameters.PendingUpload,PendingReview:$parameters.PendingReview,Accepted:$parameters.Accepted,Rejected:$parameters.Rejected,NotProvidable:$parameters.NotProvidable,NotProvidableReview:$parameters.NotProvidableReview}));";
    
    var stateJSON = reducePreviewState.CreateInputParameter("StateJSON");
    stateJSON.DataType = eSpace.TextType;
    stateJSON.Description = null; // default value
    stateJSON.IsMandatory = true; // default value
    
    var command = reducePreviewState.CreateInputParameter("Command");
    command.DataType = eSpace.TextType;
    command.Description = null; // default value
    command.IsMandatory = true; // default value
    
    var documentKey = reducePreviewState.CreateInputParameter("DocumentKey");
    documentKey.DataType = eSpace.TextType;
    documentKey.Description = null; // default value
    documentKey.IsMandatory = true; // default value
    
    var payload = reducePreviewState.CreateInputParameter("Payload");
    payload.DataType = eSpace.TextType;
    payload.Description = null; // default value
    payload.IsMandatory = true; // default value
    
    var cOR = reducePreviewState.CreateInputParameter("COR");
    cOR.DataType = eSpace.IntegerType;
    cOR.Description = null; // default value
    cOR.IsMandatory = true; // default value
    
    var pEL = reducePreviewState.CreateInputParameter("PEL");
    pEL.DataType = eSpace.IntegerType;
    pEL.Description = null; // default value
    pEL.IsMandatory = true; // default value
    
    var pendingUpload = reducePreviewState.CreateInputParameter("PendingUpload");
    pendingUpload.DataType = eSpace.IntegerType;
    pendingUpload.Description = null; // default value
    pendingUpload.IsMandatory = true; // default value
    
    var pendingReview = reducePreviewState.CreateInputParameter("PendingReview");
    pendingReview.DataType = eSpace.IntegerType;
    pendingReview.Description = null; // default value
    pendingReview.IsMandatory = true; // default value
    
    var accepted = reducePreviewState.CreateInputParameter("Accepted");
    accepted.DataType = eSpace.IntegerType;
    accepted.Description = null; // default value
    accepted.IsMandatory = true; // default value
    
    var rejected = reducePreviewState.CreateInputParameter("Rejected");
    rejected.DataType = eSpace.IntegerType;
    rejected.Description = null; // default value
    rejected.IsMandatory = true; // default value
    
    var notProvidable = reducePreviewState.CreateInputParameter("NotProvidable");
    notProvidable.DataType = eSpace.IntegerType;
    notProvidable.Description = null; // default value
    notProvidable.IsMandatory = true; // default value
    
    var notProvidableReview = reducePreviewState.CreateInputParameter("NotProvidableReview");
    notProvidableReview.DataType = eSpace.IntegerType;
    notProvidableReview.Description = null; // default value
    notProvidableReview.IsMandatory = true; // default value
    
    var resultJSON = reducePreviewState.CreateOutputParameter("ResultJSON");
    resultJSON.DataType = eSpace.TextType;
    resultJSON.SetDefaultValue(null); // default value
    resultJSON.Description = null; // default value
    
    var readPreviewState = handleIntent.CreateNode<OutSystems.Model.Logic.Nodes.IJSONDeserializeNode>("ReadPreviewState").ConnectedBelow(reducePreviewState, 1371);
    readPreviewState.DataType = taxPreviewStateVM;
    readPreviewState.DateFormat = OutSystems.Model.Enumerations.JSONDateFormat.ISO; // default value
    readPreviewState.Description = null; // default value
    readPreviewState.IsDisabled = false; // default value
    readPreviewState.SetJSONString("ReducePreviewState.ResultJSON");
    
    var assignNode = handleIntent.CreateNode<OutSystems.Model.Logic.Nodes.IAssignNode>().ConnectedBelow(readPreviewState, 1371);
    assignNode.IsDisabled = false; // default value
    assignNode.Label = null; // default value
    
    var assignment = assignNode.CreateAssignment("Demo", "ReadPreviewState.Data");
    
    var assignment2 = assignNode.CreateAssignment("ScenarioChoice", "ReadPreviewState.Data.Scenario");
    
    var endNode2 = handleIntent.CreateNode<OutSystems.Model.Logic.Nodes.IEndNode>().ConnectedBelow(assignNode, 1371);
    endNode2.IsDisabled = false; // default value
    applyPreviewIntent.Action = handleIntent;
    applyPreviewIntent.SetArgumentValue(requestKey, "\"\"");
    applyPreviewIntent.SetArgumentValue(requestPayload, "\"\"");
    applyPreviewIntent.SetArgumentValue(requestCommand, "\"reset\"");
    applyPreviewIntent2.Action = handleIntent;
    
    var endNode3 = changePreset.CreateNode<OutSystems.Model.Logic.Nodes.IEndNode>().ConnectedBelow(applyPreviewIntent2, 1371);
    endNode3.IsDisabled = false; // default value
    applyPreviewIntent2.SetArgumentValue(requestCommand, "\"preset\"");
    applyPreviewIntent2.SetArgumentValue(requestKey, "\"\"");
    applyPreviewIntent2.SetArgumentValue(requestPayload, "ScenarioChoice");
    reducePreviewState.SetArgumentValue(pEL, "Entities.DocumentType.PEL");
    reducePreviewState.SetArgumentValue(cOR, "Entities.DocumentType.COR");
    reducePreviewState.SetArgumentValue(stateJSON, "SerializeState.JSON");
    reducePreviewState.SetArgumentValue(documentKey, "RequestKey");
    reducePreviewState.SetArgumentValue(payload, "RequestPayload");
    reducePreviewState.SetArgumentValue(pendingReview, "Entities.DocumentStatus.PendingReview");
    reducePreviewState.SetArgumentValue(notProvidableReview, "Entities.DocumentStatus.NotProvidableReview");
    reducePreviewState.SetArgumentValue(pendingUpload, "Entities.DocumentStatus.PendingUpload");
    reducePreviewState.SetArgumentValue(accepted, "Entities.DocumentStatus.Accepted");
    reducePreviewState.SetArgumentValue(rejected, "Entities.DocumentStatus.Rejected");
    reducePreviewState.SetArgumentValue(command, "RequestCommand");
    reducePreviewState.SetArgumentValue(notProvidable, "Entities.DocumentStatus.NotProvidable");
    
    var container = taxDocumentsPreview.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container.Animate = false; // default value
    container.ColumnGap = null; // default value
    container.ColumnSpan = null; // default value
    container.CustomStyle = null; // default value
    container.FlexBasis = null; // default value
    container.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container.Gap = null;
    container.GridColumns = null; // default value
    container.GridRows = null; // default value
    container.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container.RowGap = null; // default value
    container.RowSpan = null; // default value
    container.SetStyle("\"tax-documents-preview\"");
    container.SetVisible("True"); // default value
    container.VisibleWasExpression = false; // default value
    container.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container.Width = "(fill parent)"; // default value
    
    var container2 = container.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container2.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container2.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container2.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container2.Animate = false; // default value
    container2.ColumnGap = null; // default value
    container2.ColumnSpan = null; // default value
    container2.CustomStyle = null; // default value
    container2.FlexBasis = null; // default value
    container2.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container2.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container2.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container2.Gap = null;
    container2.GridColumns = null; // default value
    container2.GridRows = null; // default value
    container2.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container2.RowGap = null; // default value
    container2.RowSpan = null; // default value
    container2.SetStyle("\"td-shell\"");
    container2.SetVisible("True"); // default value
    container2.VisibleWasExpression = false; // default value
    container2.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container2.Width = "(fill parent)"; // default value
    
    var container3 = container2.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container3.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container3.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container3.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container3.Animate = false; // default value
    container3.ColumnGap = null; // default value
    container3.ColumnSpan = null; // default value
    container3.CustomStyle = null; // default value
    container3.FlexBasis = null; // default value
    container3.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container3.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container3.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container3.Gap = null;
    container3.GridColumns = null; // default value
    container3.GridRows = null; // default value
    container3.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container3.RowGap = null; // default value
    container3.RowSpan = null; // default value
    container3.SetStyle("\"td-preview-controls\"");
    container3.SetVisible("True"); // default value
    container3.VisibleWasExpression = false; // default value
    container3.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container3.Width = "(fill parent)"; // default value
    
    var button = container3.CreateWidget<ServiceStudio.Plugin.NRWidgets.IButton>();
    /*** Deleting Widgets that are created by default when instantiating an IButton ***/
    button.Widgets.ToList().ForEach(x => x.Delete());
    button.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    button.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    button.ColumnGap = null; // default value
    button.ColumnSpan = null; // default value
    button.SetConfirmationMessage(null); // default value
    button.CustomStyle = null; // default value
    button.SetEnabled("True");
    button.FlexBasis = null; // default value
    button.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    button.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    button.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    button.Gap = null;
    button.GridColumns = null; // default value
    button.GridRows = null; // default value
    button.IsDefault = false; // default value
    button.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    button.RowGap = null; // default value
    button.RowSpan = null; // default value
    button.SetStyle("\"td-link\"");
    button.SetVisible("True"); // default value
    button.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    button.Width = ""; // default value
    
    var expression = button.CreateWidget<ServiceStudio.Plugin.NRWidgets.IExpression>();
    expression.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    expression.ColumnSpan = null; // default value
    expression.CustomStyle = null; // default value
    expression.Example = null; // default value
    expression.FlexBasis = null; // default value
    expression.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    expression.RowSpan = null; // default value
    expression.SetStyle(null); // default value
    expression.SetValue("\"Preview controls — prototype tooling \" + If(Demo.ShowControls,\"⌃\",\"⌄\")");
    expression.Width = ""; // default value
    var builtinEvent = button.OnClick;
    builtinEvent.BuiltInValidations = OutSystems.Model.Enumerations.ValidationBehavior.None; // default value
    builtinEvent.Destination = handleIntent;
    builtinEvent.Transition = OutSystems.Model.Enumerations.TransitionTypeWithInheritance.Inherited; // default value
    builtinEvent.SetArgumentValue(requestKey, "\"\"");
    builtinEvent.SetArgumentValue(requestCommand, "\"controls\"");
    builtinEvent.SetArgumentValue(requestPayload, "\"\"");
    
    var extendedProperty = button.CreateExtendedProperty();
    extendedProperty.Property = "aria-expanded";
    extendedProperty.SetValue("If(Demo.ShowControls,\"true\",\"false\")");
    
    var ifWidget = container3.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.IIfWidget>();
    ifWidget.Animate = false; // default value
    ifWidget.SetCondition("Demo.ShowControls");
    ifWidget.CustomStyle = null; // default value
    ifWidget.DesignMode = OutSystems.Model.Enumerations.DesignMode.ShowAll; // default value
    
    var container4 = ifWidget.TrueBranch.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container4.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container4.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container4.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container4.Animate = false; // default value
    container4.ColumnGap = null; // default value
    container4.ColumnSpan = null; // default value
    container4.CustomStyle = null; // default value
    container4.FlexBasis = null; // default value
    container4.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container4.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container4.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container4.Gap = null;
    container4.GridColumns = null; // default value
    container4.GridRows = null; // default value
    container4.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container4.RowGap = null; // default value
    container4.RowSpan = null; // default value
    container4.SetStyle("\"td-preview-tools\"");
    container4.SetVisible("True"); // default value
    container4.VisibleWasExpression = false; // default value
    container4.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container4.Width = "(fill parent)"; // default value
    
    var textWidget = container4.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.ITextWidget>();
    textWidget.CustomStyle = null; // default value
    textWidget.SetStyleClasses(null); // default value
    textWidget.Text = "Scenario";
    
    var previewScenario = container4.CreateWidget<ServiceStudio.Plugin.NRWidgets.IDropdown>("PreviewScenario");
    previewScenario.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    previewScenario.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    previewScenario.ColumnGap = null; // default value
    previewScenario.ColumnSpan = null; // default value
    previewScenario.CustomStyle = null; // default value
    previewScenario.DropdownMode = ServiceStudio.Plugin.NRWidgets.Enumerations.DropdownMode.Text;
    previewScenario.SetEmptyValue(null); // default value
    previewScenario.SetEnabled("True");
    previewScenario.FlexBasis = null; // default value
    previewScenario.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    previewScenario.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    previewScenario.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    previewScenario.Gap = null;
    previewScenario.GridColumns = null; // default value
    previewScenario.GridRows = null; // default value
    previewScenario.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    previewScenario.SetLabels("Label");
    previewScenario.SetList("Demo.Scenarios");
    previewScenario.SetMandatory("False");
    previewScenario.RowGap = null; // default value
    previewScenario.RowSpan = null; // default value
    previewScenario.SetStyle("\"dropdown\""); // default value
    previewScenario.SetValues("Code");
    previewScenario.SetVariable("ScenarioChoice");
    previewScenario.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    previewScenario.Width = ""; // default value
    var builtinEvent2 = previewScenario.OnChange;
    builtinEvent2.BuiltInValidations = OutSystems.Model.Enumerations.ValidationBehavior.None; // default value
    builtinEvent2.Destination = changePreset;
    builtinEvent2.Transition = OutSystems.Model.Enumerations.TransitionTypeWithInheritance.Inherited; // default value
    
    var extendedProperty2 = previewScenario.CreateExtendedProperty();
    extendedProperty2.Property = "aria-label";
    extendedProperty2.SetValue("\"Preview reference scenario\"");
    
    var button2 = container4.CreateWidget<ServiceStudio.Plugin.NRWidgets.IButton>();
    button2.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    button2.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    button2.ColumnGap = null; // default value
    button2.ColumnSpan = null; // default value
    button2.SetConfirmationMessage(null); // default value
    button2.CustomStyle = null; // default value
    button2.SetEnabled("True");
    button2.FlexBasis = null; // default value
    button2.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    button2.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    button2.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    button2.Gap = null;
    button2.GridColumns = null; // default value
    button2.GridRows = null; // default value
    button2.IsDefault = false; // default value
    button2.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    button2.RowGap = null; // default value
    button2.RowSpan = null; // default value
    button2.SetStyle("\"td-button\"");
    button2.SetVisible("True"); // default value
    button2.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    button2.Width = ""; // default value
    
    var textWidget2 = (OutSystems.Model.UI.Mobile.Widgets.ITextWidget)button2.Widgets.First();
    textWidget2.CustomStyle = null; // default value
    textWidget2.Name = null; // default value
    textWidget2.SetStyleClasses(null); // default value
    textWidget2.Text = "Reset demo";
    var builtinEvent3 = button2.OnClick;
    builtinEvent3.BuiltInValidations = OutSystems.Model.Enumerations.ValidationBehavior.None; // default value
    builtinEvent3.Destination = handleIntent;
    builtinEvent3.Transition = OutSystems.Model.Enumerations.TransitionTypeWithInheritance.Inherited; // default value
    builtinEvent3.SetArgumentValue(requestPayload, "\"\"");
    builtinEvent3.SetArgumentValue(requestCommand, "\"reset\"");
    builtinEvent3.SetArgumentValue(requestKey, "\"\"");
    
    var container5 = ifWidget.TrueBranch.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container5.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container5.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container5.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container5.Animate = false; // default value
    container5.ColumnGap = null; // default value
    container5.ColumnSpan = null; // default value
    container5.CustomStyle = null; // default value
    container5.FlexBasis = null; // default value
    container5.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container5.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container5.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container5.Gap = null;
    container5.GridColumns = null; // default value
    container5.GridRows = null; // default value
    container5.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container5.RowGap = null; // default value
    container5.RowSpan = null; // default value
    container5.SetStyle("\"td-muted\"");
    container5.SetVisible("True"); // default value
    container5.VisibleWasExpression = false; // default value
    container5.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container5.Width = "(fill parent)"; // default value
    
    var textWidget3 = container5.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.ITextWidget>();
    textWidget3.CustomStyle = null; // default value
    textWidget3.SetStyleClasses(null); // default value
    textWidget3.Text = "All states is a composite showcase. Review modes and transitions are illustrative only.";
    
    var container6 = container2.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container6.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container6.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container6.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container6.Animate = false; // default value
    container6.ColumnGap = null; // default value
    container6.ColumnSpan = null; // default value
    container6.CustomStyle = null; // default value
    container6.FlexBasis = null; // default value
    container6.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container6.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container6.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container6.Gap = null;
    container6.GridColumns = null; // default value
    container6.GridRows = null; // default value
    container6.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container6.RowGap = null; // default value
    container6.RowSpan = null; // default value
    container6.SetStyle("\"td-feedback\"");
    container6.SetVisible("True"); // default value
    container6.VisibleWasExpression = false; // default value
    container6.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container6.Width = "(fill parent)"; // default value
    
    var expression2 = container6.CreateWidget<ServiceStudio.Plugin.NRWidgets.IExpression>();
    expression2.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    expression2.ColumnSpan = null; // default value
    expression2.CustomStyle = null; // default value
    expression2.Example = null; // default value
    expression2.FlexBasis = null; // default value
    expression2.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    expression2.RowSpan = null; // default value
    expression2.SetStyle(null); // default value
    expression2.SetValue("Demo.Feedback");
    expression2.Width = ""; // default value
    
    var extendedProperty3 = container6.CreateExtendedProperty();
    extendedProperty3.Property = "role";
    extendedProperty3.SetValue("\"status\"");
    
    var extendedProperty4 = container6.CreateExtendedProperty();
    extendedProperty4.Property = "aria-live";
    extendedProperty4.SetValue("\"polite\"");
    
    var container7 = container2.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container7.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container7.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container7.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container7.Animate = false; // default value
    container7.ColumnGap = null; // default value
    container7.ColumnSpan = null; // default value
    container7.CustomStyle = null; // default value
    container7.FlexBasis = null; // default value
    container7.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container7.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container7.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container7.Gap = null;
    container7.GridColumns = null; // default value
    container7.GridRows = null; // default value
    container7.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container7.RowGap = null; // default value
    container7.RowSpan = null; // default value
    container7.SetStyle("\"td-panel\"");
    container7.SetVisible("True"); // default value
    container7.VisibleWasExpression = false; // default value
    container7.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container7.Width = "(fill parent)"; // default value
    
    var ifWidget2 = container7.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.IIfWidget>();
    ifWidget2.Animate = false; // default value
    ifWidget2.SetCondition("Demo.ShowTabs");
    ifWidget2.CustomStyle = null; // default value
    ifWidget2.DesignMode = OutSystems.Model.Enumerations.DesignMode.ShowAll; // default value
    
    var documentTypeTabsInstance = ifWidget2.TrueBranch.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.IMobileBlockInstanceWidget>();
    documentTypeTabsInstance.CustomStyle = null; // default value
    documentTypeTabsInstance.DesignMode = OutSystems.Model.Enumerations.DesignMode.ShowAll; // default value
    var documentTypeTabs = mainFlow.Nodes.OfType<OutSystems.Model.UI.Mobile.IMobileBlock>().Named("DocumentTypeTabs");
    documentTypeTabsInstance.SourceBlock = documentTypeTabs;
    var activeDocumentType = documentTypeTabs.InputParameters.Named("ActiveDocumentType");
    documentTypeTabsInstance.SetArgumentValue(activeDocumentType, "Demo.ActiveDocumentType");
    var eventHandler = documentTypeTabsInstance.EventHandlers.FirstOrDefault(e => e.Event.Name == "TypeChanged");
    eventHandler.Handler = handleIntent;
    eventHandler.SetArgumentValue(requestPayload, "RequestPayload");
    eventHandler.SetArgumentValue(requestKey, "RequestKey");
    eventHandler.SetArgumentValue(requestCommand, "RequestCommand");
    
    var container8 = ifWidget2.FalseBranch.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container8.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container8.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container8.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container8.Animate = false; // default value
    container8.ColumnGap = null; // default value
    container8.ColumnSpan = null; // default value
    container8.CustomStyle = null; // default value
    container8.FlexBasis = null; // default value
    container8.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container8.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container8.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container8.Gap = null;
    container8.GridColumns = null; // default value
    container8.GridRows = null; // default value
    container8.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container8.RowGap = null; // default value
    container8.RowSpan = null; // default value
    container8.SetStyle("\"td-heading\"");
    container8.SetVisible("True"); // default value
    container8.VisibleWasExpression = false; // default value
    container8.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container8.Width = "(fill parent)"; // default value
    
    var expression3 = container8.CreateWidget<ServiceStudio.Plugin.NRWidgets.IExpression>();
    expression3.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    expression3.ColumnSpan = null; // default value
    expression3.CustomStyle = null; // default value
    expression3.Example = null; // default value
    expression3.FlexBasis = null; // default value
    expression3.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    expression3.RowSpan = null; // default value
    expression3.SetStyle(null); // default value
    expression3.SetValue("If(Demo.ActiveDocumentType = Entities.DocumentType.COR,\"Certificate of Tax Residence (COR)\",\"Permanent Establishment Letter (PEL)\")");
    expression3.Width = ""; // default value
    
    var ifWidget3 = container7.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.IIfWidget>();
    ifWidget3.Animate = false; // default value
    ifWidget3.SetCondition("Demo.IsReviewer");
    ifWidget3.CustomStyle = null; // default value
    ifWidget3.DesignMode = OutSystems.Model.Enumerations.DesignMode.ShowAll; // default value
    
    var container9 = ifWidget3.TrueBranch.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container9.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container9.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container9.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container9.Animate = false; // default value
    container9.ColumnGap = null; // default value
    container9.ColumnSpan = null; // default value
    container9.CustomStyle = null; // default value
    container9.FlexBasis = null; // default value
    container9.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container9.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container9.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container9.Gap = null;
    container9.GridColumns = null; // default value
    container9.GridRows = null; // default value
    container9.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container9.RowGap = null; // default value
    container9.RowSpan = null; // default value
    container9.SetStyle("\"td-intro\"");
    container9.SetVisible("True"); // default value
    container9.VisibleWasExpression = false; // default value
    container9.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container9.Width = "(fill parent)"; // default value
    
    var expression4 = container9.CreateWidget<ServiceStudio.Plugin.NRWidgets.IExpression>();
    expression4.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    expression4.ColumnSpan = null; // default value
    expression4.CustomStyle = null; // default value
    expression4.Example = null; // default value
    expression4.FlexBasis = null; // default value
    expression4.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    expression4.RowSpan = null; // default value
    expression4.SetStyle(null); // default value
    expression4.SetValue("\"Please carefully review the \" + If(Demo.ActiveDocumentType = Entities.DocumentType.COR,\"Certificate of Tax Residence (COR)\",\"Permanent Establishment Letter (PEL)\") + \" that the submitter uploaded.\"");
    expression4.Width = ""; // default value
    
    var textWidget4 = container9.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.ITextWidget>();
    textWidget4.CustomStyle = null; // default value
    textWidget4.SetStyleClasses(null); // default value
    textWidget4.Text = "If one document covers multiple years but the Submitter has not uploaded it to the other year(s), you can suspend the reminder below. Multiple year selection is applicable.";
    
    var button3 = ifWidget3.TrueBranch.CreateWidget<ServiceStudio.Plugin.NRWidgets.IButton>();
    button3.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    button3.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    button3.ColumnGap = null; // default value
    button3.ColumnSpan = null; // default value
    button3.SetConfirmationMessage(null); // default value
    button3.CustomStyle = null; // default value
    button3.SetEnabled("True");
    button3.FlexBasis = null; // default value
    button3.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    button3.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    button3.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    button3.Gap = null;
    button3.GridColumns = null; // default value
    button3.GridRows = null; // default value
    button3.IsDefault = false; // default value
    button3.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    button3.RowGap = null; // default value
    button3.RowSpan = null; // default value
    button3.SetStyle("\"td-link\"");
    button3.SetVisible("True"); // default value
    button3.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    button3.Width = ""; // default value
    
    var textWidget5 = (OutSystems.Model.UI.Mobile.Widgets.ITextWidget)button3.Widgets.First();
    textWidget5.CustomStyle = null; // default value
    textWidget5.Name = null; // default value
    textWidget5.SetStyleClasses(null); // default value
    textWidget5.Text = "Suspend Reminder";
    var builtinEvent4 = button3.OnClick;
    builtinEvent4.BuiltInValidations = OutSystems.Model.Enumerations.ValidationBehavior.None; // default value
    builtinEvent4.Destination = handleIntent;
    builtinEvent4.Transition = OutSystems.Model.Enumerations.TransitionTypeWithInheritance.Inherited; // default value
    builtinEvent4.SetArgumentValue(requestKey, "\"\"");
    builtinEvent4.SetArgumentValue(requestCommand, "\"suspend\"");
    builtinEvent4.SetArgumentValue(requestPayload, "\"\"");
    
    var button4 = ifWidget3.FalseBranch.CreateWidget<ServiceStudio.Plugin.NRWidgets.IButton>();
    button4.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    button4.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    button4.ColumnGap = null; // default value
    button4.ColumnSpan = null; // default value
    button4.SetConfirmationMessage(null); // default value
    button4.CustomStyle = null; // default value
    button4.SetEnabled("True");
    button4.FlexBasis = null; // default value
    button4.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    button4.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    button4.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    button4.Gap = null;
    button4.GridColumns = null; // default value
    button4.GridRows = null; // default value
    button4.IsDefault = false; // default value
    button4.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    button4.RowGap = null; // default value
    button4.RowSpan = null; // default value
    button4.SetStyle("\"td-button td-outline\"");
    button4.SetVisible("True"); // default value
    button4.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    button4.Width = ""; // default value
    
    var textWidget6 = (OutSystems.Model.UI.Mobile.Widgets.ITextWidget)button4.Widgets.First();
    textWidget6.CustomStyle = null; // default value
    textWidget6.Name = null; // default value
    textWidget6.SetStyleClasses(null); // default value
    textWidget6.Text = "⇩ Download Specimen Template";
    var builtinEvent5 = button4.OnClick;
    builtinEvent5.BuiltInValidations = OutSystems.Model.Enumerations.ValidationBehavior.None; // default value
    builtinEvent5.Destination = handleIntent;
    builtinEvent5.Transition = OutSystems.Model.Enumerations.TransitionTypeWithInheritance.Inherited; // default value
    builtinEvent5.SetArgumentValue(requestKey, "\"\"");
    builtinEvent5.SetArgumentValue(requestCommand, "\"sample\"");
    builtinEvent5.SetArgumentValue(requestPayload, "\"\"");
    
    var container10 = ifWidget3.FalseBranch.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container10.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container10.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container10.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container10.Animate = false; // default value
    container10.ColumnGap = null; // default value
    container10.ColumnSpan = null; // default value
    container10.CustomStyle = null; // default value
    container10.FlexBasis = null; // default value
    container10.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container10.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container10.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container10.Gap = null;
    container10.GridColumns = null; // default value
    container10.GridRows = null; // default value
    container10.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container10.RowGap = null; // default value
    container10.RowSpan = null; // default value
    container10.SetStyle("\"td-intro\"");
    container10.SetVisible("True"); // default value
    container10.VisibleWasExpression = false; // default value
    container10.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container10.Width = "(fill parent)"; // default value
    
    var textWidget7 = container10.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.ITextWidget>();
    textWidget7.CustomStyle = null; // default value
    textWidget7.SetStyleClasses(null); // default value
    textWidget7.Text = "• In case the Vendor is not able to provide the document, please ";
    
    var button5 = container10.CreateWidget<ServiceStudio.Plugin.NRWidgets.IButton>();
    button5.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    button5.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    button5.ColumnGap = null; // default value
    button5.ColumnSpan = null; // default value
    button5.SetConfirmationMessage(null); // default value
    button5.CustomStyle = null; // default value
    button5.SetEnabled("True");
    button5.FlexBasis = null; // default value
    button5.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    button5.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    button5.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    button5.Gap = null;
    button5.GridColumns = null; // default value
    button5.GridRows = null; // default value
    button5.IsDefault = false; // default value
    button5.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    button5.RowGap = null; // default value
    button5.RowSpan = null; // default value
    button5.SetStyle("\"td-link\"");
    button5.SetVisible("True"); // default value
    button5.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    button5.Width = ""; // default value
    
    var textWidget8 = (OutSystems.Model.UI.Mobile.Widgets.ITextWidget)button5.Widgets.First();
    textWidget8.CustomStyle = null; // default value
    textWidget8.Name = null; // default value
    textWidget8.SetStyleClasses(null); // default value
    textWidget8.Text = "click here";
    var builtinEvent6 = button5.OnClick;
    builtinEvent6.BuiltInValidations = OutSystems.Model.Enumerations.ValidationBehavior.None; // default value
    builtinEvent6.Destination = handleIntent;
    builtinEvent6.Transition = OutSystems.Model.Enumerations.TransitionTypeWithInheritance.Inherited; // default value
    builtinEvent6.SetArgumentValue(requestKey, "\"\"");
    builtinEvent6.SetArgumentValue(requestPayload, "\"\"");
    builtinEvent6.SetArgumentValue(requestCommand, "\"request\"");
    
    var textWidget9 = container10.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.ITextWidget>();
    textWidget9.CustomStyle = null; // default value
    textWidget9.SetStyleClasses(null); // default value
    textWidget9.Text = " for update.";
    
    var container11 = container10.CreateWidget<ServiceStudio.Plugin.NRWidgets.IContainer>();
    container11.Align = ServiceStudio.Plugin.NRWidgets.Enumerations.Align.Default; // default value
    container11.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    container11.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    container11.Animate = false; // default value
    container11.ColumnGap = null; // default value
    container11.ColumnSpan = null; // default value
    container11.CustomStyle = null; // default value
    container11.FlexBasis = null; // default value
    container11.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    container11.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    container11.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    container11.Gap = null;
    container11.GridColumns = null; // default value
    container11.GridRows = null; // default value
    container11.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    container11.RowGap = null; // default value
    container11.RowSpan = null; // default value
    container11.SetStyle(null); // default value
    container11.SetVisible("True"); // default value
    container11.VisibleWasExpression = false; // default value
    container11.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    container11.Width = "(fill parent)"; // default value
    
    var textWidget10 = container11.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.ITextWidget>();
    textWidget10.CustomStyle = null; // default value
    textWidget10.SetStyleClasses(null); // default value
    textWidget10.Text = "• In case the Vendor is able to provide the document, please upload it into its corresponding year below.";
    
    var ifWidget4 = ifWidget3.FalseBranch.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.IIfWidget>();
    ifWidget4.Animate = false; // default value
    ifWidget4.SetCondition("Demo.Scenario = \"all\"");
    ifWidget4.CustomStyle = null; // default value
    ifWidget4.DesignMode = OutSystems.Model.Enumerations.DesignMode.ShowAll; // default value
    
    var button6 = ifWidget4.TrueBranch.CreateWidget<ServiceStudio.Plugin.NRWidgets.IButton>();
    button6.AlignItems = OutSystems.Model.Enumerations.AlignItems.Stretch; // default value
    button6.AlignSelf = OutSystems.Model.Enumerations.AlignSelf.Auto; // default value
    button6.ColumnGap = null; // default value
    button6.ColumnSpan = null; // default value
    button6.SetConfirmationMessage(null); // default value
    button6.CustomStyle = null; // default value
    button6.SetEnabled("True");
    button6.FlexBasis = null; // default value
    button6.FlexDirection = OutSystems.Model.Enumerations.FlexDirection.Row; // default value
    button6.Flexible = OutSystems.Model.Enumerations.Flexible.Shrink; // default value
    button6.FlexWrap = OutSystems.Model.Enumerations.FlexWrap.NoWrap; // default value
    button6.Gap = null;
    button6.GridColumns = null; // default value
    button6.GridRows = null; // default value
    button6.IsDefault = false; // default value
    button6.JustifyContent = OutSystems.Model.Enumerations.JustifyContent.Start; // default value
    button6.RowGap = null; // default value
    button6.RowSpan = null; // default value
    button6.SetStyle("\"td-link\"");
    button6.SetVisible("True"); // default value
    button6.WidgetGridType = OutSystems.Model.Enumerations.WidgetGridType.None; // default value
    button6.Width = ""; // default value
    
    var textWidget11 = (OutSystems.Model.UI.Mobile.Widgets.ITextWidget)button6.Widgets.First();
    textWidget11.CustomStyle = null; // default value
    textWidget11.Name = null; // default value
    textWidget11.SetStyleClasses(null); // default value
    textWidget11.Text = "Suspend Reminder";
    var builtinEvent7 = button6.OnClick;
    builtinEvent7.BuiltInValidations = OutSystems.Model.Enumerations.ValidationBehavior.None; // default value
    builtinEvent7.Destination = handleIntent;
    builtinEvent7.Transition = OutSystems.Model.Enumerations.TransitionTypeWithInheritance.Inherited; // default value
    builtinEvent7.SetArgumentValue(requestPayload, "\"\"");
    builtinEvent7.SetArgumentValue(requestKey, "\"\"");
    builtinEvent7.SetArgumentValue(requestCommand, "\"suspend\"");
    
    var documentYearListInstance = container7.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.IMobileBlockInstanceWidget>();
    documentYearListInstance.CustomStyle = null; // default value
    documentYearListInstance.DesignMode = OutSystems.Model.Enumerations.DesignMode.ShowAll; // default value
    var documentYearList = mainFlow.Nodes.OfType<OutSystems.Model.UI.Mobile.IMobileBlock>().Named("DocumentYearList");
    documentYearListInstance.SourceBlock = documentYearList;
    var isComposite = documentYearList.InputParameters.Named("IsComposite");
    documentYearListInstance.SetArgumentValue(isComposite, "Demo.Scenario = \"all\"");
    var activeDocumentType2 = documentYearList.InputParameters.Named("ActiveDocumentType");
    documentYearListInstance.SetArgumentValue(activeDocumentType2, "Demo.ActiveDocumentType");
    var previewMode = documentYearList.InputParameters.Named("PreviewMode");
    documentYearListInstance.SetArgumentValue(previewMode, "Demo.IsReviewer or Demo.Scenario = \"022033\"");
    var documents = documentYearList.InputParameters.Named("Documents");
    documentYearListInstance.SetArgumentValue(documents, "Demo.Documents");
    var eventHandler2 = documentYearListInstance.EventHandlers.FirstOrDefault(e => e.Event.Name == "RowIntent");
    eventHandler2.Handler = handleIntent;
    eventHandler2.SetArgumentValue(requestPayload, "RequestPayload");
    eventHandler2.SetArgumentValue(requestCommand, "RequestCommand");
    eventHandler2.SetArgumentValue(requestKey, "RequestKey");
    
    var ifWidget5 = container2.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.IIfWidget>();
    ifWidget5.Animate = false; // default value
    ifWidget5.SetCondition("Demo.DialogKind <> \"\"");
    ifWidget5.CustomStyle = null; // default value
    ifWidget5.DesignMode = OutSystems.Model.Enumerations.DesignMode.ShowAll; // default value
    
    var yearSelectionDialogInstance = ifWidget5.TrueBranch.CreateWidget<OutSystems.Model.UI.Mobile.Widgets.IMobileBlockInstanceWidget>();
    yearSelectionDialogInstance.CustomStyle = null; // default value
    yearSelectionDialogInstance.DesignMode = OutSystems.Model.Enumerations.DesignMode.ShowAll; // default value
    var yearSelectionDialog = mainFlow.Nodes.OfType<OutSystems.Model.UI.Mobile.IMobileBlock>().Named("YearSelectionDialog");
    yearSelectionDialogInstance.SourceBlock = yearSelectionDialog;
    var dialogKind = yearSelectionDialog.InputParameters.Named("DialogKind");
    yearSelectionDialogInstance.SetArgumentValue(dialogKind, "Demo.DialogKind");
    var feedback = yearSelectionDialog.InputParameters.Named("Feedback");
    yearSelectionDialogInstance.SetArgumentValue(feedback, "Demo.Feedback");
    var years = yearSelectionDialog.InputParameters.Named("Years");
    yearSelectionDialogInstance.SetArgumentValue(years, "Demo.DialogYears");
    var eventHandler3 = yearSelectionDialogInstance.EventHandlers.FirstOrDefault(e => e.Event.Name == "SelectionIntent");
    eventHandler3.Handler = handleIntent;
    eventHandler3.SetArgumentValue(requestPayload, "RequestPayload");
    eventHandler3.SetArgumentValue(requestCommand, "RequestCommand");
    eventHandler3.SetArgumentValue(requestKey, "RequestKey");
}

```
