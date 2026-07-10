import { defineBoot } from '#q-app';
import { apiClient } from '@/api/client';
import dayjs from 'dayjs';
import 'dayjs/locale/ru';

dayjs.locale('ru');

export default defineBoot(({ app }) => {
  app.config.globalProperties.$api = apiClient;
});

export { apiClient };
