<template>
  <div class="week-navigator">
    <q-btn flat dense icon="chevron_left" label="Предыдущая неделя" @click="$emit('prev')" />
    <div class="week-navigator__label">
      {{ weekLabel }}
      <span class="week-navigator__parity">({{ parityLabel }})</span>
    </div>
    <q-btn flat dense icon-right="chevron_right" label="Следующая неделя" @click="$emit('next')" />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import type { WeekParity } from '@/types/schedule';

const props = defineProps<{
  weekLabel: string;
  weekParity: WeekParity;
}>();

defineEmits<{
  prev: [];
  next: [];
}>();

const parityLabel = computed(() => {
  const labels: Record<WeekParity, string> = {
    odd: 'нечётная неделя',
    even: 'чётная неделя',
    every: 'каждая неделя',
  };
  return labels[props.weekParity];
});
</script>
