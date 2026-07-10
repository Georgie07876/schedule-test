import dayjs, { type Dayjs } from 'dayjs';
import isoWeek from 'dayjs/plugin/isoWeek';
import { computed, ref } from 'vue';
import type { WeekParity } from '@/types/schedule';

dayjs.extend(isoWeek);

const WEEKDAY_LABELS = ['вс', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб'] as const;
const SCHEDULE_DAYS_COUNT = 6;

function getMonday(date: Dayjs): Dayjs {
  const day = date.day();
  const diff = day === 0 ? -6 : 1 - day;
  return date.add(diff, 'day').startOf('day');
}

export function useWeekNavigation() {
  const weekStart = ref(getMonday(dayjs()));

  const weekParity = computed<WeekParity>(() => {
    const weekNumber = weekStart.value.isoWeek();
    return weekNumber % 2 === 1 ? 'odd' : 'even';
  });

  const weekDays = computed(() => {
    return Array.from({ length: SCHEDULE_DAYS_COUNT }, (_, index) => {
      const date = weekStart.value.add(index, 'day');
      const dayOfWeek = index + 1;
      const weekdayLabel = WEEKDAY_LABELS[date.day()];

      return {
        dayOfWeek,
        date: date.toDate(),
        name: weekdayLabel,
        dateLabel: date.format('D MMMM'),
      };
    });
  });

  const weekLabel = computed(() => {
    const weekEnd = weekStart.value.add(SCHEDULE_DAYS_COUNT - 1, 'day');
    const startMonth = weekStart.value.format('D MMMM');
    const endPart =
      weekStart.value.month() === weekEnd.month()
        ? weekEnd.format('D MMMM')
        : weekEnd.format('D MMMM');

    return `${startMonth} – ${endPart}`;
  });

  function goToPrevWeek(): void {
    weekStart.value = weekStart.value.subtract(7, 'day');
  }

  function goToNextWeek(): void {
    weekStart.value = weekStart.value.add(7, 'day');
  }

  return {
    weekStart,
    weekDays,
    weekParity,
    weekLabel,
    goToPrevWeek,
    goToNextWeek,
  };
}
