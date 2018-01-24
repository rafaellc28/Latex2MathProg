set I;

param t{i in I};

param a{i in I : not t[i]}, := 1;





solve;


data;

set I :=;

param t :=;


end;
