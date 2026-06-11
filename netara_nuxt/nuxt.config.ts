import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  css: ['./app/assets/css/main.css'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:8000/api',   // یا دامنهٔ سرور
      apiBaseHost: 'http://127.0.0.1:8000'    // برای چسباندن URL فایل‌های media
    }
  }
});