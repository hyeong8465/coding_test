-- 코드를 입력하세요
SELECT a.PRODUCT_CODE, a.price 
* sum(b.sales_amount) as SALES
FROM PRODUCT as a, OFFLINE_SALE as b
where a.product_id = b.product_id
GROUP BY a.PRODUCT_CODE 
ORDER BY SALES DESC, a.PRODUCT_CODE ASC;