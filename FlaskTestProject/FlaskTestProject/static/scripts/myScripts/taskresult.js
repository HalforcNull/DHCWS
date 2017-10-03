$(document).ready(function () {
    mydiv = document.getElementById('result1');
    data = {x:[1,2,3,4,5,6,7,8,9,10],
            y:[1,2,1,2,1,2,1,2,1,2]};
    t = [data];
    Plotly.plot(mydiv, t);
})