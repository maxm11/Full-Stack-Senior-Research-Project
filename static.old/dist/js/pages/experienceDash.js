var currentTextScore = 1
var currentTextMag = 0.6

function colorGrad (value) {
    if(value<0){
        red = 255;
        if (value<-1){
            green = 0;
            blue = 0;
        }
        else{
            green = -1*(255*(value));
            blue = -1*(255*(value));
        };
    }
    else{
        blue = 255;
        if(value>1){
           red = 0;
           green = 0; 
        }
        else{
            red = 255 + (255*(-1*value));
            green = 255 + (255*(-1*value));
        }
    }
    red = Math.round(red)
    green = Math.round(green)
    blue = Math.round(blue)
    var rgbReturn = 'rgba('
    return rgbReturn.concat(red.toString()).concat(", ").concat(green.toString()).concat(", ").concat(blue.toString())
}
// Current Text Sentiment - Score Chart
var currentTextScoreChartData = {
        labels: [""],
        datasets: [{
            label: 'Score',
            backgroundColor: colorGrad(currentTextScore).concat(', 0.5)'),
            borderColor: colorGrad(currentTextScore).concat(', 1)'),
            borderWidth: 1,
            data: [
                currentTextScore
            ]
        }]

    };

// Current Text Sentiment - Magnitude Chart
var currentTextMagChartData = {
    labels: [""],
    datasets: [{
        label: 'Magnitude',
        backgroundColor: colorGrad(currentTextMag).concat(', 0.5)'),
        borderColor: colorGrad(currentTextMag).concat(', 1)'),
        borderWidth: 1,
        data: [
            currentTextMag
        ]
    }]

};


window.onload = function() {

    // Current Text Sentiment - Score Chart
    var ctx1 = document.getElementById("currentExpScore").getContext("2d");
    window.currentExpScore = new Chart(ctx1, {
        type: 'horizontalBar',
        data: currentTextScoreChartData,
        options: {
            // Elements options apply to all of the options unless overridden in a dataset
            // In this case, we are setting the border of each horizontal bar to be 2px wide
            elements: {
                rectangle: {
                    borderWidth: 2,
                }
            },
            scales: {
                xAxes:[{
                    ticks: {
                        min: -1,
                        max: 1
                    }
                }]
            },
            legend: {
                display: false
            },
            responsive: true
        }
    });

    // Current Text Sentiment - Magnitude Chart
    var ctx2 = document.getElementById("currentExpMag").getContext("2d");
    window.currentExpScore = new Chart(ctx2, {
        type: 'horizontalBar',
        data: currentTextMagChartData,
        options: {
            // Elements options apply to all of the options unless overridden in a dataset
            // In this case, we are setting the border of each horizontal bar to be 2px wide
            elements: {
                rectangle: {
                    borderWidth: 2,
                }
            },
            scales: {
                xAxes:[{
                    ticks: {
                        beginAtZero: true,
                        suggestedMax: 1
                    }
                }]
            },
            legend: {
                display: false
            },
            responsive: true
        }
    });
};
