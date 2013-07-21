<!DOCTYPE html>
<html>
  <?php
     if(!isset($_POST["pass"])) {
       echo "<body><center><form action='index.php' method='POST'><p>Password: </p><input type='password' name='pass' style='width:100px;'></input><br/><input type='submit' value='Submit'></input></form></center></body>";
     }
     else {
       if($_POST["pass"] == "demobot") {
         echo "<head>
    <script src='jquery-2.0.3.min.js'></script>
    <script src='index.js'></script>
  </head>
  <body>
    <div id='d'></div>
    <canvas id='can' width='50px' height='50px' style='width: 50; height: 50; position: absolute; top: 50%; left: 50%; margin-left: -25px; margin-top: -25px;'></canvas>
  </body>";
       }
       else {
         echo "<body><center><p>Incorrect.</p><form action='index.php' method='POST'><p>Password: </p><input type='password' name='pass' style='width:100px;'></input><br/><input type='submit' value='Submit'></input></form></center></body>";
       }
     }
  ?>
</html>
