-- 코드를 입력하세요
# 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와 상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을 년, 월 별로 출력
SELECT date_format(sale.sales_date, '%Y') as year,
    date_format(sale.sales_date, '%m') as month,
    count(distinct info.user_id) as p,
    round(count(distinct info.user_id)/(select count(*) from user_info where joined like '2021%'),1) as puchased_ratio

FROM USER_INFO as info

JOIN ONLINE_SALE as sale
ON info.user_id = sale.user_id

where date_format(info.joined, '%Y') = '2021'
group by year, month
order by year, month
;