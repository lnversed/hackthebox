<?php
	$myip = "10.10.14.11";
	$hostname = "test.dynamicdns.htb";
	list($h,$d) = explode(".",$hostname,2);
	$cmd = sprintf("server 127.0.0.1\nzone %s\nupdate delete %s.%s\nupdate add %s.%s 30 IN A %s\nsend\n",$d,$h,$d,$h,$d,$myip);
	echo $cmd;
	//system('echo "'.$cmd.'" | /usr/bin/nsupdate -t 1 -k /etc/bind/ddns.key',$retval);
?>
