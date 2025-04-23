-- 코드를 입력하세요
SELECT year(sales_date) YEAR, month(sales_date) MONTH, GENDER, COUNT(distinct osi.USER_ID) USERS
FROM ONLINE_SALE osi
JOIN USER_INFO ui on osi.USER_ID = ui.USER_ID
WHERE GENDER is not null
GROUP BY YEAR, MONTH, GENDER
ORDER BY 1,2,3
;



