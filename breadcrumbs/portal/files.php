"<?php session_start();
$LOGGED_IN = false;
if($_SESSION['username'] !== "paul"){
    header("Location: ../index.php");
}
if(isset($_SESSION['loggedIn'])){
    $LOGGED_IN = true;
    require '../db/db.php';
}
else{
    header("Location: ../auth/login.php");
    die();
}
?>
<html lang="en">
    <head>
        <title>Binary</title>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <link rel="stylesheet" type="text/css" href="../assets/css/main.css">
        <link rel="stylesheet" type="text/css" href="../assets/css/all.css">
    </head>

    <nav class="navbar navbar-default justify-content-end">
        <div class="navbar-header justify-content-end">
            <button type="button" class="navbar-toggle btn btn-outline-info p-3 m-3" data-toggle="collapse" data-target=".navbar-collapse"><i class="fas fa-hamburger"></i></button>
        </div>

        <div class="collapse navbar-collapse justify-content-end mr-5">
             <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link text-right" href="../index.php"><i class="fas fa-home"></i> Home</a></li>
                <li class="nav-item"><a class="nav-link text-right" href="issues.php"><i class="fa fa-check" aria-hidden="true"></i> Issues</a></li>
                <li class="nav-item"><a class="nav-link text-right" href="users.php"><i class="fa fa-user" aria-hidden="true"></i> User Management</a></li>
                <li class="nav-item"><a class="nav-link text-right" href="#"><i class="fa fa-file" aria-hidden="true"></i> File Management</a></li>
                <li class="nav-item"><a class="nav-link text-right" href="../auth/logout.php"><i class="fas fa-sign-out-alt"></i> Logout</a></li>
             </ul>
        </div>
    </nav>
    <body class="bg-dark">
        <main class="main">
            <div class="row justify-content-center text-white text-center">
                <div class="col-md-3">
                    <h1>Task Submission</h1>
                    <p class="text-danger"><i class="fas fa-exclamation-circle"></i> Please upload only .zip files!</p>
                    <form onsubmit="return false">
                        <div class="form-group mt-5">
                            <input type="text" class="form-control" placeholder="Task completed" id="task" name="task">
                        </div>
                        <div class="form-group">
                            <input type="file" class="form-control" placeholder="Task" id="file" name="file">
                        </div>
                        <button type="submit" class="btn btn-outline-success btn-block py-3" id="upload">Upload</button>
                    </form>
                    <p id="message"></p>
                </div>
            </div>
        </div>
        </main>

        <?php include "../includes/footer.php"; ?>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
        <script type="text/javascript" src='../assets/js/files.js'></script>
    </body>


</html>
"
