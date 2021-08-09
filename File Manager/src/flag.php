<?php
if(!preg_match("/".$_SERVER['HTTP_HOST']."/i",$_SERVER['HTTP_REFERER'])){
    die("No ^~^");
}else{
    $flag = "HCAMP{this_3s_file_manager_exploit!!}";
    die($flag);
}