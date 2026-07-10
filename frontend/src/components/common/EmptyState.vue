<template>
  <div class="empty-state">
    <q-icon :name="icon" size="48px" class="empty-state__icon" />
    <div class="empty-state__message">{{ message }}</div>
  </div>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    message: string;
    icon?: string;
  }>(),
  {
    icon: 'search',
  },
);
</script>
