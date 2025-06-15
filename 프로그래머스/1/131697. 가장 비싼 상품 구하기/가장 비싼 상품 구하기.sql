-- 코드를 입력하세요
SELECT max(PRICE) as MAX_PRICE
from PRODUCT
group by PRICE
order by PRICE desc
limit 1
