<?php
require_once('../inc/sensor.class.php');
$sensor = new Sensor();

$output = array('success' => null, 'message' => null);

switch ($_REQUEST['func']) {
  case 'getReadings':
    $days = !empty($_REQUEST['days']) ? $_REQUEST['days'] : null;
    $output['success'] = true;
    $output['data'] = $sensor->getReadings($days);
    break;
}

echo json_encode($output);
?>
