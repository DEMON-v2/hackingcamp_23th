<?php

if(!isset($_FILES['upload_file'])){
    die("<script>alert('파일이 선택되지 않았습니다.'); history.go(-1); </script>"); 
}

$file = $_FILES['upload_file'];
$filename = $file['name'];
$ip = $_SERVER['REMOTE_ADDR'];
$encrypt_path = hash('sha256', $ip);

if(preg_match("/htaccess/i", $filename)){
    die("<script>alert('업로드가 제한된 파일입니다.'); history.go(-1); </script>");
}

$ext = end(explode('.', strtolower($filename)));
if($ext != "jpg" && $ext != "jpeg" && $ext != "png" && $ext != "gif"){
    if(mb_strpos(file_get_contents($file['tmp_name']), "<?") !== FALSE){
        die("<script>alert('No Hack!'); history.go(-1); </script>");
    }
}

$create_path = "/var/www/html/uploads/{$encrypt_path}/";
if(!file_exists($create_path)){
    mkdir($create_path, 0777, true);
}

$location = "/var/www/html/uploads/{$encrypt_path}/";

if(move_uploaded_file($file['tmp_name'], $location . $file['name'])){
    echo("<script>alert('Success! Your Upload Directory : uploads/$encrypt_path'); location.href='index.php'; </script>");
}else{
    die("<script>alert('Failed'); history.go(-1); </script>");
}

?>