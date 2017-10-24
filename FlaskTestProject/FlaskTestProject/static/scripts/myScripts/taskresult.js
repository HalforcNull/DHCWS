$(document).ready(function () {
    idDiv = document.getElementById('task_id');
    task_id = idDiv.value; 
    for( lpIndex = 1; lpIndex < 10; lpIndex++)
    {
        mydiv = document.getElementById('result'+ '_' + lpIndex);

        if( !loadPlotlyResult(task_id, lpIndex, mydiv ) )
        { break; }
    }
    
    // mydiv = document.getElementById('result'+ '_' + 1);
    // loadPlotlyResult(1,1, mydiv);
    // mydiv = document.getElementById('result'+ '_' + 2);
    // loadPlotlyResult(1,2,mydiv);
    return;
});

function loadPlotlyResult(task_id, result_id, mydiv){
    if(mydiv == null || mydiv == undefined)
    {
        return false;
    }
    mydiv.value = 'Data Load Error';
    for( i = 1; i <= mydiv.getAttribute('datacount'); i++ )
    {
        file_id = i;
        Plotly.d3.csv("/api/datafile/"+task_id+ "/" + result_id + "/" + file_id, function(error,data)
        {
            if(error) return console.warn(error);

            xArray = data.map(function(data){return data['x']});
            yArray = data.map(function(data){return data['y']});
            plotData = {x:xArray, y:yArray};
            t = [plotData];

            Plotly.plot(mydiv,t);
        });
    }
    return true;
}