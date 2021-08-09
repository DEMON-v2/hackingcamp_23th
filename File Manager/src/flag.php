<?php
if(!preg_match("/".$_SERVER['HTTP_HOST']."/i",$_SERVER['HTTP_REFERER'])){
    die("No ^~^");
}