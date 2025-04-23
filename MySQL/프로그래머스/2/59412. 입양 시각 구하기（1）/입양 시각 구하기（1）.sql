-- 코드를 입력하세요
SELECT HOUR(datetime) HOUR, COUNT(*) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
having HOUR BETWEEN 9 and 19
ORDER BY HOUR asc


# select *
# from animal_outs;