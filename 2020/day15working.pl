
$FINAL_TURN = 2020;
@starting =  (3, 1, 2);

%said;
$turn = 0;
for ( ; $turn <= $#starting; ++$turn ) {
    $num = $starting[$turn];
    $said{$num} = $turn;
    print "$turn : $num\n";
}

$num = 0;
print "$turn : $num\n";
    for ( ; $turn <= $FINAL_TURN - 2; ++$turn) {
        if ( !defined($said{$num})) {
            $said{$num} = $turn;
            $num = 0;
        } else {
            $diff = $turn - $said{$num};
            $said{$num} = $turn;
            $num = $diff;
       }
        print "$turn : $num\n";
    }

print "num is $num\n";

