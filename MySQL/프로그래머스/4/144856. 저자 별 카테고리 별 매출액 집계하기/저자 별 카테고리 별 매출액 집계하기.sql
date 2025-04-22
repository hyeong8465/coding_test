# 2022-01의 저자별, 카테고리 별 매출액을 구해라
# 저자 id, 저자명, 카테고리, 매출액 출력
select b.author_id, a.author_name, b.category, sum(s.sales*b.price) TOTAL_SALES
FROM BOOK b
JOIN AUTHOR a on b.author_id = a. author_id
JOIN (SELECT * FROM BOOK_SALES WHERE SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31') s on s.book_id = b.book_id
group by a.author_name, b.category
ORDER BY b.author_id, b.category desc


;

# (SELECT * FROM BOOK_SALES WHERE SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31') sales