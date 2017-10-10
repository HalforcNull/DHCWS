$(document).ready(function () {/*
    mydiv = document.getElementById('result1');
    data = {x:[1,2,3,4,5,6,7,8,9,10],
            y:[1,2,1,2,1,2,1,2,1,2]};
    t = [data];
    Plotly.plot(mydiv, t);
*/

    loadPlotlyResult(1,1);
})

function loadPlotlyResult(task_id, file_id){
    mydiv = document.getElementById('result1');
    Plotly.d3.csv("/api/datafile/1/1", function(error,data)
    {
        if(error) return console.warn(error);

        xArray = data.map(function(data){return data['x']});
        yArray = data.map(function(data){return data['y']});
        plotData = {x:xArray, y:yArray};
        t = [plotData];

        Plotly.plot(mydiv,t);
    });
    
}