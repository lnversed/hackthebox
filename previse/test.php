<?php

$enc = base64_decode("JDEk8J+ngmxsb2wkNTBQVC5YdzdSamN1bEtUY2RuTUtWLw==");
echo "Encypted hash: " . $enc . PHP_EOL;
$testhash = crypt("burner", '$1$🧂llol$');
echo "testhash: " . $testhash . PHP_EOL;

$filehandle = fopen("/tmp/matri/testlist", "r");
if ($filehandle) {
	while (($line = fgets($filehandle)) !== false) {
		$hash = crypt(str_replace("\n", "", $line), '$1$🧂llol$');
		echo $hash;
		echo ": $line" . PHP_EOL;
		if ($hash === $enc) {
			echo "Password cracked: " . $line . PHP_EOL;
			break;
		}
		
	}
}


fclose($filehandle);
