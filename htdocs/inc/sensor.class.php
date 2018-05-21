<?php
class Sensor {
  private $dbFile = '/config/sensor.db';
  private $dbConn = null;

  public function __construct() {
    session_start();

    if (file_exists($this->dbFile) && is_writable($this->dbFile)) {
      $this->connectDb();
    } elseif (is_writable(dirname($this->dbFile))) {
      $this->connectDb();
      $this->initDb();
    }
  }

  public function connectDb() {
    $this->dbConn = new SQLite3($this->dbFile);
    $this->dbConn->busyTimeout(500);
    $this->dbConn->exec('PRAGMA journal_mode = WAL');
  }

  public function initDb() {
    $query = <<<EOQ
CREATE TABLE IF NOT EXISTS `readings` (
  `reading_id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `date` INTEGER DEFAULT (STRFTIME('%s', 'now')),
  `temperature` NUMERIC,
  `humidity` NUMERIC
);
EOQ;
    return $this->dbConn->exec($query);
  }

  public function getReadings($days = null, $granularity = null) {
    $days = !empty($days) ? $this->dbConn->escapeString($days) : 7;
    switch ($granularity) {
      case 'year':
        $granule = '%Y';
        break;
      case 'month':
        $granule = '%Y-%m';
        break;
      case 'day':
        $granule = '%Y-%m-%d';
        break;
      case 'hour':
        $granule = '%Y-%m-%dT%H';
        break;
      default:
        $granule = '%Y-%m-%dT%H:%M';
    }
    $query = <<<EOQ
SELECT STRFTIME('{$granule}', DATETIME(`date`, 'unixepoch'), 'localtime') AS `date`, ROUND(AVG(`temperature`) * 9 / 5 + 32, 1) AS `temperature`, ROUND(AVG(`humidity`), 1) AS `humidity`
FROM `readings`
WHERE `date` > STRFTIME('%s', DATETIME('now', '-{$days} days'))
GROUP BY STRFTIME('{$granule}', DATETIME(`date`, 'unixepoch'))
ORDER BY `date`
EOQ;
    if ($readings = $this->dbConn->query($query)) {
      $output = array();
      while ($reading = $readings->fetchArray(SQLITE3_ASSOC)) {
        $output['temperatureData'][] = array('x' => $reading['date'], 'y' => $reading['temperature']);
        $output['humidityData'][] = array('x' => $reading['date'], 'y' => $reading['humidity']);
      }
      return $output;
    }
    return false;
  }
}
?>
