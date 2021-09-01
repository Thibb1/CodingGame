$|=1;while(){
    for $i(0..7){
        chomp($t=<>);
        $h{$t}=$i;
    }
    $k=(sort{$b<=>$a}keys%h)[0];
    print"$h{$k}\n";
    delete$h{$k};
}
