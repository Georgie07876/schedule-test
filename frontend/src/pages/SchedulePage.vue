<template>
  <q-page class="schedule-page">
    <div class="schedule-page__inner">
      <h1 class="schedule-page__title">Расписание занятий</h1>

      <div class="schedule-page__search">
        <SearchAutocomplete
          v-if="!search.selected.value"
          :model-value="search.selected.value"
          :options="search.filteredEntities.value"
          :loading="search.loading.value"
          @update:model-value="onEntitySelected"
          @update:search-query="(q) => (search.searchQuery.value = q)"
        />
        <SelectedEntity v-else :entity="search.selected.value" @clear="onClearSelection" />

        <div v-if="search.error.value" class="schedule-page__search-error">
          {{ search.error.value }}
        </div>
      </div>

      <template v-if="search.selected.value">
        <WeekNavigator
          class="schedule-page__navigator"
          :week-label="week.weekLabel.value"
          :week-parity="week.weekParity.value"
          @prev="week.goToPrevWeek"
          @next="week.goToNextWeek"
        />

        <div v-if="schedule.loading.value" class="schedule-page__loading">
          <q-spinner color="primary" size="40px" />
        </div>

        <EmptyState
          v-else-if="schedule.error.value"
          icon="error_outline"
          :message="schedule.error.value"
        />

        <ScheduleGrid v-else :lessons="schedule.lessons.value" :week-days="week.weekDays.value" />
      </template>

      <EmptyState v-else message="Выберите группу или преподавателя, чтобы увидеть расписание" />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { onMounted, watch } from 'vue';
import { useSearch } from '@/composables/useSearch';
import { useWeekNavigation } from '@/composables/useWeekNavigation';
import { useSchedule } from '@/composables/useSchedule';
import type { SearchEntity } from '@/types/schedule';

import SearchAutocomplete from '@/components/search/SearchAutocomplete.vue';
import SelectedEntity from '@/components/search/SelectedEntity.vue';
import WeekNavigator from '@/components/schedule/WeekNavigator.vue';
import ScheduleGrid from '@/components/schedule/ScheduleGrid.vue';
import EmptyState from '@/components/common/EmptyState.vue';

const search = useSearch();
const week = useWeekNavigation();
const schedule = useSchedule();

onMounted(() => {
  void search.loadEntities();
});

function onEntitySelected(entity: SearchEntity | null) {
  search.selectEntity(entity);
}

function onClearSelection() {
  search.clearSelection();
  schedule.lessons.value = [];
}

watch(
  [() => search.selected.value, () => week.weekParity.value],
  ([entity, parity]) => {
    if (!entity) return;
    void schedule.loadSchedule(
      entity.type === 'group'
        ? { groupId: entity.id, weekParity: parity }
        : { teacherId: entity.id, weekParity: parity },
    );
  },
  { immediate: false },
);
</script>
