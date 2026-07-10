<template>
  <div class="lesson-card" :style="{ '--lesson-color': lesson.lesson_type.color }">
    <div class="lesson-card__time">
      {{ lesson.time_slot.start_time.slice(0, 5) }} - {{ lesson.time_slot.end_time.slice(0, 5) }}
    </div>

    <div class="lesson-card__subject">
      {{ lesson.subject.name }}
      <span v-if="lesson.subgroup" class="lesson-card__subgroup">
        , п/г {{ lesson.subgroup }}
      </span>
    </div>

    <div class="lesson-card__row">
      <q-icon name="person" size="16px" />
      <span class="lesson-card__row-text">{{ lesson.teacher.full_name }}</span>
    </div>

    <div class="lesson-card__row">
      <q-icon name="place" size="16px" />
      <span class="lesson-card__row-text"
        >{{ lesson.room.number }} ({{ lesson.room.building.name }})</span
      >
    </div>

    <div class="lesson-card__type-label">{{ lesson.lesson_type.name }}</div>
  </div>
</template>

<script setup lang="ts">
import type { Lesson } from '@/types/schedule';

defineProps<{
  lesson: Lesson;
}>();
</script>
