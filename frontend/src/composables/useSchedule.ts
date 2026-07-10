import { ref } from 'vue';
import { getLessons } from '@/api/schedule';
import type { Lesson, WeekParity, GetLessonsParams } from '@/types/schedule';

export function useSchedule() {
  const lessons = ref<Lesson[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);

  async function loadSchedule(params: {
    groupId?: number;
    teacherId?: number;
    weekParity: WeekParity;
  }) {
    loading.value = true;
    error.value = null;

    try {
      let lessonsParams: GetLessonsParams;
      if (params.groupId !== undefined) {
        lessonsParams = { group: params.groupId, week_parity: params.weekParity };
      } else if (params.teacherId !== undefined) {
        lessonsParams = { teacher: params.teacherId, week_parity: params.weekParity };
      } else {
        lessons.value = [];
        return;
      }
      lessons.value = await getLessons(lessonsParams);
    } catch {
      error.value = 'Не удалось загрузить расписание. Попробуйте ещё раз.';
      lessons.value = [];
    } finally {
      loading.value = false;
    }
  }

  return { lessons, loading, error, loadSchedule };
}
