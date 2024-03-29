-- 코드를 입력하세요
# SELECT OUTS.ANIMAL_ID, OUTS.NAME
# FROM ANIMAL_INS AS INS INNER JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
# WHERE ANIMAL_ID( SELECT
#                 DATEDIFF(OUTS.DATETIME - INS.DATETIME) AS DATEDIFF
#                 FROM ANIMAL_INS AS INS INNER JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
#                 ORDER BY DATEDIFF DESC )
# LIMIT 2

# SELECT ANIMAL_ID, NAME
# FROM ( SELECT DATEDIFF(OUTS.DATETIME - INS.DATETIME) AS DATEDIFF
#       FROM ANIMAL_INS AS INS INNER JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID) AS TMP
# LIMIT 2

SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_INS AS INS INNER JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY DATEDIFF(OUTS.DATETIME, INS.DATETIME) DESC
LIMIT 2
# WHERE ANIMAL_ID( SELECT
#                 DATEDIFF(OUTS.DATETIME - INS.DATETIME) AS DATEDIFF
#                 FROM ANIMAL_INS AS INS INNER JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
#                 ORDER BY DATEDIFF DESC )
# LIMIT 2