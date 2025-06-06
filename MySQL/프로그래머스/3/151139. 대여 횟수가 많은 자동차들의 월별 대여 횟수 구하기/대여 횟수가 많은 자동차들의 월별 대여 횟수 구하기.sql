SELECT MONTH(START_DATE) MONTH, c.CAR_ID, count(c.CAR_ID) RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY c
WHERE c.CAR_ID in
    (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE >= '2022-08-01' and START_DATE <='2022-10-31'
        GROUP BY CAR_ID
        having count(CAR_ID) >= 5
    )
    and c.START_DATE >= '2022-08-01' and c.START_DATE <='2022-10-31'
GROUP BY MONTH(START_DATE), CAR_ID
HAVING COUNT(c.CAR_ID) != 0
ORDER BY 1 ASC, 2 DESC;

