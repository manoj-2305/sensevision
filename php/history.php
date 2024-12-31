<?php
session_start();  // Ensure session starts at the very beginning

include '../database/config.php';

header('Content-Type: application/json'); // Ensure the response is JSON

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['user_id'])) {
        $user_id = $_POST['user_id'];

        if (!$user_id) {
            echo json_encode(["success" => false, "message" => "Missing user_id"]);
            exit;
        }

        // Fetch file history for the logged-in user
        $query = "SELECT file_type, file_name, timestamp FROM uploads WHERE user_id = ?";
        $stmt = $conn->prepare($query);
        $stmt->bind_param("i", $user_id);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            $history = [];
            while ($row = $result->fetch_assoc()) {
                $history[] = $row;
            }
            echo json_encode(["success" => true, "history" => $history]);
        } else {
            echo json_encode(["success" => false, "message" => "No file history found"]);
        }
    } else {
        echo json_encode(["success" => false, "message" => "User is not logged in"]);
    }
} else {
    echo json_encode(["success" => false, "message" => "Invalid request"]);
}
?>
