<?php
require '../database/config.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'] ?? '';
    $otp = $_POST['otp'] ?? '';
    $new_password = $_POST['new_password'] ?? '';

    // Validate input fields
    if (empty($email) || empty($otp) || empty($new_password)) {
        echo json_encode(["success" => false, "message" => "All fields are required."]);
        exit;
    }

    // Check for valid OTP and expiry time
    $query = "SELECT * FROM users WHERE email = ? AND otp = ? AND otp_expiry > NOW()";
    $stmt = $conn->prepare($query);
    if (!$stmt) {
        echo json_encode(["success" => false, "message" => "Database error: " . $conn->error]);
        exit;
    }
    $stmt->bind_param("si", $email, $otp);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows === 0) {
        echo json_encode(["success" => false, "message" => "Invalid or expired OTP."]);
        exit;
    }

    // Hash the new password
    $hashed_password = password_hash($new_password, PASSWORD_DEFAULT);

    // Update the password and clear OTP fields
    $updateQuery = "UPDATE users SET password = ?, otp = NULL, otp_expiry = NULL WHERE email = ?";
    $updateStmt = $conn->prepare($updateQuery);
    if (!$updateStmt) {
        echo json_encode(["success" => false, "message" => "Database error: " . $conn->error]);
        exit;
    }
    $updateStmt->bind_param("ss", $hashed_password, $email);

    if ($updateStmt->execute()) {
        echo json_encode(["success" => true, "message" => "Password reset successfully."]);
    } else {
        echo json_encode(["success" => false, "message" => "Failed to reset password. Database error: " . $conn->error]);
    }
}
?>
