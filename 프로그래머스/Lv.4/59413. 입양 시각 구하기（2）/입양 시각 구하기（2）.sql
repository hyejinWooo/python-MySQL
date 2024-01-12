-- 코드를 입력하세요
# SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
# FROM (SELECT HOUR(DATETIME) AS HOUR
#       FROM ANIMAL_OUTS
#       GROUP BY HOUR
#       HAVING HOUR BETWEEN 0 AND 23
# GROUP BY HOUR
# HAVING HOUR BETWEEN 0 AND 23
# ORDER BY HOUR

# SELECT HOUR(DATETIME) AS HOUR,
#     CASE
#         WHEN COUNT IS NULL THEN 0
#         ELSE COUNT(*)
#     END COUNT
# FROM ANIMAL_OUTS IN (SELECT COUNT(*) AS COUNT
#       FROM ANIMAL_OUTS
#       GROUP BY HOUR
#       HAVING HOUR(DATETIME) BETWEEN 0 AND 23) 
# ORDER BY HOUR

# SELECT HOUR(DATETIME) AS HOUR,
#     CASE
#         WHEN COUNT IS NULL THEN 0
#         ELSE COUNT(*)
#     END COUNT
# FROM ANIMAL_OUTS
# WHERE HOUR IN()
# ORDER BY HOUR

# SELECT
#     CASE
#         WHEN HOUR(DATETIME) BETWEEN 0 AND 23 , COUNT(*) AS COUNT
# FROM ANIMAL_OUTS 
# GROUP BY HOUR
# HAVING HOUR BETWEEN 0 AND 23
# ORDER BY HOUR

set @hour := -1;
# ; 중요!!

select (@hour := @hour+1) as HOUR, (select count(*) from animal_outs where hour(datetime) = @hour) as count
# hour라는 변수와 데이터 안의 hour가 일치하면 카운트
from animal_outs
# group by hour
where @hour > -2 and @hour < 23 # 왜 where @hour > 0 and @hour < 23 이건 안 되는지...
order by @hour

# SET @hour := -1; -- 변수 선언

# SELECT (@hour := @hour + 1) as HOUR,
# (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
# FROM ANIMAL_OUTS
# WHERE @hour < 23


# WITH RECURSIVE TIME AS(
# SELECT 0 AS H UNION ALL SELECT H+1 FROM TIME WHERE H < 23
# )
# SELECT
# H AS 'HOUR',
# COUNT(HOUR(DATETIME)) AS 'COUNT'
# FROM TIME LEFT JOIN ANIMAL_OUTS ON (H=HOUR(DATETIME))