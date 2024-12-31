<?php
require '../database/config.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'] ?? '';
    $otp = $_POST['otp'] ?? '';

    // Validate input fields
    if (empty($email) || empty($otp)) {
        echo json_encode(["success" => false, "message" => "Email and OTP are required."]);
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

    // If OTP is valid, redirect to reset_password.php
    echo json_encode(["success" => true, "message" => "OTP verified successfully.", "redirect" => "reset_password.php?email=" . urlencode($email)]);
    exit;
}
?>