#!/usr/bin/perl

while (<>) {
    while ( /([a-źA-Ź]+)/g ) {
        $WORDS{lc $1}++;
    }
}

foreach my $word ( sort { $WORDS{$b} <=> $WORDS{$a} } keys %WORDS) {
    printf "%s %d\n", $word, $WORDS{$word};
	if( ++$i == 20 ) {
		exit;
	}
}
# vim: fdm=marker ts=4 sw=4 sts=4
