import { computed, ref } from 'vue';
import { getGroups, getTeachers } from '@/api/schedule';
import type { Group, SearchEntity, Teacher } from '@/types/schedule';

const MIN_QUERY_LENGTH = 2;

export function useSearch() {
  const searchQuery = ref('');
  const loading = ref(false);
  const error = ref<string | null>(null);
  const selected = ref<SearchEntity | null>(null);

  const groups = ref<Group[]>([]);
  const teachers = ref<Teacher[]>([]);

  const loadEntities = async () => {
    loading.value = true;
    error.value = null;
    try {
      const [groupsRes, teachersRes] = await Promise.all([getGroups(), getTeachers()]);
      groups.value = groupsRes;
      teachers.value = teachersRes;
    } catch (err) {
      console.error('Ошибка при загрузке сущностей:', err);
      error.value = 'Не удалось загрузить список групп и преподавателей.';
    } finally {
      loading.value = false;
    }
  };

  const filteredEntities = computed<SearchEntity[]>(() => {
    const query = searchQuery.value.trim().toLowerCase();
    if (query.length < MIN_QUERY_LENGTH) {
      return [];
    }

    const groupResults: SearchEntity[] = groups.value
      .filter((group) => group.name.toLowerCase().includes(query))
      .map((group) => ({
        type: 'group',
        id: group.id,
        label: group.name,
      }));

    const teacherResults: SearchEntity[] = teachers.value
      .filter((teacher) => teacher.full_name.toLowerCase().includes(query))
      .map((teacher) => ({
        type: 'teacher',
        id: teacher.id,
        label: teacher.full_name,
      }));

    return [...groupResults, ...teacherResults];
  });

  const selectEntity = (entity: SearchEntity | null) => {
    selected.value = entity;
  };

  const clearSelection = () => {
    selected.value = null;
    searchQuery.value = '';
  };

  return {
    searchQuery,
    loading,
    error,
    selected,
    filteredEntities,
    loadEntities,
    selectEntity,
    clearSelection,
  };
}
