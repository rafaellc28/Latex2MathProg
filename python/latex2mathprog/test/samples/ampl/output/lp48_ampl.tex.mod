set DEST;

param lambda, := 0.85;

set ORIG;

param demand{d in DEST}, >= 0;

param cost{o in ORIG, d in DEST}, >= 0;

param supply{o in ORIG}, >= 0;


var Trans{o in ORIG, d in DEST}, >= 0;


minimize obj: lambda * sum{i in ORIG, j in DEST}cost[i,j] * Trans[i,j] + (1 - lambda) * sum{i in ORIG, j in DEST}cost[i,j] * Trans[i,j];

s.t. C1 {i in ORIG} :
	sum{j in DEST}Trans[i,j], = supply[i];

s.t. C2 {j in DEST} :
	sum{i in ORIG}Trans[i,j], = demand[j];


solve;


data;

set DEST :=;

set ORIG :=;

param demand :=;

param cost :=;

param supply :=;


end;
