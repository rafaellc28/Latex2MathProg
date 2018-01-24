set I;

param for0;

param a{i in I}, := 1 + for0;





solve;


data;

set I :=;

param for0 := 0;


end;
