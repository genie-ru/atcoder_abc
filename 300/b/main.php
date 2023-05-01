<?php
$stdin = fopen('php://stdin', 'r');
$line = fgets($stdin);
list($H, $W) = explode(' ', trim($line));
$A = array();
$B = array();
for ($i = 0; $i < $H; $i++) {
  $A[] = trim(fgets($stdin));
}
for ($i = 0; $i < $H; $i++) {
  $B[] = trim(fgets($stdin));
}
$match = false;
for ($s = 0; $s < $H && !$match; $s++) {
  for ($t = 0; $t < $W && !$match; $t++) {
    $ok = true;
    for ($i = 0; $i < $H && $ok; $i++) {
      for ($j = 0; $j < $W && $ok; $j++) {
        if ($A[($i - $s + $H) % $H][($j - $t + $W) % $W] !== $B[$i][$j]) {
          $ok = false;
        }
      }
    }
    if ($ok) {
      echo "Yes\n";
      $match = true;
    }
  }
}
if (!$match) {
  echo "No\n";
}
fclose($stdin);
?>
