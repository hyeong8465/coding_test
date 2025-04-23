-- 코드를 입력하세요
# SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
# FROM ANIMAL_OUTS
# GROUP BY HOUR;


# 0~23범위를 어떻게 지정하나
with recursive temp as (
    select 0 hour
    union all
    select hour+1 from temp where hour<23
)
select t.hour hour, count(datetime) count
from temp t
left join animal_outs ao on hour(ao.datetime) = t.hour
group by t.hour
order by t.hour

