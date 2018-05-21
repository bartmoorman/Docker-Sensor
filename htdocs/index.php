<?php
require_once('inc/sensor.class.php');
$sensor = new Sensor();
?>
<!DOCTYPE html>
<html lang='en'>
  <head>
    <title>Sensor - Index</title>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>
    <link rel='stylesheet' href='//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'>
    <link rel='stylesheet' href='//bootswatch.com/4/darkly/bootstrap.min.css'>
    <link rel='stylesheet' href='//use.fontawesome.com/releases/v5.0.12/css/all.css' integrity='sha384-G0fIWCsCzJIMAVNQPfjH08cyYaUtMwjJwqiRKxxE/rx96Uroj1BtIQ6MLJuheaO9' crossorigin='anonymous'>
  </head>
  <body>
    <canvas id='chart'></canvas>
    <script src='//code.jquery.com/jquery-3.2.1.min.js' integrity='sha384-xBuQ/xzmlsLoJpyjoggmTEz8OWUFM0/RC5BsqQBDX2v5cMvDHcMakNTNrHIW2I5f' crossorigin='anonymous'></script>
    <script src='//cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js' integrity='sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q' crossorigin='anonymous'></script>
    <script src='//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script>
    <script src='//cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.1/moment.min.js' integrity='sha384-F13mJAeqdsVJS5kJv7MZ4PzYmJ+yXXZkt/gEnamJGTXZFzYgAcVtNg5wBDrRgLg9' crossorigin='anonymous'></script>
    <script src='//cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js' integrity='sha384-0saKbDOWtYAw5aP4czPUm6ByY5JojfQ9Co6wDgkuM7Zn+anp+4Rj92oGK8cbV91S' crossorigin='anonymous'></script>
    <script>
      $(document).ready(function() {
        var config = {
          type: 'line',
          data: {
            datasets: [{
              label: 'Temperature',
              backgroundColor: 'rgba(255, 0, 0, 0.1)',
              borderColor: 'rgba(255, 0, 0)',
              borderWidth: 1,
              fill: false,
              yAxisID: 'temperature'
            }, {
              label: 'Humidity',
              backgroundColor: 'rgba(0, 0, 255, 0.1)',
              borderColor: 'rgba(0, 0, 255)',
              borderWidth: 1,
              fill: false,
              yAxisID: 'humidity'
            }]
          },
          options: {
            title: {display: true, text: 'Temperature & Humidity'},
            legend: {position: 'bottom'},
            scales: {
              xAxes: [{display: true, type: 'time'}],
              yAxes: [{
                display: true,
                id: 'temperature',
                position: 'left',
                scaleLabel: {display: true, labelString: 'Temperature'}
              }, {
                display: true,
                id: 'humidity',
                position: 'right',
                scaleLabel: {display: true, labelString: 'Humidity'},
                gridLines: {display: false}
              }]
            }
          }
        };
        var chart = new Chart($('#chart'), config);

        function updateChart() {
          $.getJSON('src/action.php', {"func": "getReadings"})
            .done(function(data) {
              if (data.success) {
                config.data.datasets[0].data = data.data.temperatureData;
                config.data.datasets[1].data = data.data.humidityData;
              }
            })
            .fail(function(jqxhr, textStatus, errorThrown) {
              console.log(`getReadings failed: ${jqxhr.status} (${jqxhr.statusText}), ${textStatus}, ${errorThrown}`);
            })
            .always(function() {
              chart.update();
            });

          setTimeout(updateChart, 5000);
        };

        updateChart();
      });
    </script>
  </body>
</html>
