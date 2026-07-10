import axios from 'axios';

export const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/v1/schedule',
  timeout: 10000,
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    const err = error instanceof Error ? error : new Error(String(error));
    return Promise.reject(err);
  },
);
