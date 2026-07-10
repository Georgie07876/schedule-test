SELECT
    l.day_of_week,
    ts.number       AS pair_number,
    ts.start_time,
    ts.end_time,
    g.name          AS group_name,
    l.subgroup,
    s.name          AS subject,
    lt.name         AS lesson_type,
    l.week_parity,
    b.name          AS building,
    r.number        AS room_number
FROM schedule_lesson l
JOIN schedule_teacher t     ON l.teacher_id = t.id
JOIN schedule_group g       ON l.group_id = g.id
JOIN schedule_subject s     ON l.subject_id = s.id
JOIN schedule_lessontype lt ON l.lesson_type_id = lt.id
JOIN schedule_room r        ON l.room_id = r.id
JOIN schedule_building b    ON r.building_id = b.id
JOIN schedule_timeslot ts   ON l.time_slot_id = ts.id
WHERE t.last_name = 'Долженко'
  AND t.first_name = 'Алексей'
  AND t.middle_name = 'Иванович'
ORDER BY l.day_of_week, ts.number, l.week_parity;
