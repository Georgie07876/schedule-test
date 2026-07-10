<template>
  <q-chip
    removable
    class="selected-entity"
    color="primary"
    text-color="white"
    @remove="$emit('clear')"
  >
    <q-icon :name="entity.type === 'group' ? 'groups' : 'person'" left />
    {{ entity.label }}
  </q-chip>
</template>

<script setup lang="ts">
import type { SearchEntity } from '@/types/schedule';

defineProps<{
  entity: SearchEntity;
}>();

defineEmits<{
  clear: [];
}>();
</script>
