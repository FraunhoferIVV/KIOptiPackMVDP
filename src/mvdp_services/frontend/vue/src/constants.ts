export const constants = {
  restBaseUrl: import.meta.env.DEV ? 'http://localhost:5478/' : '/'
} as const;
