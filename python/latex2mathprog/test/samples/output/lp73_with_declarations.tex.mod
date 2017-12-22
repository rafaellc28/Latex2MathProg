param year integer, <= 3999, >= 0001, := 2010;

param daysinmonth{m in 1..12} integer, <= 31, >= 28, := (str2time(year + (if m < 12 then 0 else 1) & "-" & (if m < 12 then m + 1 else 1) & "-01", "%Y-%m-%d") - str2time(year & "-" & m & "-01", "%Y-%m-%d")) / 86400;

param firstday{m in 1..12} integer, <= 6, >= 0, := time2str(str2time(year & "-" & m & "-01", "%Y-%m-%d"),"%w");

param foo{m in 1..12, k in 0..5, d in 0..6} integer, := 7 * k + d + 1 - firstday[m];

param cal{m in 1..12, k in 0..5, d in 0..6} integer, := if 1 <= foo[m,k,d] and foo[m,k,d] <= daysinmonth[m] then foo[m,k,d] else 0;





solve;


end;
