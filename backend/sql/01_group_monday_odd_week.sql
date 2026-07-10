
SELECT
    ts.number          AS pair_number,
    ts.start_time,
    ts.end_time,
    s.name             AS subject,
    lt.name            AS lesson_type,
    l.subgroup,
    b.name             AS building,
    r.number           AS room_number,
    t.last_name        AS teacher_last_name,
    t.first_name       AS teacher_first_name,
    t.academic_title
FROM schedule_lesson l
JOIN schedule_group g       ON l.group_id = g.id
JOIN schedule_subject s     ON l.subject_id = s.id
JOIN schedule_lessontype lt ON l.lesson_type_id = lt.id
JOIN schedule_room r        ON l.room_id = r.id
JOIN schedule_building b    ON r.building_id = b.id
JOIN schedule_teacher t     ON l.teacher_id = t.id
JOIN schedule_timeslot ts   ON l.time_slot_id = ts.id
WHERE g.name = 'ИСТ-311'
  AND l.day_of_week = 1                     
  AND l.week_parity IN ('odd', 'every')
ORDER BY ts.number;
