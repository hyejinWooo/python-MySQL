-- 코드를 입력하세요
# SELECT I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
# FROM REST_INFO AS I INNER JOIN REST_REVIEW AS R ON I.REST_ID = R.REST_ID
# WHERE ADDRESS LIKE '%서울%'
# ORDER BY SCORE DESC, FAVORITES DESC

# SELECT I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
# FROM REST_INFO AS I INNER JOIN REST_REVIEW AS R ON I.REST_ID = R.REST_ID
# GROUP BY REST_ID
# HAVING ADDRESS LIKE '%서울%'
# ORDER BY SCORE DESC, FAVORITES DESC

SELECT A.REST_ID, B.REST_NAME, B.FOOD_TYPE, B.FAVORITES, B.ADDRESS, ROUND(AVG(A.REVIEW_SCORE),2) AS SCORE
FROM REST_REVIEW A
JOIN REST_INFO B ON A.REST_ID = B.REST_ID
GROUP BY A.REST_ID
HAVING B.ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, B.FAVORITES DESC