import { apiClient } from './client';
import type {
  GetLessonsParams,
  Group,
  Lesson,
  PaginatedResponse,
  Teacher,
} from '@/types/schedule';

const PAGE_SIZE = 100;

export async function getGroups(): Promise<Group[]> {
  const { data } = await apiClient.get<PaginatedResponse<Group>>('/groups/', {
    params: { page_size: PAGE_SIZE },
  });
  return data.results;
}

export async function getTeachers(): Promise<Teacher[]> {
  const { data } = await apiClient.get<PaginatedResponse<Teacher>>('/teachers/', {
    params: { page_size: PAGE_SIZE },
  });
  return data.results;
}

export async function getLessons(params: GetLessonsParams): Promise<Lesson[]> {
  const { data } = await apiClient.get<PaginatedResponse<Lesson>>('/lessons/', {
    params: {
      ...params,
      page_size: PAGE_SIZE,
    },
  });
  return data.results;
}
