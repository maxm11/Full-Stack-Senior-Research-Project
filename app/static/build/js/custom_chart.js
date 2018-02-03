var ctxRadar1 = document.getElementById("canvasRadarPhysical").getContext("2d");
var dataRadar1 = {
    labels: ["Sickness", "Tiredness", "Hunger", "Thirst"],
    datasets: [{
        label: "Physical Wellness Variables",
        backgroundColor: "rgba(3, 88, 106, 0.2)",
        borderColor: "rgba(3, 88, 106, 0.80)",
        pointBorderColor: "rgba(3, 88, 106, 0.80)",
        pointBackgroundColor: "rgba(3, 88, 106, 0.80)",
        pointHoverBackgroundColor: "#fff",
        pointHoverBorderColor: "rgba(220,220,220,1)",
        data: [5, 1, 1, 1]
    }]
};
var canvasRadarPhysical = new Chart(ctxRadar1, {
    type: 'radar',
    data: dataRadar1,
});


var ctxRadar2 = document.getElementById("canvasRadarMental").getContext("2d");
var dataRadar2 = {
    labels: ["Sickness", "Tiredness", "Hunger", "Thirst"],
    datasets: [{
        label: "Physical Wellness Variables",
        backgroundColor: "rgba(3, 88, 106, 0.2)",
        borderColor: "rgba(3, 88, 106, 0.80)",
        pointBorderColor: "rgba(3, 88, 106, 0.80)",
        pointBackgroundColor: "rgba(3, 88, 106, 0.80)",
        pointHoverBackgroundColor: "#fff",
        pointHoverBorderColor: "rgba(220,220,220,1)",
        data: [5, 1, 1, 1]
    }]
};
var canvasRadarMental = new Chart(ctxRadar2, {
    type: 'radar',
    data: dataRadar2,
});