SELECT *
FROM (SELECT sum(score) SCORE, e.EMP_NO, e.EMP_NAME, POSITION, EMAIL
    FROM HR_EMPLOYEES e
    JOIN HR_GRADE g on e.emp_no = g.emp_no
    JOIN hr_department d on e.dept_id = d.dept_id
    group by e.emp_no) a
WHERE SCORE = (SELECT max(SCORE)
              FROM (SELECT sum(score) SCORE, e.EMP_NO, e.EMP_NAME, POSITION, EMAIL
    FROM HR_EMPLOYEES e
    JOIN HR_GRADE g on e.emp_no = g.emp_no
    JOIN hr_department d on e.dept_id = d.dept_id
    group by e.emp_no) b
)

;