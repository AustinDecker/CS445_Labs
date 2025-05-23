<?php
// Function to create a sql connection.
function getDB() {
  $dbhost="10.9.0.6";
  $dbuser="seed";
  $dbpass="dees";
  $dbname="sqllab_users";

  // Create a DB connection
  $conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error . "\n");
  }
  return $conn;
}

$input_uname = $_GET['username'];
$input_pwd = $_GET['Password'];
$hashed_pwd = sha1($input_pwd);

// create a connection
$conn = getDB();
$stmt = $conn->prepare("SELECT id, name, eid, salary, ssn 
                        FROM credential 
                        WHERE name = ? AND Password = ?");

// Bind parameters
$stmt->bind_param("ss", $input_uname, $hashed_pwd);

// Execute the query
$stmt->execute();

// Get the result
$result = $stmt->get_result();

if ($result->num_rows > 0) {
    // Only take the first row 
    $firstrow = $result->fetch_assoc();
    $id     = $firstrow["id"];
    $name   = $firstrow["name"];
    $eid    = $firstrow["eid"];
    $salary = $firstrow["salary"];
    $ssn    = $firstrow["ssn"];
}

// Close the statement
$stmt->close();

// close the sql connection
$conn->close();
?>
