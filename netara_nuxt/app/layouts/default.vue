<template>
  <!-- افزودن دایرکشن داینامیک به تگ پدر -->
  <div :dir="currentDir" class="relative min-h-screen text-slate-900 dark:text-slate-50 font-sans selection:bg-purple-500 selection:text-white flex flex-col pt-20 transition-colors duration-300">
    
    <!-- پس‌زمینه جذاب و مدرن -->
    <div class="fixed inset-0 z-[-1] bg-slate-50 dark:bg-slate-950 transition-colors duration-300"></div>
    <!-- پترن شبکه‌ای -->
    <div class="fixed inset-0 z-[-1] bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
    <!-- افکت نوری بالا -->
    <div class="fixed top-0 z-[-1] h-screen w-screen bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.3),rgba(255,255,255,0))] dark:bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.15),rgba(255,255,255,0))]"></div>

    <NavBar />
    
    <!-- حذف dir="rtl" سخت‌کد شده از main -->
    <main class="flex-grow container mx-auto px-6 py-12">
      <slot />
    </main>

    <SiteFooter />
  </div>
</template>

<script setup>
import { computed } from 'vue'

// خواندن زبان از کوکی (پیش‌فرض: فارسی)
const lang = useCookie('lang', { default: () => 'fa' })
const currentDir = computed(() => lang.value === 'en' ? 'ltr' : 'rtl')

// اعمال مستقیم دایرکشن و زبان روی تگ HTML برای سئو و استایل‌های ریشه
useHead({
  htmlAttrs: {
    lang: lang,
    dir: currentDir
  }
})
</script>
