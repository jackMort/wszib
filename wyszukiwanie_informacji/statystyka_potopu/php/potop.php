<?php
   $str = "";
   $fp = fopen( "php://stdin", "r" );
   while( !feof( $fp ) )
   	  $str.= fgets( $fp, 2048 );
   fclose( $fp );

   $words = preg_split( "/[^a-ź]+/", strtolower( $str ) );

   $freq = array_count_values( $words );
   arsort( $freq );
   $i = 0;
   foreach( $freq as $key => $value ) {
	  echo "$key $value\n";
	  if( ++$i == 20 )
	  return;
   }
   // vim: fdm=marker ts=4 sw=4 sts=4
?>
