function UpdateScriptInfo() {
    var selectedScriptName = $('listAvaliableScripts').value;
    var scriptDescriptionSection = $('txtScriptDescription');
    var scriptSourseCodeSection = $('txtScriptSourceCode');

    var xhttpDesc = new XMLHttpRequest();
    var xhttpSour = new XMLHttpRequest();
    xhttpDesc.open("GET", "/api/scriptdescription/"+selectedScriptName, false);
    xhttpDesc.setRequestHeader("Content-type", "application/json");
    
    xhttpSour.open("GET", "/api/scriptsourcecode/" + selectedScriptName, false);
    xhttpSour.setRequestHeader("Content-type", "application/json");

    xhttpDesc.send();
    xhttpSour.send();

    scriptDescriptionSection.value = xhttpDesc.responseText;
    scriptSourseCodeSection.value = xhttpSour.responseText;
}


function NavigateToSelectedScript(){
    var selectedScriptName = $('listAvaliableScripts').value;
}
