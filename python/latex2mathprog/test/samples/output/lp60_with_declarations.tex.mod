param n integer, >= 0;

set V, := 1..n;

set E dimen 2, within V cross V, default setof {i in V, j in V : i <> j and Uniform(0, 1) <= 0.15} (i,j);


var x{i in V} binary;

var k{i in V} >= 1, <= card(V);


minimize obj: sum{i in V}x[i];

s.t. C1 {(i,j) in E} :
	k[j] - k[i], >= 1 - card(V) * (x[i] + x[j]);


solve;


data;

param n := 0;

set E :=;


end;
