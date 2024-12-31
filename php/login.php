<?php
// login.php
include '../database/config.php'; // Include database connection

session_start(); // Start the session to store session variables

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $_POST['email'];
    $password = $_POST['password']; // No need to hash the password here

    // Check if user exists
    $query = "SELECT * FROM users WHERE email = ?";
    $stmt = $conn->prepare($query);
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        // Verify the password
        if (password_verify($password, $user['password'])) {
            // Store user ID in session after successful login
            $_SESSION['user_id'] = $user['user_id'];

            // Include user_id in the response
            echo json_encode([
                "success" => true,
                "user" => $user,
                "user_id" => $user['user_id'] // Return the user_id
            ]);
        } else {
            echo json_encode(["success" => false, "message" => "Invalid email or password"]);
        }
    } else {
        echo json_encode(["success" => false, "message" => "Invalid email or password"]);
    }
}
?>
