export interface Group {
  id: number;
  name: string;
  course: number | null;
}

export interface Building {
  id: number;
  name: string;
}

export interface Room {
  id: number;
  number: string;
  building: Building;
  capacity: number | null;
}

export interface Subject {
  id: number;
  name: string;
}

export interface Teacher {
  id: number;
  last_name: string;
  first_name: string;
  middle_name: string;
  academic_title: string;
  full_name: string;
}

export interface TimeSlot {
  id: number;
  number: number;
  start_time: string;
  end_time: string;
}

export interface LessonType {
  id: number;
  name: string;
  color: string;
}

export type WeekParity = 'odd' | 'even' | 'every';

export interface Lesson {
  id: number;
  group: Group;
  teacher: Teacher;
  room: Room;
  subject: Subject;
  lesson_type: LessonType;
  time_slot: TimeSlot;
  day_of_week: number;
  day_of_week_display: string;
  week_parity: WeekParity;
  week_parity_display: string;
  subgroup: number | null;
}

export type SearchEntity =
  { type: 'group'; id: number; label: string } | { type: 'teacher'; id: number; label: string };

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export type ScheduleStatus = 'idle' | 'loading' | 'loaded' | 'error';

export interface DaySchedule {
  dayOfWeek: number;
  date: Date;
  dateLabel: string;
  lessons: Lesson[];
}

export type GetLessonsParams =
  { group: number; week_parity: WeekParity } | { teacher: number; week_parity: WeekParity };
