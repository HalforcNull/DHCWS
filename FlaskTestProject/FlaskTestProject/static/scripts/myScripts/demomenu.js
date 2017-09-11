function UpdateScriptInfo() {
    var selectedScriptName = document.getElementById('listAvaliableScripts').value;
    var scriptDescriptionSection = document.getElementById('txtScriptDescription');
    var scriptSourseCodeSection = document.getElementById('txtScriptSourceCode');

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