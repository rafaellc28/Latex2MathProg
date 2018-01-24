set I;

param D{j in 1..10};

param a{i in I : 1 = 1 and forall{j in 1..10} D[j] > i}, < 2;





solve;


data;

set I :=;

param D :=;

param a :=;


end;
