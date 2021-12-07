$FINAL_TURN = 2020;
@starting = (0, 3, 6);
    %said;
    $turn = 1;
    for ( ; $turn <= ($#starting + 1); ++$turn) {
        $num = $starting[$turn - 1];
        #$said{$num} = $turn;
        $said{$num} = defined($said{$num}) ? $turn : -$turn;
print "turn $turn, said $num\n";
    }
 #  at this point, with input 1,3,2, $num == 2

    for ( ; $turn <= 20; ++$turn) {
print "turn $turn, last number said was $num\n";
    if ($said{$num} < 0) {
print "  that's the first time we said it, so saying 0\n";
        $num = 0;
    } else {
print "  we said it before in $said{$num}, so saying $turn - $said{$num} = ", ($turn - $said{$num}), "\n";
        $num = $turn - $said{$num};
    }
    $said{$num} = defined($said{$num}) ? $turn : -$turn;
print "	recorded $num -> $said{$num}\n";
}
