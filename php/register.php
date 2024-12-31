<?php
// register.php
include '../database/config.php'; // Include database connection
require '../PHPMailer/src/PHPMailer.php';
require '../PHPMailer/src/SMTP.php';
require '../PHPMailer/src/Exception.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Sanitize input
    $name = trim($_POST['name']);
    $phone = trim($_POST['phone']);
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    $password = $_POST['password'];

    // Validate input
    if (empty($name) || empty($phone) || empty($email) || empty($password)) {
        echo json_encode(["success" => false, "message" => "All fields are required"]);
        exit;
    }

    // Encrypt the password
    $password = password_hash($password, PASSWORD_DEFAULT); // Secure password hash

    // Check if user already exists
    $checkQuery = "SELECT * FROM users WHERE email = ?";
    $stmt = $conn->prepare($checkQuery);
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
        echo json_encode(["success" => false, "message" => "User already exists"]);
    } else {
        // Insert new user
        $insertQuery = "INSERT INTO users (name, phone, email, password) VALUES (?, ?, ?, ?)";
        $stmt = $conn->prepare($insertQuery);
        $stmt->bind_param("ssss", $name, $phone, $email, $password);
        if ($stmt->execute()) {
            // Send email to the user
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
            $mail->Subject = 'Welcome to SenseVision - Registration Successful';
            $mail->Body = "
                <div style='font-family: Arial, sans-serif; line-height: 1.6;'>
                    <h2 style='color:rgb(0, 208, 255);'>Welcome to SenseVision, $name!</h2>
                    <p>Thank you for registering with us. We are thrilled to have you on board and look forward to helping you leverage our platform to achieve your goals.</p>
                    <p><b>Here are your registration details:</b></p>
                    <ul style='list-style-type: none; padding: 0;'>
                        <li><b>Name:</b> $name</li>
                        <li><b>Email:</b> $email</li>
                    </ul>
                    <p>If you have any questions, concerns, or need assistance, please don't hesitate to <a href='mailto:manuproject23@gmail.com' style='color: rgb(0, 208, 255);'>contact our support team</a>.</p>
                    <p style='margin-top: 20px;'>
                        Best regards,<br>
                        <b>SenseVision Application Team</b><br>
                        <i>Your partner in real-time solutions.</i>
                    </p>
                </div>
            ";

            if ($mail->send()) {
                echo json_encode(["success" => true, "message" => "Registration successful and confirmation email sent!"]);
            } else {
                echo json_encode(["success" => true, "message" => "Registration successful, but email could not be sent. Error: " . $mail->ErrorInfo]);
            }
        } else {
            echo json_encode(["success" => false, "message" => "Registration failed, please try again"]);
        }
    }
}
?>
