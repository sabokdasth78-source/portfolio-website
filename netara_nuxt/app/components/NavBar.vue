<template>
  <header class="fixed top-0 left-0 right-0 z-50 bg-white/70 dark:bg-slate-950/70 backdrop-blur-lg border-b border-slate-200 dark:border-white/10 transition-all duration-300 shadow-sm dark:shadow-none">
    <nav class="container mx-auto px-4 md:px-6 py-3 flex justify-between items-center" dir="rtl">
      
      <!-- لوگو و نام -->
      <NuxtLink href="/" class="flex items-center gap-2 md:gap-3 group">
        <img src="/logo.png" alt="لوگو" class="h-8 w-8 md:h-10 md:w-10 object-contain group-hover:scale-110 transition-transform duration-300 drop-shadow-md" />
        <div class="text-xl md:text-2xl font-black tracking-tighter text-slate-900 dark:text-white">
          نت<span class="text-transparent bg-clip-text bg-gradient-to-l from-cyan-500 to-purple-600 dark:from-cyan-400 dark:to-purple-500"> آرا  </span>
        </div>
      </NuxtLink>
      
      <!-- لینک‌های دسکتاپ و دکمه‌ها -->
      <div class="flex items-center gap-3 md:gap-8">
        <ul class="hidden md:flex gap-6 lg:gap-8 text-sm font-medium text-slate-600 dark:text-slate-300">
          <li><NuxtLink href="/" class="hover:text-cyan-600 dark:hover:text-cyan-400 transition-colors">خانه</NuxtLink></li>
          <li><NuxtLink href="/projects" class="hover:text-cyan-600 dark:hover:text-cyan-400 transition-colors">پروژه‌ها</NuxtLink></li>
          <li><NuxtLink href="/blog" class="hover:text-cyan-600 dark:hover:text-cyan-400 transition-colors">وبلاگ</NuxtLink></li>
          <li><NuxtLink href="/about" class="hover:text-cyan-600 dark:hover:text-cyan-400 transition-colors">درباره من</NuxtLink></li>
        </ul>
        
        <div class="flex items-center gap-2 md:gap-3">
          
          <!-- دکمه‌های احراز هویت دسکتاپ -->
          <div class="hidden md:flex items-center gap-2">
            <!-- اگر کاربر لاگین نکرده بود -->
            <template v-if="!user">
              <NuxtLink href="/login" class="text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-cyan-600 dark:hover:text-cyan-400 transition-colors px-2">ورود</NuxtLink>
              <NuxtLink href="/register" class="text-sm font-medium text-white bg-slate-800 dark:bg-white/10 hover:bg-slate-700 dark:hover:bg-white/20 px-4 py-1.5 rounded-full transition-colors border border-transparent dark:border-white/10">ثبت‌نام</NuxtLink>
            </template>

            <!-- اگر کاربر لاگین کرده بود -->
            <template v-else>
              <NuxtLink href="/dashboard" class="flex items-center gap-1 text-sm font-medium text-slate-700 dark:text-slate-200 bg-cyan-50 dark:bg-cyan-500/10 hover:bg-cyan-100 dark:hover:bg-cyan-500/20 px-4 py-1.5 rounded-full transition-colors border border-cyan-200 dark:border-cyan-500/30">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                حساب کاربری
              </NuxtLink>
              <button @click="handleLogout" class="text-sm font-medium text-red-500 hover:text-red-600 dark:text-red-400 dark:hover:text-red-300 transition-colors px-2" title="خروج">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
              </button>
            </template>
          </div>

          <!-- دکمه دریافت مشاوره -->
          <NuxtLink href="/contact" class="hidden sm:flex items-center px-4 py-1.5 md:px-5 md:py-2 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white text-xs md:text-sm font-bold hover:shadow-[0_0_15px_rgba(6,182,212,0.4)] hover:scale-105 transition-all duration-300">
            دریافت مشاوره
          </NuxtLink>

          <!-- خط جداکننده (فقط در دسکتاپ) -->
          <div class="hidden md:block w-px h-6 bg-slate-300 dark:bg-slate-700"></div>

          <!-- دکمه تغییر حالت تاریک/روشن -->
          <button @click="toggleDark()" class="p-2 md:p-2.5 rounded-full bg-slate-100 dark:bg-slate-800/50 text-slate-600 dark:text-slate-300 hover:bg-cyan-100 dark:hover:bg-cyan-900/30 hover:text-cyan-600 dark:hover:text-cyan-400 transition-all duration-300 border border-transparent dark:border-white/5">
            <svg v-if="isDark" class="w-4 h-4 md:w-5 md:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
            <svg v-else class="w-4 h-4 md:w-5 md:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
          </button>

          <!-- دکمه منوی موبایل (فقط موبایل) -->
          <button @click="isMobileMenuOpen = !isMobileMenuOpen" class="md:hidden p-2 rounded-full bg-slate-100 dark:bg-slate-800/50 text-slate-600 dark:text-slate-300 hover:text-cyan-600 dark:hover:text-cyan-400 transition-all">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path v-if="!isMobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
      </div>
    </nav>

    <!-- منوی موبایل (کشویی) -->
    <div v-show="isMobileMenuOpen" class="md:hidden absolute top-full left-0 right-0 bg-white/95 dark:bg-slate-950/95 backdrop-blur-xl border-b border-slate-200 dark:border-white/10 shadow-lg px-4 py-6 flex flex-col gap-4" dir="rtl">
      
      <!-- پروفایل در موبایل -->
      <div v-if="user" class="flex items-center justify-between pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-2 text-slate-700 dark:text-slate-200 font-bold">
          <svg class="w-6 h-6 text-cyan-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          {{ user }}
        </div>
        <button @click="handleLogout" class="text-sm text-red-500">خروج</button>
      </div>
      <div v-else class="flex gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <NuxtLink @click="isMobileMenuOpen = false" href="/login" class="flex-1 text-center py-2 rounded-xl border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-200 font-medium">ورود</NuxtLink>
        <NuxtLink @click="isMobileMenuOpen = false" href="/register" class="flex-1 text-center py-2 rounded-xl bg-slate-800 dark:bg-white/10 text-white font-medium">ثبت‌نام</NuxtLink>
      </div>

      <NuxtLink @click="isMobileMenuOpen = false" v-if="user" href="/dashboard" class="px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl text-cyan-600 dark:text-cyan-400 font-medium transition-colors">داشبورد من</NuxtLink>
      <NuxtLink @click="isMobileMenuOpen = false" href="/" class="px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl text-slate-700 dark:text-slate-200 font-medium transition-colors">خانه</NuxtLink>
      <NuxtLink @click="isMobileMenuOpen = false" href="/projects" class="px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl text-slate-700 dark:text-slate-200 font-medium transition-colors">پروژه‌ها</NuxtLink>
      <NuxtLink @click="isMobileMenuOpen = false" href="/blog" class="px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl text-slate-700 dark:text-slate-200 font-medium transition-colors">وبلاگ</NuxtLink>
      <NuxtLink @click="isMobileMenuOpen = false" href="/about" class="px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl text-slate-700 dark:text-slate-200 font-medium transition-colors">درباره من</NuxtLink>
      <NuxtLink @click="isMobileMenuOpen = false" href="/contact" class="mt-2 text-center px-5 py-3 rounded-xl bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-bold shadow-md">دریافت مشاوره</NuxtLink>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { useDark, useToggle } from '@vueuse/core'

const isDark = useDark()
const toggleDark = useToggle(isDark)
const isMobileMenuOpen = ref(false)

// بررسی وضعیت لاگین کاربر با استفاده از کوکی
const user = useCookie('username')
const router = useRouter()

const handleLogout = () => {
  // پاک کردن کوکی‌ها
  const accessToken = useCookie('access_token')
  const refreshToken = useCookie('refresh_token')
  const username = useCookie('username')
  
  accessToken.value = null
  refreshToken.value = null
  username.value = null
  
  isMobileMenuOpen.value = false
  router.push('/login')
}
</script>
