<?php
include "err_domains.php";
$num = count($domains);  
echo $num."\n";
for($i=0;$i<$num;$i++){  
	$domain = $domains[$i];
	echo $domain."\n"; 	
	$g = stream_context_create(array("ssl" => array("capture_peer_cert_chain" => true))); 
	$r = stream_socket_client("ssl://$domain:443", $errno, $errstr, 10, STREAM_CLIENT_CONNECT, $g);
	$cont = stream_context_get_params($r);
	
	foreach ($cont["options"]["ssl"]["peer_certificate_chain"] as $value) {

		//使用openssl扩展解析证书，这里使用x509证书验证函数
		$cerInfo = openssl_x509_parse($value);
   		// echo var_dump($cerInfo);
   		echo date("Y-m-d",$cerInfo['validFrom_time_t']),"\n";
   		echo date("Y-m-d",$cerInfo['validTo_time_t']),"\n"; 

   		if(strpos($cerInfo['name'],$domain)) {
	   		echo  "start:".date("Y-m-d",$cerInfo['validFrom_time_t'])."<br/>";
	   		echo "end:".date("Y-m-d",$cerInfo['validTo_time_t']);
	   		}   

	}	
	
} 



die();






$domain = "sun.tw22.net";

$g = stream_context_create(array("ssl" => array("capture_peer_cert_chain" => true))); 

$r = stream_socket_client("ssl://$domain:443", $errno, $errstr, 30, STREAM_CLIENT_CONNECT, $g);

$cont = stream_context_get_params($r);

foreach ($cont["options"]["ssl"]["peer_certificate_chain"] as $value) {

	//使用openssl扩展解析证书，这里使用x509证书验证函数

	$cerInfo = openssl_x509_parse($value);

   // echo '<pre>';

   // print_r($cerInfo);
   // echo var_dump($cerInfo);
   echo date("Y-m-d",$cerInfo['validFrom_time_t']),"\n";
   echo date("Y-m-d",$cerInfo['validTo_time_t']),"\n"; 

   if(strpos($cerInfo['name'],$domain)) {

	   echo  "start:".date("Y-m-d",$cerInfo['validFrom_time_t'])."<br/>";

	   echo "end:".date("Y-m-d",$cerInfo['validTo_time_t']);

   }   

}
