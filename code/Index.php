<!DOCTYPE html>
<html>
<title>EL FINAL</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body,h1 {font-family: "Raleway", Arial, sans-serif}
h1 {letter-spacing: 6px}
.w3-row-padding img {margin-bottom: 12px}
</style>
<body>

<!-- !PAGE CONTENT! -->
<div class="w3-content" style="max-width:1500px">

<!-- Header -->
<header class="w3-panel w3-center w3-opacity" style="padding:128px 16px">
  <h1 class="w3-xlarge">EMBEDDED LINUX</h1>
  <h1>John Doe</h1>
  

    </div>
  </div>
</header>

<!-- Photo Grid -->
<div class="w3-row-padding w3-grayscale" style="margin-bottom:128px">

<?php
$servername = "localhost";
$username = "root";
$password = "root";

// Create connection
$conn = mysqli_connect($servername, $username, $password);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Create database
//$sql = "CREATE DATABASE myDB";
//if (mysqli_query($conn, $sql)) {
 //   echo "Database created successfully";
//} else {
  //  echo "Error creating database: " . mysqli_error($conn);
//}

mysqli_close($conn);
?>

  
<!-- End Page Content -->
</div>

<!-- Footer -->
<footer class="w3-container w3-padding-64 w3-light-grey w3-center w3-large">  
  <p>Created by John, Steven, David &copy 2017</a></p>
</footer>


