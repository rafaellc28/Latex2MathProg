set I;

param D{j in 1..10};

param a{i in I : forall{j in 1..10} D[j] > i and 1 = 1}, < 2;





solve;


data;

set I :=;

param D :=;

param a :=;


end;
