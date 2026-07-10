SELECT DISTINCT
    g.name AS group_name,
    g.course
FROM schedule_lesson l
JOIN schedule_group g     ON l.group_id = g.id
JOIN schedule_room r      ON l.room_id = r.id
JOIN schedule_building b  ON r.building_id = b.id
WHERE r.number = '212'
  AND b.name = 'Главный корпус'
  AND l.day_of_week = 3                     
ORDER BY g.name;
