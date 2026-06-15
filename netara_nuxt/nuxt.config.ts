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
      // فقط مقادیر پیش‌فرض (لوکال) را اینجا می‌نویسیم
      // در محیط پروداکشن، Nuxt به‌طور خودکار مقادیر فایل env. را جایگزین می‌کند
      apiBase: 'http://127.0.0.1:8000/api', 
      apiBaseHost: 'http://127.0.0.1:8000'
    }
  }
});
