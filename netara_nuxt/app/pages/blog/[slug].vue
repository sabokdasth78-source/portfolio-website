<template>
  <div class="space-y-12 pb-20 pt-10">
    
    <!-- وضعیت لودینگ -->
    <div v-if="pending" class="flex justify-center items-center py-20">
      <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-cyan-500 dark:border-cyan-400"></div>
    </div>

    <!-- وضعیت خطا -->
    <div v-else-if="error || !post" class="text-center py-20 text-red-600 dark:text-red-400 bg-red-50 dark:bg-red-900/10 rounded-2xl border border-red-200 dark:border-red-500/20">
      {{ t.notFound }}
      <br />
      <NuxtLink to="/blog" class="text-cyan-500 underline mt-4 inline-block">{{ t.backToBlog }}</NuxtLink>
    </div>

    <!-- محتوای اصلی مقاله -->
    <div v-else class="animate-fade-up max-w-4xl mx-auto">
      
      <!-- دکمه بازگشت -->
      <NuxtLink to="/blog" class="inline-flex items-center gap-2 text-slate-500 hover:text-cyan-500 dark:text-slate-400 dark:hover:text-cyan-400 mb-8 transition-colors font-medium">
        <svg class="w-5 h-5 rtl:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
        {{ t.backToArticles }}
      </NuxtLink>

      <article class="bg-white/30 dark:bg-slate-800/30 backdrop-blur-xl border border-slate-200/50 dark:border-white/5 rounded-[3rem] p-8 md:p-12 shadow-lg mb-12">
        
        <!-- تصویر شاخص مقاله -->
        <div v-if="imageUrl" class="w-full h-[300px] md:h-[450px] rounded-[2rem] overflow-hidden mb-10 shadow-xl relative group border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-slate-900">
          <img :src="imageUrl" :alt="post.title" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
        </div>

        <!-- عنوان مقاله -->
        <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-8 leading-tight">
          {{ post.title }}
        </h1>

        <!-- محتوای متن -->
        <div 
          class="prose prose-lg prose-slate dark:prose-invert max-w-none text-slate-700 dark:text-slate-300 leading-loose"
          v-html="post.content"
        >
        </div>

      </article>

      <!-- Call To Action (CTA) Section مخصوص مقاله -->
      <section class="bg-gradient-to-br from-slate-900 to-slate-800 dark:from-slate-800 dark:to-slate-900 rounded-[2.5rem] p-10 md:p-16 text-center text-white shadow-2xl relative overflow-hidden border border-slate-700 dark:border-white/10 group mt-12">
        <div class="absolute top-0 right-0 w-64 h-64 bg-cyan-500 opacity-20 rounded-full blur-[80px] group-hover:opacity-40 transition-opacity duration-700"></div>
        <div class="absolute bottom-0 left-0 w-64 h-64 bg-purple-600 opacity-20 rounded-full blur-[80px] group-hover:opacity-40 transition-opacity duration-700"></div>
        
        <div class="relative z-10">
          <h2 class="text-3xl md:text-5xl font-extrabold mb-6 tracking-tight">{{ t.ctaTitle }}</h2>
          <p class="text-slate-300 mb-10 max-w-2xl mx-auto text-lg leading-relaxed">
            {{ t.ctaDesc }}
          </p>
          <NuxtLink to="/contact" class="inline-flex items-center gap-2 px-8 py-4 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-bold hover:shadow-[0_0_30px_rgba(6,182,212,0.5)] hover:scale-105 transition-all duration-300">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
            {{ t.ctaButton }}
          </NuxtLink>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRuntimeConfig, useCookie, useFetch } from '#app'

const route = useRoute()
const config = useRuntimeConfig()
const lang = useCookie('lang', { default: () => 'fa' })

// دیکشنری دو زبانه
const t = computed(() => {
  return lang.value === 'en' ? {
    notFound: 'Article not found or an error occurred.',
    backToBlog: 'Back to Blog',
    backToArticles: 'Back to Articles List',
    ctaTitle: 'Need a professional website?',
    ctaDesc: 'I hope you enjoyed reading this article. If you are looking to design or develop a modern and fast website for your business, let\'s talk.',
    ctaButton: 'Contact & Order Project'
  } : {
    notFound: 'مقاله یافت نشد یا خطایی رخ داده است.',
    backToBlog: 'بازگشت به وبلاگ',
    backToArticles: 'بازگشت به لیست مقالات',
    ctaTitle: 'به یک سایت حرفه‌ای نیاز دارید؟',
    ctaDesc: 'امیدوارم از خواندن این مقاله لذت برده باشید. اگر به دنبال طراحی یا توسعه یک وب‌سایت مدرن و سریع برای کسب‌وکار خود هستید، بیایید با هم گفتگو کنیم.',
    ctaButton: 'ارتباط و سفارش پروژه'
  }
})

// فراخوانی جزئیات مقاله از بک‌اند بدون انکود اضافی
const { data: post, pending, error } = await useFetch(`/blog/posts/${route.params.slug}/`, {
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

// استخراج عکس مقاله
const imageUrl = computed(() => {
  if (post.value && post.value.image) {
    return getMediaUrl(post.value.image)
  }
  return null
})
</script>
