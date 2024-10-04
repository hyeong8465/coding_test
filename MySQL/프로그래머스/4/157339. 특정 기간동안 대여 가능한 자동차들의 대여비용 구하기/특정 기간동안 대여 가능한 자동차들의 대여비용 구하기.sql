

# 자동차 종류가 세단 혹은 SUV
# 20221101 - 20221130
# 30일 대여 금액 50이상 200미만
# ID, 종류, 대여 금액
select a.car_id, a.car_type, round(a.daily_fee * 30 * (1 - (c.discount_rate/100)) ) as fee
from car_rental_company_car as a

INNER JOIN
(SELECT CAR_TYPE, DISCOUNT_RATE
 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
 WHERE DURATION_TYPE = '30일 이상' AND CAR_TYPE IN ('세단', 'SUV')) as c
 ON a.CAR_TYPE = c.CAR_TYPE

AND a.CAR_ID not in
(select car_id from car_rental_company_rental_history where end_date >= '2022-11-01' and start_date <= '2022-11-30')

having fee between 500000 and 1999999
order by fee desc, a.car_type, a.car_id desc;

# SELECT a.CAR_ID, 
# a.CAR_TYPE, 
# ROUND( a.DAILY_FEE * 30 * (1 - (c.DISCOUNT_RATE / 100)) ) AS FEE
# FROM CAR_RENTAL_COMPANY_CAR as a

# INNER JOIN 
# (SELECT CAR_TYPE, DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
# WHERE DURATION_TYPE = '30일 이상' AND CAR_TYPE IN ('세단', 'SUV')) as c
# ON a.CAR_TYPE = c.CAR_TYPE

# AND a.CAR_ID NOT IN 
# (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-11-30')

# HAVING FEE BETWEEN 500000 AND 1999999

# ORDER BY FEE DESC, a.CAR_TYPE, a.CAR_ID DESC;


