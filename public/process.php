<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = $_POST['number'];
    $text = $_POST['text'];
    $command = escapeshellcmd("python3 process.py $number \"$text\"");
    $output = shell_exec($command);
    $results = json_decode($output, true);
    echo "<h1>Puzzle Results</h1>";
    echo "<p><strong>Number Puzzle:</strong> " . $results['number_result'] . "</p>";
    echo "<p><strong>Binary Text:</strong> " . $results['binary_text'] . "</p>";
    echo "<p><strong>Vowel Count:</strong> " . $results['vowel_count'] . "</p>";
    echo "<p><strong>Treasure Hunt:</strong> " . $results['treasure_result'] . "</p>";
} else {
    echo "Invalid request.";
}
?>