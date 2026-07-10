<template>
  <q-select
    class="search-autocomplete"
    outlined
    dense
    clearable
    use-input
    :model-value="modelValue"
    :options="options"
    :loading="loading"
    option-label="label"
    label="Поиск группы или преподавателя"
    placeholder="Начните вводить название..."
    @update:model-value="(val) => $emit('update:modelValue', val)"
    @filter="onFilter"
  >
    <template #option="{ itemProps, opt }">
      <q-item v-bind="itemProps">
        <q-item-section avatar>
          <q-icon :name="opt.type === 'group' ? 'groups' : 'person'" />
        </q-item-section>
        <q-item-section>{{ opt.label }}</q-item-section>
      </q-item>
    </template>

    <template #no-option>
      <q-item>
        <q-item-section class="text-grey">Ничего не найдено</q-item-section>
      </q-item>
    </template>
  </q-select>
</template>

<script setup lang="ts">
import type { SearchEntity } from '@/types/schedule';

defineProps<{
  modelValue: SearchEntity | null;
  options: SearchEntity[];
  loading: boolean;
}>();

const emit = defineEmits<{
  'update:modelValue': [value: SearchEntity | null];
  'update:searchQuery': [value: string];
}>();

function onFilter(val: string, update: (fn: () => void) => void) {
  update(() => {
    emit('update:searchQuery', val);
  });
}
</script>
