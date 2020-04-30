--Original takes 3-4 hours
select 
	orders.id,
	batch_id,
	timestamp, 
	aufnr, 
	qmnum, 
	first_teco, 
	last_change, 
	stort, 
	iwerk, 
	ingpr, 
	gewrk	
from (
		select 
			-1 as id,
			t.objectid ordernum1,
			ltrim(orderc.ordernum,'0') ordernumber,
			first_teco,
			max(udate+utime) last_change
		 from (
			 	select * from (select -1 as id, substring(objectid, 3) ordernum, objectid , min(udate+utime) first_teco from data.change_docs
				where fname='TECO'and objectclas != 'OVG'
				group by objectid, id) FirstT
				inner join	(
								select -1 as id, objnr, qmnum, aedat from data.orders 
								where auart= 'MR01' 
								and (sttxt like '%TECO%' or sttxt like '%CLSD%')
								and sttxt not like '%DLFL%' 
								and aedat between (date_trunc('month', current_date) - '1 mon'::interval month) and (date_trunc('month', current_date)-'1 day'::interval day)
							) o on FirstT.objectid=o.objnr
			  ) t 
		inner join (
						select * , substring(objectid, 6) ordernum 
						from data.change_docs 
						where objectclas='ORDER' and fname in ('TPLNR', 'EQUNR') and udate between (date_trunc('month', current_date) - '1 mon'::interval month) and (date_trunc('month', current_date)-'1 day'::interval day)
				   ) orderc on t.ordernum=orderc.ordernum 
		where (udate+utime) > first_teco 		
		group by ordernum1, ordernumber, first_teco
		-----	
		union all
		-----		
		select 
			-1 as id, 
			qmnum, 
			ltrim(ordernum, '0') ordernumber, 
			first_teco, 
			max(udate+utime) last_change 
		from (	
				select 
					-1 as id, 
					ordernum, 
					tec.first_teco, 
					objnr, 
					qmnum, 
					aedat 
				from (
						select * 
						from (
								select 
									-1 as id, 
									substring(objectid, 3) ordernum, 
									objectid , 
									min(udate+utime) 
									first_teco 
								from data.change_docs
								where fname='TECO'and objectclas != 'OVG'
								group by objectid, id
							 ) FirstT
						inner join (
										select -1 as id, objnr, qmnum, aedat from data.orders 
										where auart= 'MR01' 
										and (sttxt like '%TECO%' or sttxt like '%CLSD%') 
										and sttxt not like '%DLFL%'
										and aedat between (date_trunc('month', current_date) - '1 mon'::interval month) and (date_trunc('month', current_date)-'1 day'::interval day)--in last 1 month
									) o on FirstT.objectid=o.objnr 	 
					 ) tec		
				left join (
							select 
								-1 as id, 
								orderc.ordern ordernum1, 
								t.objectid ordernumber, 
								first_teco 
							from (
									select 
										* 
									from (
											select 
												-1 as "id", 
												substring(objectid, 3) as "ordernum", 
												objectid , 
												udate+utime as "first_teco"
											from data.change_docs
											where fname='TECO'
											and objectclas != 'OVG'
										 ) FirstT
									inner join (
													select 
														-1 as "id", 
														objnr, 
														qmnum, 
														aedat 
													from data.orders 
													where auart= 'MR01'
													and (sttxt like '%TECO%' or sttxt like '%CLSD%') 
													and sttxt not like '%DLFL%' 
													and aedat between (date_trunc('month', current_date) - '1 mon'::interval month) and (date_trunc('month', current_date)-'1 day'::interval day)--in last 1 month
												) o on FirstT.objectid=o.objnr 	 
								 ) t 		
							inner join (
											select * , substring(objectid, 6) ordern 
											from data.change_docs 
											where objectclas='ORDER' 
											and fname in ('TPLNR', 'EQUNR') 
											and udate between (date_trunc('month', current_date) - '1 mon'::interval month) and (date_trunc('month', current_date)-'1 day'::interval day)
										) orderc on t.ordernum=orderc.ordern 
							where (udate+utime) > first_teco 
							group by ordernum1, ordernumber, first_teco 
						  ) ordc on tec.ordernum =ordc.ordernum1
				where ordc.ordernum1 is null
			 ) tno 		
		inner join ( 
						select *, ltrim(objectid, '0') notnum 
						from data.change_docs 
						where objectclas='MELDUNG' and fname in ('TPLNR', 'EQUNR') and udate between (date_trunc('month', current_date) - '1 mon'::interval month) and (date_trunc('month', current_date)-'1 day'::interval day)
				   ) notechange on tno.qmnum=notechange.notnum 
		where (notechange.udate+notechange.utime) > first_teco 
		group by ordernum, first_teco, qmnum		 
	 ) orderchanged
