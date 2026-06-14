<template>
  <div class="container mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-center mb-10 dark:text-white">{{ t.title }}</h1>

    <div v-if="pending" class="text-center">{{ t.loading }}</div>
    <div v-else-if="error" class="text-red-500 text-center">{{ t.error }}</div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <NuxtLink 
        v-for="post in posts" 
        :key="post.id" 
        :to="`/blog/${post.slug}`"
        class="bg-white dark:bg-slate-800 rounded-2xl shadow-lg overflow-hidden hover:-translate-y-2 transition-transform duration-300"
      >
        <img v-if="post.image" :src="post.image" :alt="post.title" class="w-full h-48 object-cover">
        <div class="p-6">
          <h2 class="text-xl font-bold mb-3 dark:text-white">{{ post.title }}</h2>
          <!-- تگ‌های HTML و کاراکترهای اضافی در اینجا حذف می‌شوند -->
          <p class="text-slate-500 dark:text-slate-400 line-clamp-3">
            {{ post.content.replace(/<[^>]+>/g, '').replace(/&zwnj;/g, ' ').replace(/&nbsp;/g, ' ') }}
          </p>
        </div>
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRuntimeConfig, useCookie, useFetch } from '#app'

const config = useRuntimeConfig()
const lang = useCookie('lang', { default: () => 'fa' })

// دیکشنری دو زبانه
const t = computed(() => {
  return lang.value === 'en' ? {
    title: 'Blog',
    loading: 'Loading...',
    error: 'Error fetching data'
  } : {
    title: 'وبلاگ',
    loading: 'در حال بارگذاری...',
    error: 'خطا در دریافت اطلاعات'
  }
})

const { data: posts, pending, error } = await useFetch('/blog/posts/', {
  baseURL: config.public.apiBase
})
</script>
