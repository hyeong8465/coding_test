/*
입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
outs에는 있지만 ins에는 없는 데이터
*/
SELECT outs.animal_id, outs.name
FROM animal_outs AS outs
LEFT OUTER JOIN animal_ins AS ins
ON outs.animal_id = ins.animal_id
WHERE ins.animal_id IS NULL
ORDER BY outs.animal_id;