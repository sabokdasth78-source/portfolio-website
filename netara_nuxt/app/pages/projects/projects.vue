<template>
  <div class="space-y-12 pb-20 pt-10">
    <!-- هدر و کانتینر اصلی مشابه صفحه Home -->
    <section class="animate-fade-up p-8 md:p-12 rounded-3xl bg-white/30 dark:bg-slate-800/30 backdrop-blur-xl border border-slate-200/50 dark:border-white/5">
      <div class="text-center mb-16">
        <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-6">پروژه‌های <span class="text-cyan-500">من</span></h1>
        <p class="text-slate-600 dark:text-slate-400 max-w-2xl mx-auto text-lg leading-relaxed">
          در این بخش می‌توانید تمامی پروژه‌ها و نمونه‌کارهای من را با جزئیات کامل مشاهده کنید.
        </p>
      </div>
      
      <!-- وضعیت لودینگ -->
      <div v-if="pending" class="flex justify-center items-center py-20">
        <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-cyan-500 dark:border-cyan-400"></div>
      </div>

      <!-- وضعیت خطا -->
      <div v-else-if="error" class="text-center py-20 text-red-600 dark:text-red-400 bg-red-50 dark:bg-red-900/10 rounded-2xl border border-red-200 dark:border-red-500/20">
        خطا در ارتباط با سرور. لطفاً بک‌اِند را بررسی کنید. ({{ error }})
      </div>
      
      <!-- لیست پروژه‌ها -->
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <ProjectCard 
          v-for="project in projects" 
          :key="project.id" 
          :project="project" 
        />
      </div>
    </section>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()

// 🛠 اصلاح و یکپارچه‌سازی متد فراخوانی API
const { data: projects, pending, error } = await useFetch('/projects/', {
  baseURL: config.public.apiBase,
  transform: (response) => response.results || response
})
</script>
