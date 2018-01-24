set I;

param for_;

param a{i in I}, := 1 - for_;





solve;


data;

set I :=;

param for_ := 0;


end;
