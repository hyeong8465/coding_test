-- 코드를 입력하세요
SELECT
    CASE
        WHEN PRICE < 10000 THEN '0000'
        ELSE concat(left(PRICE,char_length(price)-4), '0000')
    END PRICE_GROUP,
    count(*) PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
order by 1
