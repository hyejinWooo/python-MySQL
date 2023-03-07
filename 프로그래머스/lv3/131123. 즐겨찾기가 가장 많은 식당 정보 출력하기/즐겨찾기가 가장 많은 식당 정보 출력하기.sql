-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO A
WHERE FAVORITES IN(SELECT MAX(FAVORITES) FROM REST_INFO B WHERE A.FOOD_TYPE = B.FOOD_TYPE)
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC

# SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
# FROM REST_INFO
# ORDER BY FOOD_TYPE DESC

# SELECT food_type, rest_id, rest_name, favorites 
# from rest_info a 
# where favorites = (select max(favorites) from rest_info b where a.food_type = b.food_type)
# group by food_type
# order by food_type desc