inner join data.orders on orderchanged.ordernumber = orders.aufnr
WHERE (orders.ingpr IS NULL OR orders.ingpr NOT IN ('500','T00','T10','T20','T30','T40','T50','T60','T70','T80','T90','TAR'))
AND (orders.stort IS NULL OR orders.stort NOT IN('ADM'))
;













--Optimized runs in 10-15 seconds
select *
from (
	select distinct 
		od.id,od.objnr, od.qmnum, od.aedat, od.ingpr, od.stort, od.iwerk, od.gewrk,od.beber,
		max(first_teco) over (partition by aufnr) as first_teco,
		max(eqfl_change) over (partition by aufnr) as eqfl_change
	from (
			select--order
				aufnr,
				min(udate+utime) filter (where fname='TECO') 
					over(partition by aufnr) "first_teco",
				max(udate+utime) filter (where fname in ('TPLNR', 'EQUNR') and udate between (date_trunc('month', current_date)-interval '1 mon') and (date_trunc('month', current_date)-interval '1 day')) 
					over(partition by aufnr) "eqfl_change",
				od.id, 
				od.objnr, 
				od.qmnum, 
				od.aedat,
				od.ingpr,
				od.stort,
				od.iwerk,
				od.gewrk,
				od.beber--select count('')
			from data.orders as od
			join data.change_docs as cd on cd.objectclas like 'OR%' and  ltrim(substring(cd.objectid, 5),'0')=od.aufnr
			where od.auart= 'MR01'
			and (od.sttxt like '%TECO%' or od.sttxt like '%CLSD%') 
			and od.sttxt not like '%DLFL%' 
			and od.aedat between (date_trunc('month', current_date) - interval '1 mon') and (date_trunc('month', current_date)-interval '1 day')--in last 1 month
			-----
			union
			-----
			select--Meldung
				aufnr,
				min(udate+utime) filter (where fname='TECO') 
					over(partition by aufnr) "first_teco",
				max(udate+utime) filter (where fname in ('TPLNR', 'EQUNR') and udate between (date_trunc('month', current_date)-interval '1 mon') and (date_trunc('month', current_date)-interval '1 day')) 
					over(partition by aufnr) "eqfl_change",
				od.id, 
				od.objnr, 
				od.qmnum, 
				od.aedat,
				od.ingpr,
				od.stort,
				od.iwerk,
				od.gewrk,
				od.beber--select count('')
			from data.orders as od
			join data.change_docs as cd on cd.objectclas like 'ME%' and  ltrim(substring(cd.objectid, 5),'0')=od.qmnum
			where od.auart= 'MR01'
			and (od.sttxt like '%TECO%' or od.sttxt like '%CLSD%') 
			and od.sttxt not like '%DLFL%' 
			and od.aedat between (date_trunc('month', current_date) - interval '1 mon') and (date_trunc('month', current_date)-interval '1 day')--in last 1 month
		) as od 
	) as od 
where first_teco is not null and eqfl_change is not null
and eqfl_change>first_teco
and  (od.ingpr IS NULL OR od.ingpr NOT IN ('500','T00','T10','T20','T30','T40','T50','T60','T70','T80','T90','TAR'))
AND (od.stort IS NULL OR od.stort NOT IN('ADM'))
;