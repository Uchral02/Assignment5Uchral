<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $number = $_POST['number'];
    $text = $_POST['text'];

    // Call the Python script with the form data
    $command = escapeshellcmd("python3 process.py $number \"$text\"");
    $output = shell_exec($command);

    // Display the results
    echo "<h1>Puzzle Results</h1>";
    echo "<pre>$output</pre>";
} else {
    echo "Invalid request.";
}
?>