set PROD;

set STAGE;

param profit{p in PROD};

param avail_mean{s in STAGE}, > 0;

param rate{p in PROD, s in STAGE}, > 0;

param market{p in PROD}, >= 0;

param commit{p in PROD}, >= 0;

param avail_variance{s in STAGE}, < avail_mean[s]/2, > 0;

param avail{s in STAGE}, := max(Normal(avail_mean[s], avail_variance[s]),0);


var Make{p in PROD}, <= market[p], >= commit[p];


maximize obj: sum{p in PROD}profit[p] * Make[p];

s.t. C1 {s in STAGE} :
	sum{p in PROD}(1/rate[p,s]) * Make[p], <= avail[s];


solve;


data;

set PROD :=;

set STAGE :=;

param profit :=;

param avail_mean :=;

param rate :=;

param market :=;

param commit :=;

param avail_variance :=;


end;
