set J;

set P{j in J};

param T{j in J};


var x{j in J} >= 0;

var z;


minimize obj: z;

s.t. C1 {j in J, k in P[j]} :
	x[j], >= x[k] + T[k];

s.t. C2 {j in J} :
	z, >= x[j] + T[j];

s.t. C3 {j in J} :
	T[j], >= 0;


solve;


data;

set J :=;

set P[0] :=;

param T :=;


end;
