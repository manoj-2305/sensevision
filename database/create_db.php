<?php
// Database connection parameters
$host = "localhost";
$username = "root";
$password = "";
$database = "object_detection";

try {
    // Connect to MySQL
    $conn = new mysqli($host, $username, $password);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Create database if not exists
    $sql = "CREATE DATABASE IF NOT EXISTS $database";
    if ($conn->query($sql) === TRUE) {
        echo "Database created successfully<br>";
    } else {
        echo "Error creating database: " . $conn->error;
    }

    // Select the database
    $conn->select_db($database);

    // Create `users` table with history-related fields
    $sql = "CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(15) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        reset_token VARCHAR(255) NULL,
        token_expiry DATETIME NULL;
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    $sql ="CREATE TABLE IF NOT EXISTS uploads (
        upload_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        file_type VARCHAR(225), -- File type
        file_name VARCHAR(255), -- File name
        file_path VARCHAR(255), -- File path
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, -- Time of upload
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
    )";
    

    if ($conn->query($sql) === TRUE) {
        echo "Table `users` created successfully with history fields<br>";
    } else {
        echo "Error creating table `users`: " . $conn->error;
    }

    // Close connection
    $conn->close();
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
