<template>
  <NuxtLink :to="`/projects/${project.id}`" class="block group relative bg-white/80 dark:bg-slate-900/60 backdrop-blur-md rounded-[2rem] border border-slate-200/80 dark:border-white/10 overflow-hidden hover:border-cyan-500/50 dark:hover:border-cyan-500/50 transition-all duration-500 hover:-translate-y-3 hover:shadow-[0_20px_40px_-15px_rgba(6,182,212,0.2)]">
    
    <!-- مدیا (فقط عکس) -->
    <div class="relative h-60 overflow-hidden">
      <!-- تصویر شاخص یا اولین تصویر -->
      <img v-if="thumbnailImage" :src="thumbnailImage" :alt="project.title" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
      
      <!-- اگر عکسی نداشت -->
      <div v-else class="w-full h-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-slate-400 dark:text-slate-500">
        <svg class="w-12 h-12 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
      </div>
      
      <div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 via-slate-900/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex items-end p-6">
        <span class="w-full text-center py-2.5 rounded-xl bg-cyan-500/90 text-white text-sm font-bold backdrop-blur-sm transition-colors transform translate-y-4 group-hover:translate-y-0 duration-500">
          مشاهده جزئیات
        </span>
      </div>
    </div>
    
    <!-- محتوای کارت -->
    <div class="p-6 relative">
      <h3 class="text-xl font-bold text-slate-800 dark:text-white mb-3 group-hover:text-cyan-600 dark:group-hover:text-cyan-400 transition-colors">{{ project.title }}</h3>
      <p class="text-slate-600 dark:text-slate-400 text-sm mb-6 line-clamp-3 leading-relaxed">
        {{ project.description }}
      </p>
      
      <!-- تکنولوژی‌ها -->
      <div class="flex flex-wrap gap-2">
        <span v-for="(tech, index) in (project.technologies || '').split(',')" :key="index" 
              class="px-3 py-1 bg-slate-100 text-slate-700 dark:bg-slate-800 dark:border dark:border-white/5 dark:text-slate-300 text-xs font-medium rounded-lg">
          {{ tech.trim() }}
        </span>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
import { computed } from 'vue'
import { useRuntimeConfig } from '#app'

const props = defineProps({
  project: {
    type: Object,
    required: true
  }
})

const config = useRuntimeConfig()

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

const thumbnailImage = computed(() => {
  if (props.project.images && props.project.images.length > 0) {
    const featured = props.project.images.find(img => img.is_featured)
    const selectedPath = featured ? featured.image : props.project.images[0].image
    return getMediaUrl(selectedPath)
  }
  return null
})
</script>
