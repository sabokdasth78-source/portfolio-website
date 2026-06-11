<template>
  <div class="space-y-12 pb-20 pt-10">
    
    <!-- وضعیت لودینگ -->
    <div v-if="pending" class="flex justify-center items-center py-20">
      <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-cyan-500 dark:border-cyan-400"></div>
    </div>

    <!-- وضعیت خطا -->
    <div v-else-if="error || !project" class="text-center py-20 text-red-600 dark:text-red-400 bg-red-50 dark:bg-red-900/10 rounded-2xl border border-red-200 dark:border-red-500/20">
      پروژه یافت نشد یا خطایی رخ داده است.
      <br />
      <NuxtLink to="/projects" class="text-cyan-500 underline mt-4 inline-block">بازگشت به پروژه‌ها</NuxtLink>
    </div>

    <!-- محتوای اصلی پروژه -->
    <div v-else class="animate-fade-up">
      <!-- دکمه بازگشت -->
      <NuxtLink to="/projects" class="inline-flex items-center gap-2 text-slate-500 hover:text-cyan-500 dark:text-slate-400 dark:hover:text-cyan-400 mb-8 transition-colors">
        <svg class="w-5 h-5 rtl:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
        بازگشت به لیست پروژه‌ها
      </NuxtLink>

      <div class="bg-white/30 dark:bg-slate-800/30 backdrop-blur-xl border border-slate-200/50 dark:border-white/5 rounded-[3rem] p-8 md:p-12 shadow-lg mb-12">
        
        <!-- عنوان و تکنولوژی‌ها -->
        <div class="mb-10 text-center">
          <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-6">{{ project.title }}</h1>
          <div class="flex flex-wrap justify-center gap-3">
            <span v-for="(tech, index) in (project.technologies || '').split(',')" :key="index" 
                  class="px-4 py-2 bg-slate-100 text-slate-700 dark:bg-slate-900 dark:border dark:border-white/10 dark:text-slate-300 text-sm font-semibold rounded-xl">
              {{ tech.trim() }}
            </span>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          
          <!-- بخش مدیا (عکس دراز + ویدیو) : عرض بیشتر (8 ستون) -->
          <div class="lg:col-span-8 space-y-8">
            
            <!-- تصویر Mockup کامل (دراز) -->
            <div v-if="mockupUrl" class="w-full rounded-[2rem] overflow-hidden border border-slate-200 dark:border-slate-700 shadow-xl bg-slate-50 dark:bg-slate-900/50 p-2 md:p-4">
              <img :src="mockupUrl" class="w-full h-auto rounded-xl object-top" :alt="project.title" />
            </div>

            <!-- ویدیو -->
            <div v-if="videoUrl" class="w-full rounded-[2rem] overflow-hidden border-2 border-slate-200 dark:border-slate-700 shadow-xl bg-black">
              <video controls class="w-full h-auto object-contain">
                <source :src="videoUrl" type="video/mp4">
                مرورگر شما از پخش ویدیو پشتیبانی نمی‌کند.
              </video>
            </div>

          </div>

          <!-- بخش توضیحات و لینک‌ها (استیکی در کنار صفحه) : عرض کمتر (4 ستون) -->
          <div class="lg:col-span-4 space-y-8 relative">
            <div class="sticky top-24">
              <div class="prose prose-slate dark:prose-invert max-w-none bg-slate-50 dark:bg-slate-800/50 p-6 rounded-2xl border border-slate-100 dark:border-slate-700">
                <h3 class="text-2xl font-bold text-slate-800 dark:text-white mb-4">درباره پروژه</h3>
                <p class="text-slate-600 dark:text-slate-300 leading-relaxed text-lg whitespace-pre-line">
                  {{ project.description }}
                </p>
              </div>

              <!-- دکمه‌های لینک -->
              <div class="flex flex-col gap-4 mt-8">
                <a v-if="project.live_link" :href="project.live_link" target="_blank" class="w-full py-4 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-bold text-center hover:shadow-[0_0_20px_rgba(6,182,212,0.4)] hover:-translate-y-1 transition-all duration-300 flex items-center justify-center gap-2">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                  مشاهده آنلاین سایت
                </a>
                
                <a v-if="project.github_link" :href="project.github_link" target="_blank" class="w-full py-4 rounded-xl bg-slate-900 text-white dark:bg-white dark:text-slate-900 font-bold text-center hover:shadow-lg hover:-translate-y-1 transition-all duration-300 flex items-center justify-center gap-2">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                  سورس کد
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Call To Action (CTA) Section -->
      <section class="bg-gradient-to-br from-slate-900 to-slate-800 dark:from-slate-800 dark:to-slate-900 rounded-[2.5rem] p-10 md:p-16 text-center text-white shadow-2xl relative overflow-hidden border border-slate-700 dark:border-white/10 group mt-12">
        <div class="absolute top-0 right-0 w-64 h-64 bg-cyan-500 opacity-20 rounded-full blur-[80px] group-hover:opacity-40 transition-opacity duration-700"></div>
        <div class="absolute bottom-0 left-0 w-64 h-64 bg-purple-600 opacity-20 rounded-full blur-[80px] group-hover:opacity-40 transition-opacity duration-700"></div>
        
        <div class="relative z-10">
          <h2 class="text-3xl md:text-5xl font-extrabold mb-6 tracking-tight">پروژه‌ای مشابه نیاز دارید؟</h2>
          <p class="text-slate-300 mb-10 max-w-2xl mx-auto text-lg leading-relaxed">
            اگر از این پروژه خوشتان آمده و ایده‌ای برای کسب‌وکار خود دارید، خوشحال می‌شوم در اجرای آن به شما کمک کنم.
          </p>
          <NuxtLink to="/contact" class="inline-flex items-center gap-2 px-8 py-4 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-bold hover:shadow-[0_0_30px_rgba(6,182,212,0.5)] hover:scale-105 transition-all duration-300">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
            ارتباط و سفارش پروژه
          </NuxtLink>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRuntimeConfig } from '#app'

const route = useRoute()
const config = useRuntimeConfig()

const { data: project, pending, error } = await useFetch(`/projects/${route.params.id}/`, {
  baseURL: config.public.apiBase
})

const getMediaUrl = (path) => {
  if (!path) return null
  try {
    if (path.startsWith('http')) {
      const urlObj = new URL(path)
      return `${config.public.apiBaseHost}${urlObj.pathname}`
    }
    return `${config.public.apiBaseHost}${path}`
  } catch (e) {
    return path
  }
}

// استخراج عکس Mockup (دراز)
const mockupUrl = computed(() => {
  if (project.value && project.value.mockup_image) {
    return getMediaUrl(project.value.mockup_image)
  }
  return null
})

// استخراج ویدیو
const videoUrl = computed(() => {
  if (project.value && project.value.video) {
    return getMediaUrl(project.value.video)
  }
  return null
})
</script>
