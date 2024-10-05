-- 코드를 입력하세요
# FOOD_PRODUCT와 FOOD_ORDER 테이블에서
# 생산일자가 2022년 5월인 식품
# 식품 ID, 식품 이름, 총매출을 조회
# 총매출을 기준으로 내림차순 정렬
#총매출이 같다면 식품 ID를 기준으로 오름차순 정렬
SELECT a.product_id, b.product_name,
sum(a.amount*price) as TOTAL_SALE
from food_order as a
inner join food_product as b
on a.product_id = b.product_id

where date_format(a.produce_date, '%Y-%m') like '2022-05%'
group by a.product_id
order by total_sale desc, a.product_id
;