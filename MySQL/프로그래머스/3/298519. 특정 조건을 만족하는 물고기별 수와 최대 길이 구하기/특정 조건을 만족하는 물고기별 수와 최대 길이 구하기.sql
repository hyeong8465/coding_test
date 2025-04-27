-- 코드를 작성해주세요
select fish_count, max_length, fish_type
from
    (
    select
    fish_type,
    avg(temp) length,
    max(temp) max_length,
    count(*) fish_count
from (
    select
        fish_type,
        case
            when length <= 10 then 10
            else length
        end temp
    from FISH_INFO) a
    group by fish_type) b
where length >= 33
order by fish_type asc;


# select
#     fish_type,
#     avg(temp) length,
#     max(temp) max_length,
#     count(*) fish_count
# from (
#     select
#     fish_type,
#     case
#         when length <= 10 then 10
#         else length
#     end temp
#     from FISH_INFO) a
# group by fish_type