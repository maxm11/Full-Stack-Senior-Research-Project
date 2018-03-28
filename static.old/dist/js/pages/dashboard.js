/*
 * Author: Abdullah A Almsaeed
 * Date: 4 Jan 2014
 * Description:
 *      This is a demo file used only for the main dashboard (index.html)
 **/

$(function () {

  'use strict';

  // Make the dashboard widgets sortable Using jquery UI
  $('.connectedSortable').sortable({
    placeholder         : 'sort-highlight',
    connectWith         : '.connectedSortable',
    handle              : '.box-header, .nav-tabs',
    forcePlaceholderSize: true,
    zIndex              : 999999
  });
  $('.connectedSortable .box-header, .connectedSortable .nav-tabs-custom').css('cursor', 'move');

  // jQuery UI sortable for the todo list
  $('.todo-list').sortable({
    placeholder         : 'sort-highlight',
    handle              : '.handle',
    forcePlaceholderSize: true,
    zIndex              : 999999
  });

  // bootstrap WYSIHTML5 - text editor
  $('.textarea').wysihtml5();

  $('.daterange').daterangepicker({
    ranges   : {
      'Today'       : [moment(), moment()],
      'Yesterday'   : [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
      'Last 7 Days' : [moment().subtract(6, 'days'), moment()],
      'Last 30 Days': [moment().subtract(29, 'days'), moment()],
      'This Month'  : [moment().startOf('month'), moment().endOf('month')],
      'Last Month'  : [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
    },
    startDate: moment().subtract(29, 'days'),
    endDate  : moment()
  }, function (start, end) {
    window.alert('You chose: ' + start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
  });

  /* jQueryKnob */
  $('.knob').knob();

  // jvectormap data
  var visitorsData = {
    US: 398, // USA
    SA: 400, // Saudi Arabia
    CA: 1000, // Canada
    DE: 500, // Germany
    FR: 760, // France
    CN: 300, // China
    AU: 700, // Australia
    BR: 600, // Brazil
    IN: 800, // India
    GB: 320, // Great Britain
    RU: 3000 // Russia
  };

  // Sparkline charts
  var myvalues = [1000, 1200, 920, 927, 931, 1027, 819, 930, 1021];
  $('#sparkline-1').sparkline(myvalues, {
    type     : 'line',
    lineColor: '#92c1dc',
    fillColor: '#ebf4f9',
    height   : '50',
    width    : '80'
  });
  myvalues = [515, 519, 520, 522, 652, 810, 370, 627, 319, 630, 921];
  $('#sparkline-2').sparkline(myvalues, {
    type     : 'line',
    lineColor: '#92c1dc',
    fillColor: '#ebf4f9',
    height   : '50',
    width    : '80'
  });
  myvalues = [15, 19, 20, 22, 33, 27, 31, 27, 19, 30, 21];
  $('#sparkline-3').sparkline(myvalues, {
    type     : 'line',
    lineColor: '#92c1dc',
    fillColor: '#ebf4f9',
    height   : '50',
    width    : '80'
  });

// JavaScript Document
/* ChartJS
     * -------
     * Here we will create a few charts using ChartJS
     */

  // The Calender
  $('#calendar').datepicker();

  // SLIMSCROLL FOR CHAT WIDGET
  $('#chat-box').slimScroll({
    height: '250px'
  });

  // Fix for charts under tabs
  $('.box ul.nav a').on('shown.bs.tab', function () {
    area.redraw();
    donut.redraw();
    line.redraw();
  });

  /* The todo list plugin */
  $('.todo-list').todoList({
    onCheck  : function () {
      window.console.log($(this), 'The element has been checked');
    },
    onUnCheck: function () {
      window.console.log($(this), 'The element has been unchecked');
    }
  });

});
// ChartJS
// Radar Chart
  var radarChartCanvas = document.getElementById("radarChart1");
    // This will get the first returned node in the jQuery collection.
	var radarChartData = {
      labels  : ['Angry-Disgusted', 'Fearful', 'Happy', 'Sad', 'Surprised'],
      datasets: [
        {
          label               : 'Entity',
          backgroundColor     : 'rgba(0, 214, 222, 0.3)',
          borderColor         : 'rgba(0, 214, 222, 1)',
          pointBackgroundColor : 'rgba(0, 214, 222, 1)',
          pointBorderColor    : '#c1c7d1',
          pointHoverBackgroundColor  : '#fff',
          pointHoverBorderColor : 'rgba(220,220,220,1)',
          data                : [65, 59, 80, 81, 56]
        } 
      ]
    };
	var radarChartOptions = {
      //Boolean - If we should show the scale at all
      showScale               : false,
      //Boolean - Whether grid lines are shown across the chart
      scaleShowGridLines      : false,
      //String - Colour of the grid lines
      scaleGridLineColor      : 'rgba(0,0,0,.05)',
      //Number - Width of the grid lines
      scaleGridLineWidth      : 1,
      //Boolean - Whether to show horizontal lines (except X axis)
      scaleShowHorizontalLines: true,
      //Boolean - Whether to show vertical lines (except Y axis)
      scaleShowVerticalLines  : true,
      //Boolean - Whether the line is curved between points
      bezierCurve             : true,
      //Number - Tension of the bezier curve between points
      bezierCurveTension      : 0.3,
      //Boolean - Whether to show a dot for each point
      pointDot                : false,
      //Number - Radius of each point dot in pixels
      pointDotRadius          : 4,
      //Number - Pixel width of point dot stroke
      pointDotStrokeWidth     : 1,
      //Number - amount extra to add to the radius to cater for hit detection outside the drawn point
      pointHitDetectionRadius : 20,
      //Boolean - Whether to show a stroke for datasets
      datasetStroke           : true,
      //Number - Pixel width of dataset stroke
      datasetStrokeWidth      : 2,
      //Boolean - Whether to fill the dataset with a color
      datasetFill             : true,
      //String - A legend template
      legendTemplate          : '<ul class="<%=name.toLowerCase()%>-legend"><% for (var i=0; i<datasets.length; i++){%><li><span style="background-color:<%=datasets[i].lineColor%>"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>',
      //Boolean - whether to maintain the starting aspect ratio or not when responsive, if set to false, will take up entire container
      maintainAspectRatio     : true,
      //Boolean - whether to make the chart responsive to window resizing
      responsive              : true
    };

// Training Data Line Chart
var trainLineChartCanvas = document.getElementById("trainChart1");
var trainLineChartData = {
  labels: ["10:11AM", "10:12AM", "10:13AM", "10:14AM", "10:15AM", "10:16AM"],
  datasets: [{
    label: "Training",
    data: [30,31,34,40,44,47],
    backgroundColor     : 'rgba(32, 158, 1, 0.5)',
    borderColor         : 'rgba(32, 158, 1, 1)',
    pointBackgroundColor : 'rgba(32, 158, 1, 1)',
    pointBorderColor    : '#c1c7d1',
    pointHoverBackgroundColor  : '#fff',
    pointHoverBorderColor : 'rgba(220,220,220,1)'
  },
  {
    label: "Testing",
    data: [55,57,61,67,70,77],
    backgroundColor     : 'rgba(135, 217, 255, 0.5)',
    borderColor         : 'rgba(135, 217, 255, 1)',
    pointBackgroundColor : 'rgba(135, 217, 255, 1)',
    pointBorderColor    : '#c1c7d1',
    pointHoverBackgroundColor  : '#fff',
    pointHoverBorderColor : 'rgba(220,220,220,1)'
  }]
};
var trainLineChartOptions = {
  scales: {
    yAxes: [{
      ticks:{
        beginAtZero : "True",
        max : 100
      }
    }]
  }
};
window.onload = function(){
  window.trainChart1 = new Chart(trainLineChartCanvas, {type:"line", data:trainLineChartData, options:trainLineChartOptions});
  window.radarChart1 = new Chart(radarChartCanvas, {type:"radar", data:radarChartData, options:radarChartOptions});
};