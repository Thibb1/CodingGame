$n=<>;$q=<>;%d;
for (0..$n-1) {
    chomp($t=<>);
    ($d,$mt)=split(/ /,$t);
    $d=~s/([A-Z])(.*)/\L$1$2/g;
    $d{$d}=$mt;
}
for my $i (0..$q-1) {
    chomp($l=<>);
    $l=~s/([A-Z])(.*)/\L$1$2/g;
    $l=~s/(.*)\.(\w+$)|.*/$2/g;
    print length $l && defined $d{$l}?"$d{$l}\n":"UNKNOWN\n";
}
