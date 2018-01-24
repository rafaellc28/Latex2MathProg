param a;

param c;

param b;

param d;


maximize obj: if a then b;

s.t. C1  : if c then d, <= 1;


solve;


data;

param a := 0;

param c := 0;

param b := 0;

param d := 0;


end;
