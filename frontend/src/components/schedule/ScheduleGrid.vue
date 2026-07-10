<template>
  <div class="schedule-grid">
    <DayColumn
      v-for="day in weekDays"
      :key="day.dayOfWeek"
      :day-name="day.name"
      :date-label="day.dateLabel"
      :lessons="lessonsByDay(day.dayOfWeek)"
      class="schedule-grid__column"
    />
  </div>
</template>

<script setup lang="ts">
import type { Lesson } from '@/types/schedule';
import DayColumn from './DayColomn.vue';

interface WeekDay {
  dayOfWeek: number;
  name: string;
  dateLabel: string;
}

const props = defineProps<{
  lessons: Lesson[];
  weekDays: WeekDay[];
}>();

function lessonsByDay(dayOfWeek: number): Lesson[] {
  return props.lessons
    .filter((lesson) => lesson.day_of_week === dayOfWeek)
    .sort((a, b) => a.time_slot.number - b.time_slot.number);
}
</script>
