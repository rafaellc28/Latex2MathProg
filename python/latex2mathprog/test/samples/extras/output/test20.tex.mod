set DEST;

param maxserve;

set ORIG;


var Use{i in ORIG, j in DEST} binary;


s.t. C1 {i in ORIG} :
	sum{j in DEST}Use[i,j], <= maxserve;


solve;


data;

set DEST :=;

param maxserve := 0;

set ORIG :=;


end;
