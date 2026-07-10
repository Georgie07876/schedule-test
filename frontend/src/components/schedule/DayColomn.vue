<template>
  <div class="day-column">
    <div class="day-column__header">
      <div class="day-column__name">{{ dayName }}</div>
      <div class="day-column__date">{{ dateLabel }}</div>
    </div>

    <div v-if="lessons.length === 0" class="day-column__empty">Занятий нет</div>

    <LessonCard
      v-for="lesson in lessons"
      :key="lesson.id"
      :lesson="lesson"
      class="day-column__lesson"
    />
  </div>
</template>

<script setup lang="ts">
import type { Lesson } from '@/types/schedule';
import LessonCard from './LessonCard.vue';

defineProps<{
  dayName: string;
  dateLabel: string;
  lessons: Lesson[];
}>();
</script>
