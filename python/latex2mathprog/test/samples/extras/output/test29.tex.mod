param A;

param B;

set C, := if 1 then A else B;





solve;


data;

param A := 0;

param B := 0;


end;
