
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d')
FROM MEMBER_PROFILE
WHERE month(DATE_OF_BIRTH) = 3 and TLNO is not null and gender = 'W'
ORDER BY MEMBER_ID ASC;