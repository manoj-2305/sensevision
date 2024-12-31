<?php
// Include database configuration
include '../database/config.php';

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    session_start();

    // Debugging: Print incoming data
    error_log("Incoming POST: " . print_r($_POST, true));
    error_log("Incoming FILES: " . print_r($_FILES, true));

    // Extract user_id from POST or session
    $user_id = $_POST['user_id'] ?? $_SESSION['user_id'] ?? null;
    $file_type = $_POST['file_type'] ?? null;

    if (!$user_id || !$file_type) {
        echo json_encode(["success" => false, "message" => "Missing user_id or file_type"]);
        exit;
    }

    // File handling
    $target_dir = "../uploads/";
    if (!is_dir($target_dir)) {
        mkdir($target_dir, 0777, true);
    }

    $file_name = basename($_FILES["file"]["name"]);
    $target_file = $target_dir . $file_name;

    if ($_FILES["file"]["error"] === UPLOAD_ERR_OK && move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
        // Insert into uploads table
        $insert_query = "INSERT INTO uploads (user_id, file_type, file_name, file_path, timestamp) VALUES (?, ?, ?, ?, NOW())";
        $stmt = $conn->prepare($insert_query);
        $stmt->bind_param("isss", $user_id, $file_type, $file_name, $target_file);

        if ($stmt->execute()) {
            echo json_encode(["success" => true, "message" => "File uploaded and database updated"]);
        } else {
            error_log("Database insertion error: " . $stmt->error);
            echo json_encode(["success" => false, "message" => "Database insertion failed"]);
        }
    } else {
        echo json_encode(["success" => false, "message" => "File upload failed"]);
    }
}
?>
