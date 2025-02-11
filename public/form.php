<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puzzle Form</title>
</head>
<body>
    <h1>Solve the Puzzle!</h1>
    <form action="process.php" method="POST">
        <label for="number">Enter a Number (e.g., Birth Year):</label>
        <input type="number" id="number" name="number" required>
        <br><br>
        <label for="text">Enter a Text Message (e.g., Name or Secret Word):</label>
        <input type="text" id="text" name="text" required>
        <br><br>
        <button type="submit">Solve the Puzzle</button>
    </form>
</body>
</html>