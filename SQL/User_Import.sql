
go

DECLARE @d_sql NVARCHAR(MAX)
SET @d_sql = ''

SELECT @d_sql = @d_sql + 'DROP TABLE ' + QUOTENAME(name) + ';
'
FROM tempdb..sysobjects
WHERE name like '#[^#]%'
AND OBJECT_ID('tempdb..'+QUOTENAME(name)) IS NOT NULL

IF @d_sql <> ''
BEGIN
    EXEC( @d_sql )
END

go



IF OBJECT_ID('tempdb..#UserRoles') IS NOT NULL  
begin
	drop table #UserRoles
end

create table #UserRoles(
	id int identity,
	email varchar(100) collate Latin1_General_CI_AS,
	[Systemrole1] varchar(100) collate Latin1_General_CI_AS,
	[SystemRole2] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole3] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole4] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole5] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole6] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole7] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole8] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole9] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole10] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole11] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole12] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole13] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole14] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole15] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole16] varchar(100) collate Latin1_General_CI_AS,
	[Systemrole17] varchar(100) collate Latin1_General_CI_AS 
	ResponsibilityGroup varchar(100) collate Latin1_General_CI_AS,
	ResponsibilityGroup2 varchar(100) collate Latin1_General_CI_AS,
	ResponsibilityGroup3 varchar(100) collate Latin1_General_CI_AS,
	ResponsibilityGroup4 varchar(100) collate Latin1_General_CI_AS,
	 )
insert into #UserRoles (email, [Systemrole1], [SystemRole2], [Systemrole3], [Systemrole4], [Systemrole5], [Systemrole6], [Systemrole7], [Systemrole8], [Systemrole9], [Systemrole10], [Systemrole11], [Systemrole12], [Systemrole13], [Systemrole14], [Systemrole15], [Systemrole16], [Systemrole17],ResponsibilityGroup, ResponsibilityGroup2, ResponsibilityGroup3, ResponsibilityGroup4)
values
('Devan.Walton@yahoo.com','Y','','','','Y','','','','','','y','','','','','','','all','','',''),
('Juliana.Savage@yahoo.com','Y','','','','Y','','','','y','','','y','','','','y','','all','','',''),
('Joanna.Osborn@yahoo.com','Y','','','','Y','','','','y','','','y','','','','y','','all','','',''),
('Kevin.Hopkins@yahoo.com','Y','','','','Y','','','','','','','','','','','','','','area1','area2','area3'),
('Maxwell.Contreras@yahoo.com','Y','','','','Y','','','y','','','','y','','','','','','','area4','area5','area6'),
('Jaylen.Ferrell@yahoo.com','Y','','','','Y','','','','','','','','','','','','','','area7','area8','area9'),
('Corinne.Boyle@yahoo.com','Y','','','','Y','','','','','','y','','','','','y','','area1','area10','area11','area12'),
('Johanna.Kelley@yahoo.com','Y','','','','Y','','','','','','','','','','','','','area1','area13','area14','area15'),
('Reid.Compton@yahoo.com','Y','','','','Y','','','y','','','','','','','','','','area1','area16','area17','area18'),
('Madalyn.Holder@yahoo.com','Y','','','','Y','','','','','','','','','','','','','area1','area12','area13','area14'),
('Kadin.Stout@yahoo.com','Y','','','','Y','','','','','','','','','','','','','area1','area15','area16','area17'),
('Lincoln.Salazar@yahoo.com','Y','','','','Y','','','','','','','','','','','','','area1','area11','area12','area13'),
('Skyla.Cannon@yahoo.com','Y','','','','Y','','','','','','','','','','','','','area1','area14','area15','area16')


insert into person(email)
select distinct
	email
from #UserRoles as a 
left join person as x on x.emial=a.email
where x.personid is null

------insert user per group mapping
IF OBJECT_ID('tempdb..#Temp') IS NOT NULL begin drop table #temp end

select 
	row_number() over (order by t.name,c.name) as id,
	c.name AS column_name--select *
into #temp
FROM tempdb.sys.tables AS t
left join tempdb.sys.columns c ON t.OBJECT_ID = c.OBJECT_ID
where 1=1 
and t.create_date=(select max(create_date) from tempdb.sys.tables where name like'%#UserRoles_%')
and t.name like'%#UserRoles_%'
and c.name not in ('email','id')
and c.name not like '%ResponsibilityGroup%'

declare @sqlcommand nvarchar(max)=''
declare @SystemRole  nvarchar(500)=''
declare @count1 int=1

while @count1<=(select count(*) from #Temp)
	begin 
	
	set @SystemRole=(select column_name from #Temp where id=@count1)

	set @sqlcommand='
	--check for null systemroles or null username them uncomment out next line and change print to execute
	insert into PersonSystemRole(personid,SystemRoleID,ResponsibilityGroupID)
	select 
		c.PersonID,
		d.SystemRoleID,
		r.responsibilitygroupid
		--select *
	from #UserRoles as a 
	left join person as c on c.Username=a.email 
	left join systemrole as d on d.name='''+@SystemRole+'''
	left join responsibilitygroup as r on iif(a.responsibilitygroup=''all'',a.responsibilitygroup, r.name)=a.responsibilitygroup and r.siteid='+@siteid+'
	left join PersonSystemRole as x on x.personid=c.personid and x.systemroleid=d.systemroleid and x.responsibilitygroupid=r.responsibilitygroupid
	where a.responsibilitygroup<>'''' and x.personsystemroleid is null and a.['+@SystemRole+']=''y'''

	exec (@sqlcommand)

	set @sqlcommand=replace(@sqlcommand,'a.responsibilitygroup','a.responsibilitygroup2')
	exec (@sqlcommand)

	set @sqlcommand=replace(@sqlcommand,'a.responsibilitygroup2','a.responsibilitygroup3')
	exec (@sqlcommand)

	set @sqlcommand=replace(@sqlcommand,'a.responsibilitygroup3','a.responsibilitygroup4')
	exec (@sqlcommand)

	set @count1=@count1+1
	end


insert into personsite(personid,SiteID)
select 
	b.personid,
	c.siteid
from #UserRoles as a 
left join person as b on b.username=a.email
left join site as c on c.name=@siteid
left join personsite as x on x.personid=b.personid and x.SiteID=c.SiteID
where x.personsiteid is null
