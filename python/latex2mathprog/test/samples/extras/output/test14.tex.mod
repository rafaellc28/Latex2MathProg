param a;

param c;

param b;

param e;

param d;


s.t. C1  : if a then b + c - 1 / 2 * d / e less 9 else 1, <= 5;


solve;


data;

param a := 0;

param c := 0;

param b := 0;

param e := 0;

param d := 0;


end;
