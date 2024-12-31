<?php

// Include PHPMailer classes
require '../PHPMailer/src/PHPMailer.php';
require '../PHPMailer/src/SMTP.php';
require '../PHPMailer/src/Exception.php';

// Include database configuration
require '../database/config.php';

// Set the timezone
date_default_timezone_set('Asia/Kolkata'); // Change to your timezone

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'] ?? '';

    if (empty($email)) {
        echo json_encode(["success" => false, "message" => "Email is required."]);
        exit;
    }

    // Query to check if the email exists
    $query = "SELECT * FROM users WHERE email = ?";
    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows === 0) {
        echo json_encode(["success" => false, "message" => "No account found with this email."]);
        exit;
    }

    // Generate OTP and expiry time
    $otp = random_int(100000, 999999);
    $expiry = date('Y-m-d H:i:s', strtotime('+10 minutes'));

    // Update OTP and expiry time in the database
    $updateQuery = "UPDATE users SET otp = ?, otp_expiry = ? WHERE email = ?";
    $updateStmt = $conn->prepare($updateQuery);
    $updateStmt->bind_param("iss", $otp, $expiry, $email);

    if ($updateStmt->execute()) {
        // Set up PHPMailer
        $mail = new PHPMailer\PHPMailer\PHPMailer();
        $mail->isSMTP();
        $mail->Host = 'smtp.gmail.com';
        $mail->SMTPAuth = true;
        $mail->Username = 'manuproject23@gmail.com';
        $mail->Password = 'hhtmgyuwnvibrkdm';
        $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = 587;

        $mail->setFrom('manuproject23@gmail.com', 'SenseVision');
        $mail->addAddress($email);

        $mail->isHTML(true); 
        $mail->Subject = 'Your OTP Code for Secure Access'; 
        $mail->Body = " 
            <div style='font-family: Arial, sans-serif; line-height: 1.6;'>
                <h2 style='color:rgb(0, 208, 255);'>Your OTP Code for Secure Access</h2>
                <p>Dear User,</p>
                <p>We have received a request to verify your account associated with the email address: <b>$email</b>.</p>
                <p><b>Your One-Time Password (OTP) is:</b></p>
                <div style='font-size: 24px; font-weight: bold; color:rgb(0, 208, 255); margin: 20px 0;'>$otp</div>
                <p>This OTP is valid for the next <b>10 minutes</b>. Please use it to complete your verification process.</p>
                <p>If you did not make this request, please ignore this email or contact our support team at <a href='mailto:manuproject23@gmail.com' style='color: rgb(0, 208, 255);'>manuproject23@gmail.com</a>.</p>
                <p style='margin-top: 20px;'>
                    Best regards,<br>
                    <b>SenseVision Application Team</b><br>
                    <i>Ensuring your security, every step of the way.</i>
                </p>
                <hr style='border: none; border-top: 1px solid #ddd; margin: 20px 0;'>
                <p style='font-size: 0.9em; color: #555;'>This email was sent from an automated system. Please do not reply directly. For assistance, contact <a href='mailto:manuproject23@gmail.com' style='color: rgb(0, 208, 255);'>our support team</a>.</p>
            </div>
        ";

        if ($mail->send()) {
            echo json_encode(["success" => true, "message" => "OTP sent to your email."]);
        } else {
            echo json_encode(["success" => false, "message" => "Failed to send OTP. Mailer Error: " . $mail->ErrorInfo]);
        }
    } else {
        echo json_encode(["success" => false, "message" => "Failed to generate OTP. Database error: " . $conn->error]);
    }
}
?>
