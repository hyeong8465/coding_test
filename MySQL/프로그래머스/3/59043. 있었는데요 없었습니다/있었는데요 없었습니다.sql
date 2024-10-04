/*
보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회
*/


-- 코드를 입력하세요
SELECT ins.animal_id, ins.name
from animal_ins as ins, animal_outs as outs
where ins.animal_id = outs.animal_id and ins.datetime > outs.datetime
order by ins.datetime asc;