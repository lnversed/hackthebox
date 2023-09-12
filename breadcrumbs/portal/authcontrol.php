<?php 
require 'db/db.php';
require "cookie.php";
require "vendor/autoload.php";
use FirebaseJWTJWT;

$errors = array();
$username = "";
$userdata = array();
$valid = false;
$IP = $_SERVER['REMOTE_ADDR'];

//if user clicks on login
if($_SERVER['REQUEST_METHOD'] === "POST"){
    if($_POST['method'] == 0){
        $username = $_POST['username'];
        $password = $_POST['password'];
        
        $query = "SELECT username,position FROM users WHERE username=? LIMIT 1";
        $stmt = $con->prepare($query);
        $stmt->bind_param('s', $username);
        $stmt->execute();
        $result = $stmt->get_result();
        while ($row = $result->fetch_array(MYSQLI_ASSOC)){
            array_push($userdata, $row);
        }
        $userCount = $result->num_rows;
        $stmt->close();

        if($userCount > 0){
            $password = sha1($password);
            $passwordQuery = "SELECT * FROM users WHERE password=? AND username=? LIMIT 1";
            $stmt = $con->prepare($passwordQuery);
            $stmt->bind_param('ss', $password, $username);
            $stmt->execute();
            $result = $stmt->get_result();

            if($result->num_rows > 0){
                $valid = true;
            }
            $stmt->close();
        }

        if($valid){
            session_id(makesession($username));
            session_start();

            $secret_key = '6cb9c1a2786a483ca5e44571dcc5f3bfa298593a6376ad92185c3258acd5591e';
            $data = array();

            $payload = array(
                "data" => array(
                    "username" => $username
            ));

            $jwt = JWT::encode($payload, $secret_key, 'HS256');
            
            setcookie("token", $jwt, time() + (86400 * 30), "/");

            $_SESSION['username'] = $username;
            $_SESSION['loggedIn'] = true;
            if($userdata[0]['position'] == ""){
                $_SESSION['role'] = "Awaiting approval";
            } 
            else{
                $_SESSION['role'] = $userdata[0]['position'];
            }
            
            header("Location: /portal");
        }

        else{
            $_SESSION['loggedIn'] = false;
            $errors['valid'] = "Username or Password incorrect";
        }
    }

    elseif($_POST['method'] == 1){
        $username=$_POST['username'];
        $password=$_POST['password'];
        $passwordConf=$_POST['passwordConf'];
        
        if(empty($username)){
            $errors['username'] = "Username Required";
        }
        if(strlen($username) < 4){
            $errors['username'] = "Username must be at least 4 characters long";
        }
        if(empty($password)){
            $errors['password'] = "Password Required"; 
        }
        if($password !== $passwordConf){
            $errors['passwordConf'] = "Passwords don't match!"; 
        }

        $userQuery = "SELECT * FROM users WHERE username=? LIMIT 1";
        $stmt = $con->prepare($userQuery);
        $stmt ->bind_param('s',$username);
        $stmt->execute();
        $result = $stmt->get_result();
        $userCount = $result->num_rows;
        $stmt->close();

        if($userCount > 0){
            $errors['username'] = "Username already exists";
        }

        if(count($errors) === 0){
            $password = sha1($password);
            $sql = "INSERT INTO users(username, password, age, position) VALUES (?,?, 0, '')";
            $stmt = $con->prepare($sql);
            $stmt ->bind_param('ss', $username, $password);

            if ($stmt->execute()){
                $user_id = $con->insert_id;
                header('Location: login.php');
            }
            else{
                $_SESSION['loggedIn'] = false;
                $errors['db_error']="Database error: failed to register";
            }
        }
    }
}
