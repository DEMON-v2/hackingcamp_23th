create user wwwweb identified by 'wwwweb!@#';
grant select on *.* to wwwweb@'%';
flush privileges;