sub c{foreach ($_[0]=~/1+/g){$b=length($_);$a=$b>$a?$b:$a}}$_=<>;c($_);for $i (0..length($_)-1){if (substr($_, $i, 1)=="0"){substr($_, $i, 1)="1";c($_);substr($_, $i, 1)="0";}}print$a;
