-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS B INNER JOIN USED_GOODS_USER AS U ON B.WRITER_ID = U.USER_ID
WHERE STATUS = "DONE"
GROUP BY USER_ID
HAVING TOTAL_SALES >=700000
ORDER BY TOTAL_SALES