select view weekly as 
    select 
        extract(YEAR,Month from event_date) as login_year,
        user_pk.
        count(user_pk) as total
    from tracker
    group user_pk, login_year
    
select login_year, avg(total)
from weekly
group by login year 
