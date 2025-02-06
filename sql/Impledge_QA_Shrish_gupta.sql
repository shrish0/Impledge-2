UPDATE [Admissions]
SET attending_doctor_id = 29
WHERE attending_doctor_id = 3;
UPDATE [Admissions]
SET patient_id = 4
WHERE patient_id = 35;
SELECT COUNT(*) FROM Admissions WHERE attending_doctor_id = 5;


/* select from line no 11 to 19 for case 1 */
UPDATE [Admissions]
SET attending_doctor_id = 29
WHERE attending_doctor_id = 3;
UPDATE [Admissions]
SET patient_id = 4
WHERE patient_id = 35;
select distinct doctors.* , admissions.patient_id
from doctors join admissions 
where doctors.doctor_id=admissions.attending_doctor_id;

/* select from line no 22 to 31 for case 2 */
UPDATE [Admissions]
SET attending_doctor_id = 29
WHERE attending_doctor_id = 3;
UPDATE [Admissions]
SET patient_id = 4
WHERE patient_id = 35;
SELECT d.*
FROM doctors d
LEFT JOIN Admissions a ON d.doctor_id = a.attending_doctor_id
WHERE a.attending_doctor_id IS NULL;

/* select from line no 34 to 44 for case 3 */
UPDATE [Admissions]
SET attending_doctor_id = 29
WHERE attending_doctor_id = 3;
UPDATE [Admissions]
SET patient_id = 4
WHERE patient_id = 35;
SELECT p.*
FROM patients p
JOIN Admissions a ON p.patient_id = a.patient_id
LEFT JOIN doctors d ON a.attending_doctor_id = d.doctor_id
WHERE a.attending_doctor_id IS NULL OR d.doctor_id IS NULL;


