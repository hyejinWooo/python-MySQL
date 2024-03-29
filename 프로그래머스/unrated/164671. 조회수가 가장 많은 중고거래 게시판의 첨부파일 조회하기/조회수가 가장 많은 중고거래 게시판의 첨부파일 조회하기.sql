-- 코드를 입력하세요
SELECT CONCAT("/home/grep/src/", FILE.BOARD_ID, "/", FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM (SELECT BOARD_ID
      FROM USED_GOODS_BOARD
      ORDER BY VIEWS DESC
      LIMIT 1) AS BOARD INNER JOIN USED_GOODS_FILE AS FILE ON BOARD.BOARD_ID = FILE.BOARD_ID
ORDER BY FILE_ID DESC