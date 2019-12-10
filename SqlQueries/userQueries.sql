
select users.last_name, users.first_initial,tracker.event_date,count(tracker.event_date) from users join tracker on tracker.user_pk = users.pk group by users.pk,tracker.event_date order by users.last_name, users.first_initial ASC;


select(select count(tracker.event_date) from tracker)/(select count(users.pk) from users) as average, count(tracker.event) total from tracker;




drop view monthly;

create view monthly as
	select 
		extract(year_month from tracker.event_date) as logins_month,
		user_pk,
		count(user_pk) as total

	from tracker 
	group by user_pk, logins_month
	order by logins_month, user_pk;
select logins_month, avg(total) from monthly group by logins_month order by logins_month asc;




