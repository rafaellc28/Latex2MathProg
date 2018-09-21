set FOOD;

set MINREQ;

set MAXREQ;

param cost{f in FOOD}, > 0;

set NUTR, := MINREQ union MAXREQ;

param f_min{f in FOOD}, >= 0;

param n_min{i in MINREQ}, >= 0;

param f_max{f in FOOD}, >= f_min[f];

param n_max{i in MAXREQ}, >= n_min[i];

param amt{n in NUTR, f in FOOD}, >= 0;


var Buy{f in FOOD}, <= f_max[f], >= f_min[f];


minimize obj: sum{j in FOOD}cost[j] * Buy[j];

s.t. C1 {i in MINREQ} :
	sum{j in FOOD}amt[i,j] * Buy[j], >= n_min[i];

s.t. C2 {i in MAXREQ} :
	sum{j in FOOD}amt[i,j] * Buy[j], <= n_max[i];


solve;


data;

set FOOD :=;

set MINREQ :=;

set MAXREQ :=;

param cost :=;

param f_min :=;

param n_min :=;

param f_max :=;

param n_max :=;

param amt :=;


end;
