/*
https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_confirmed_usafacts.csv
import csv to sql server database into table named casesbystate
*/
use data
drop table if exists #cases
select 
	state,
	cast(replace(DateRecorded,' ','/') as date) as DateRecorded,
	cast(confirmed as numeric) as confirmed
into #cases
from cases
unpivot
(
	confirmed 
	for DateRecorded in([1 22 20],[1 23 20],[1 24 20],[1 25 20],[1 26 20],[1 27 20],[1 28 20],[1 29 20],[1 30 20],[1 31 20],[2 1 20],[2 2 20],[2 3 20],[2 4 20],[2 5 20],[2 6 20],[2 7 20],[2 8 20],[2 9 20],[2 10 20]
					   ,[2 11 20],[2 12 20],[2 13 20],[2 14 20],[2 15 20],[2 16 20],[2 17 20],[2 18 20],[2 19 20],[2 20 20],[2 21 20],[2 22 20],[2 23 20],[2 24 20],[2 25 20],[2 26 20],[2 27 20],[2 28 20],[2 29 20],[3 1 20],[3 2 20],[3 3 20],[3 4 20],[3 5 20],[3 6 20],[3 7 20],[3 8 20],[3 9 20],[3 10 20]
					   ,[3 11 20],[3 12 20],[3 13 20],[3 14 20],[3 15 20],[3 16 20],[3 17 20],[3 18 20],[3 19 20],[3 20 20],[3 21 20],[3 22 20],[3 23 20],[3 24 20],[3 25 20],[3 26 20],[3 27 20],[3 28 20],[3 29 20],[3 30 20],[3 31 20],[4 1 20],[4 2 20],[4 3 20],[4 4 20],[4 5 20],[4 6 20],[4 7 20],[4 8 20],[4 9 20],[4 10 20]
					   ,[4 11 20],[4 12 20],[4 13 20],[4 14 20],[4 15 20],[4 16 20],[4 17 20],[4 18 20],[4 19 20],[4 20 20],[4 21 20],[4 22 20],[4 23 20],[4 24 20],[4 25 20],[4 26 20],[4 27 20],[4 28 20],[4 29 20],
					   [4 30 20],[5 1 20],[5 2 20],[5 3 20],[5 4 20],[5 5 20],[5 6 20],[5 7 20],[5 8 20],[5 9 20],[5 10 20],[5 11 20],[5 12 20],[5 13 20],[5 14 20],[5 15 20],[5 16 20],[5 17 20],[5 18 20],[5 19 20])
) as unpivottable


;with t1 as (
	select 
		state,
		DateRecorded,
		sum(confirmed) as confirmed--select *
	from #cases
	group by DateRecorded,State
	--order by state,cast(replace(datestamp,' ','/') as date)
),t2 as (
	select 
		*,
		Confirmed-lag(Confirmed,1,0) over (partition by state order by DateRecorded) as NewConfirmed
	from t1
), t3 as (
	select
		*,
		cast((
		lag(NewConfirmed,0,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,1,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,2,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,3,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,4,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,5,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,6,0) over(partition by state order by DateRecorded)
		)/5 as decimal)as SevenDayNewconfirmedAvg
	from t2
), t4 as (
	select
		*,
		SevenDayNewconfirmedAvg/
		iif(lag(SevenDayNewconfirmedAvg,1,SevenDayNewconfirmedAvg) over(partition by state order by DateRecorded)=0,1,lag(SevenDayNewconfirmedAvg,1,SevenDayNewconfirmedAvg) over(partition by state order by DateRecorded)) as SevendayPercentChangeInNewConfirmedAvg
	from t3
)
select
	*,
	cast(SevenDayNewconfirmedAvg*SevendayPercentChangeInNewConfirmedAvg as numeric) as'EstNextDayNewConfirmed'
from t4
where 1=1
--and state='ca'
and DateRecorded=(select max(daterecorded) from #cases)
--order by DateRecorded
order by SevendayPercentChangeInNewConfirmedAvg desc

;with t1 as (
	select 
		state,
		DateRecorded,
		sum(confirmed) as confirmed--select *
	from #cases
	group by DateRecorded,State
	--order by state,cast(replace(datestamp,' ','/') as date)
),t2 as (
	select 
		*,
		Confirmed-lag(Confirmed,1,0) over (partition by state order by DateRecorded) as NewConfirmed
	from t1
), t3 as (
	select
		*,
		cast((
		lag(NewConfirmed,0,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,1,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,2,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,3,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,4,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,5,0) over(partition by state order by DateRecorded)+
		lag(NewConfirmed,6,0) over(partition by state order by DateRecorded)
		)/5 as decimal)as SevenDayNewconfirmedAvg
	from t2
), t4 as (
	select
		*,
		SevenDayNewconfirmedAvg/
		iif(lag(SevenDayNewconfirmedAvg,1,SevenDayNewconfirmedAvg) over(partition by state order by DateRecorded)=0,1,lag(SevenDayNewconfirmedAvg,1,SevenDayNewconfirmedAvg) over(partition by state order by DateRecorded)) as SevendayPercentChangeInNewConfirmedAvg
	from t3
)
select
	*,
	cast(SevenDayNewconfirmedAvg*SevendayPercentChangeInNewConfirmedAvg as numeric) as'EstNextDayNewConfirmed'
from t4
where 1=1
and state='nc'
--and DateRecorded=(select max(daterecorded) from #cases)
order by DateRecorded
--order by SevendayPercentChangeInNewConfirmedAvg desc
