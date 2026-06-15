<template>
  <div class="space-y-24 pb-20">
    
    <!-- Hero Section & Video Slider -->
    <section class="relative min-h-[85vh] flex items-center bg-white/40 dark:bg-slate-900/40 backdrop-blur-sm rounded-[3rem] p-6 md:p-12 border border-slate-200/50 dark:border-white/5 animate-fade-up overflow-hidden shadow-lg">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center w-full">
        <!-- Text Content -->
        <div class="z-10 space-y-6 md:space-y-8 mt-10 lg:mt-0 text-center lg:text-start">
          <div class="inline-block px-4 py-1.5 rounded-full bg-cyan-100 dark:bg-cyan-900/30 text-cyan-700 dark:text-cyan-300 text-xs md:text-sm font-semibold border border-cyan-200 dark:border-cyan-800/50 shadow-sm animate-pulse">
            {{ t.heroBadge }}
          </div>
          <h1 class="text-3xl sm:text-4xl md:text-6xl lg:text-7xl font-extrabold tracking-tight leading-tight text-slate-900 dark:text-white">
            {{ t.heroTitle1 }} <br />
            <span class="text-transparent bg-clip-text bg-gradient-to-l from-cyan-500 to-purple-600 dark:from-cyan-400 dark:to-purple-500">{{ t.heroTitleHighlight }}</span>
          </h1>
          <p class="text-base md:text-lg lg:text-xl text-slate-600 dark:text-slate-400 max-w-xl leading-relaxed mx-auto lg:mx-0">
            <span v-html="t.heroDesc"></span>
          </p>
          <div class="flex flex-wrap gap-4 justify-center lg:justify-start">
            <NuxtLink to="/projects" class="w-full sm:w-auto text-center px-8 py-3 rounded-full bg-slate-900 text-white dark:bg-white dark:text-slate-900 font-bold hover:bg-slate-800 dark:hover:bg-slate-200 transition-all transform hover:-translate-y-1 shadow-xl hover:shadow-cyan-500/25">
              {{ t.btnPortfolio }}
            </NuxtLink>
            <NuxtLink to="/about" class="w-full sm:w-auto text-center px-8 py-3 rounded-full bg-white/50 dark:bg-slate-900/50 backdrop-blur-md border border-slate-300 dark:border-white/20 text-slate-700 dark:text-white font-bold hover:bg-slate-100 dark:hover:bg-white/10 transition-all transform hover:-translate-y-1 shadow-sm">
              {{ t.btnAbout }}
            </NuxtLink>
          </div>
        </div>

        <!-- Video Slider -->
        <div class="relative w-full h-full min-h-[250px] sm:min-h-[300px] md:min-h-[450px] rounded-[2rem] lg:rounded-[2.5rem] overflow-hidden shadow-2xl border-4 border-white/50 dark:border-slate-800/50">
          <swiper
            :modules="modules"
            :autoplay="{ delay: 4000, disableOnInteraction: false }"
            :pagination="{ clickable: true }"
            :effect="'fade'"
            class="w-full h-full absolute inset-0"
          >
            <swiper-slide v-for="(vid, i) in videoSlides" :key="'vid'+i">
              <video :src="vid" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
            </swiper-slide>
          </swiper>
        </div>
      </div>
    </section>

    <!-- Image Slider Section -->
    <section class="animate-fade-up delay-100 w-screen relative left-1/2 -translate-x-1/2">
      <swiper
        :modules="modules"
        :spaceBetween="0"
        :centeredSlides="true"
        :autoplay="{ delay: 5000, disableOnInteraction: false }"
        :speed="1200"
        :effect="'fade'"
        :pagination="{ clickable: true }"
        :navigation="true"
        class="w-full relative z-0 [&_.swiper-button-next]:hidden md:[&_.swiper-button-next]:flex [&_.swiper-button-prev]:hidden md:[&_.swiper-button-prev]:flex [&_.swiper-pagination]:hidden md:[&_.swiper-pagination]:block"
      >
        <swiper-slide v-for="(img, index) in imageSlides" :key="'img'+index">
          <!-- حذف ارتفاع ثابت و استفاده از w-full h-auto -->
          <NuxtLink :to="img.link" class="flex items-center justify-center w-full relative z-10 cursor-pointer overflow-hidden">
            <!-- تغییر object-cover به w-full و h-auto برای حفظ تناسب عکس -->
            <img :src="img.src" class="w-full h-auto max-h-[85vh] object-contain transition-transform duration-1000 hover:scale-[1.02]" alt="Slider Image" />
          </NuxtLink>
        </swiper-slide>
      </swiper>
    </section>


    <!-- Skills Section -->
    <section class="py-12 md:py-16 relative bg-slate-50/80 dark:bg-slate-950/80 backdrop-blur-md rounded-3xl border border-slate-200 dark:border-white/5 animate-fade-up delay-200 shadow-sm mx-4 md:mx-0">
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-cyan-500/5 dark:via-cyan-500/10 to-transparent blur-3xl -z-10"></div>
      <h2 class="text-2xl sm:text-3xl md:text-4xl font-extrabold mb-8 md:mb-12 text-center text-slate-900 dark:text-white">
        <span class="text-cyan-500">{{ t.skillsTitleHighlight }}</span> {{ t.skillsTitle }}
      </h2>
      
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4 md:gap-6 max-w-6xl mx-auto px-4 md:px-6">
        <div v-for="(skill, i) in translatedSkills" :key="i" 
             class="group relative p-[1px] rounded-2xl bg-gradient-to-b from-slate-200 to-slate-100 dark:from-slate-800 dark:to-slate-800/50 hover:from-cyan-500 hover:to-purple-500 transition-all duration-500 overflow-hidden">
          <div class="relative h-full bg-white/90 dark:bg-slate-900/90 backdrop-blur-xl rounded-2xl p-4 md:p-6 flex flex-col items-center justify-center gap-2 md:gap-3 transition-all duration-500 group-hover:bg-white dark:group-hover:bg-slate-950">
            <div class="w-2.5 h-2.5 md:w-3 md:h-3 rounded-full shadow-[0_0_15px_rgba(0,0,0,0.2)]" :class="skill.color"></div>
            <span class="font-bold text-sm md:text-base text-center text-slate-700 dark:text-slate-200 group-hover:text-cyan-600 dark:group-hover:text-cyan-400 transition-colors">{{ skill.name }}</span>
            <span class="text-[10px] md:text-xs text-slate-500 dark:text-slate-400">{{ skill.level }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Projects Section -->
    <section class="animate-fade-up delay-300 p-6 md:p-8 rounded-3xl bg-white/30 dark:bg-slate-800/30 backdrop-blur-xl border border-slate-200/50 dark:border-white/5 mx-4 md:mx-0">
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-4 mb-8 md:mb-12">
        <div>
          <h2 class="text-2xl sm:text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-2">
            {{ t.projectsTitle }} <span class="text-purple-500">{{ t.projectsHighlight }}</span>
          </h2>
          <p class="text-sm md:text-base text-slate-500 dark:text-slate-400">{{ t.projectsDesc }}</p>
        </div>
        <NuxtLink to="/projects" class="flex text-cyan-600 dark:text-cyan-400 hover:text-cyan-700 dark:hover:text-cyan-300 text-sm font-medium items-center gap-1 group">
          {{ t.viewAll }} 
          <svg class="w-4 h-4 rtl:rotate-180 transform ltr:group-hover:translate-x-1 rtl:group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </NuxtLink>
      </div>
      
      <div v-if="pendingProjects" class="flex justify-center py-10 md:py-20">
        <div class="animate-spin rounded-full h-10 w-10 md:h-12 md:w-12 border-t-2 border-b-2 border-cyan-500 dark:border-cyan-400"></div>
      </div>

      <div v-else-if="errorProjects" class="text-center py-10 md:py-20 text-red-600 dark:text-red-400 bg-red-50 dark:bg-red-900/10 rounded-2xl border border-red-200 dark:border-red-500/20">
        {{ t.errorServer }}
      </div>

      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
        <ProjectCard v-for="project in projects" :key="project.id" :project="project" />
      </div>
    </section>

    <!-- Blog Section -->
    <section class="animate-fade-up delay-400 p-6 md:p-8 rounded-3xl bg-white/30 dark:bg-slate-800/30 backdrop-blur-xl border border-slate-200/50 dark:border-white/5 mx-4 md:mx-0">
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-4 mb-8 md:mb-12">
        <div>
          <h2 class="text-2xl sm:text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-2">
            {{ t.blogTitle }} <span class="text-cyan-500">{{ t.blogHighlight }}</span>
          </h2>
          <p class="text-sm md:text-base text-slate-500 dark:text-slate-400">{{ t.blogDesc }}</p>
        </div>
        <NuxtLink to="/blog" class="flex text-cyan-600 dark:text-cyan-400 hover:text-cyan-700 dark:hover:text-cyan-300 text-sm font-medium items-center gap-1 group">
          {{ t.allArticles }} 
          <svg class="w-4 h-4 rtl:rotate-180 transform ltr:group-hover:translate-x-1 rtl:group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </NuxtLink>
      </div>

      <div v-if="pendingPosts" class="flex justify-center py-10 md:py-20">
        <div class="animate-spin rounded-full h-10 w-10 md:h-12 md:w-12 border-t-2 border-b-2 border-cyan-500 dark:border-cyan-400"></div>
      </div>

      <div v-else-if="errorPosts" class="text-center py-10 md:py-20 text-sm md:text-base text-red-600 dark:text-red-400 bg-red-50 dark:bg-red-900/10 rounded-2xl border border-red-200 dark:border-red-500/20">
        {{ t.errorBlog }}
      </div>

      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
        <div v-for="post in latestPosts" :key="post.id" class="group bg-white/50 dark:bg-slate-900/50 backdrop-blur-md border border-slate-200 dark:border-white/10 rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-2 flex flex-col">
          <NuxtLink :to="`/blog/${post.id}`" class="block h-40 md:h-48 overflow-hidden relative">
            <div class="absolute inset-0 bg-cyan-500/20 group-hover:bg-transparent transition-colors z-10"></div>
            <img v-if="post.image" :src="getMediaUrl(post.image)" :alt="post.title" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
            <div v-else class="w-full h-full bg-slate-200 dark:bg-slate-800 flex items-center justify-center">
              <svg class="w-10 h-10 md:w-12 md:h-12 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
            </div>
          </NuxtLink>
          <div class="p-5 md:p-6 flex flex-col flex-grow">
            <NuxtLink :to="`/blog/${post.id}`">
              <h3 class="text-lg md:text-xl font-bold text-slate-900 dark:text-white mb-2 md:mb-3 group-hover:text-cyan-500 transition-colors line-clamp-2">{{ post.title }}</h3>
            </NuxtLink>
            <p class="text-slate-600 dark:text-slate-400 text-xs md:text-sm leading-relaxed line-clamp-3 mb-4 flex-grow">
              {{ post.content }}
            </p>
            <div class="mt-auto pt-4 border-t border-slate-100 dark:border-slate-800 flex justify-end">
              <NuxtLink :to="`/blog/${post.id}`" class="text-xs md:text-sm font-bold text-cyan-600 dark:text-cyan-400 hover:text-purple-500 flex items-center gap-1 transition-colors">
                {{ t.readMore }}
                <svg class="w-4 h-4 rtl:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Call To Action (CTA) Section -->
    <section class="animate-fade-up delay-500 bg-gradient-to-br from-slate-900 to-slate-800 dark:from-slate-800 dark:to-slate-900 rounded-[2rem] md:rounded-[2.5rem] p-8 md:p-16 text-center text-white shadow-2xl relative overflow-hidden border border-slate-700 dark:border-white/10 group mx-4 md:mx-0">
      <div class="absolute top-0 right-0 w-48 md:w-64 h-48 md:h-64 bg-cyan-500 opacity-20 rounded-full blur-[60px] md:blur-[80px] group-hover:opacity-40 transition-opacity duration-700"></div>
      <div class="absolute bottom-0 left-0 w-48 md:w-64 h-48 md:h-64 bg-purple-600 opacity-20 rounded-full blur-[60px] md:blur-[80px] group-hover:opacity-40 transition-opacity duration-700"></div>
      
      <div class="relative z-10">
        <h2 class="text-2xl sm:text-3xl md:text-5xl font-extrabold mb-4 md:mb-6 tracking-tight">{{ t.ctaTitle }}</h2>
        <p class="text-sm md:text-lg text-slate-300 mb-8 md:mb-10 max-w-2xl mx-auto leading-relaxed">
          {{ t.ctaDesc }}
        </p>
        <NuxtLink to="/contact" class="inline-flex items-center justify-center gap-2 w-full sm:w-auto px-8 py-4 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-bold hover:shadow-[0_0_30px_rgba(6,182,212,0.5)] hover:scale-105 transition-all duration-300">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
          {{ t.ctaBtn }}
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useCookie } from '#app'
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';
import 'swiper/css/effect-fade';
import { Autoplay, Pagination, Navigation, EffectFade } from 'swiper/modules';

const lang = useCookie('lang', { default: () => 'fa' })

const t = computed(() => {
  return lang.value === 'en' ? {
    heroBadge: '🚀 Ready for new projects and exciting challenges',
    heroTitle1: 'Creating',
    heroTitleHighlight: 'Extraordinary Digital Experiences',
    heroDesc: 'I transform complex ideas into beautiful, fast, and user-friendly interfaces using the power of <span class="font-bold text-emerald-500">Django</span> and the elegance of <span class="font-bold text-green-500">Nuxt.js</span>.',
    btnPortfolio: 'View Portfolio',
    btnAbout: 'About Me',
    skillsTitleHighlight: 'My',
    skillsTitle: 'Skills',
    projectsTitle: 'Selected',
    projectsHighlight: 'Projects',
    projectsDesc: 'Some of my recent works that I am proud of.',
    viewAll: 'View All',
    errorServer: 'Error connecting to the server. Please check the backend.',
    blogTitle: 'Latest on the',
    blogHighlight: 'Blog',
    blogDesc: 'Articles on web development, UI design, and my experiences.',
    allArticles: 'All Articles',
    errorBlog: 'Error fetching blog posts.',
    readMore: 'Read More',
    ctaTitle: 'Have a project in mind?',
    ctaDesc: 'Let\'s work together and turn your ideas into reality. I am available for new job opportunities and challenging projects.',
    ctaBtn: 'Start a Conversation',
    levels: {
      adv: 'Advanced',
      pro: 'Professional',
      mid: 'Intermediate',
      basic: 'Familiar'
    }
  } : {
    heroBadge: '🚀 آماده برای پروژه‌های جدید و چالش‌های هیجان‌انگیز',
    heroTitle1: 'خلق تجربه‌های',
    heroTitleHighlight: 'خارق‌العاده دیجیتال',
    heroDesc: 'من ایده‌های پیچیده را به رابط‌های کاربری زیبا، سریع و کاربرپسند با استفاده از قدرت <span class="font-bold text-emerald-500">Django</span> و ظرافت <span class="font-bold text-green-500">Nuxt.js</span> تبدیل می‌کنم.',
    btnPortfolio: 'مشاهده نمونه‌کارها',
    btnAbout: 'درباره من',
    skillsTitleHighlight: 'مهارت‌های',
    skillsTitle: 'من',
    projectsTitle: 'پروژه‌های',
    projectsHighlight: 'منتخب',
    projectsDesc: 'برخی از کارهایی که اخیراً انجام داده‌ام و به آن‌ها افتخار می‌کنم.',
    viewAll: 'مشاهده همه',
    errorServer: 'خطا در ارتباط با سرور. لطفاً بک‌اِند را بررسی کنید.',
    blogTitle: 'جدیدترین‌های',
    blogHighlight: 'وبلاگ',
    blogDesc: 'مقالاتی در زمینه توسعه وب، طراحی رابط کاربری و تجربیات من.',
    allArticles: 'همه مقالات',
    errorBlog: 'خطا در دریافت مقالات وبلاگ.',
    readMore: 'ادامه مطلب',
    ctaTitle: 'پروژه‌ای در ذهن دارید؟',
    ctaDesc: 'بیایید با هم همکاری کنیم و ایده‌های شما را به واقعیت تبدیل کنیم. من برای فرصت‌های شغلی جدید و پروژه‌های چالش‌برانگیز در دسترس هستم.',
    ctaBtn: 'شروع گفتگو',
    levels: {
      adv: 'پیشرفته',
      pro: 'حرفه‌ای',
      mid: 'متوسط',
      basic: 'آشنایی'
    }
  }
})

const modules = [Autoplay, Pagination, Navigation, EffectFade];

const videoSlides = [
  '/vid slider/vid2.mp4',
  '/vid slider/vid1.mp4',
  '/vid slider/vid4.mp4',
  '/vid slider/vid3.mp4'
];

const imageSlides = [
  { src: '/sliders/slider4.webp', link: '/contact' }, 
  { src: '/sliders/slider3.webp', link: '/projects' },          
  { src: '/sliders/slider2.webp', link: '/contact' }, 
  { src: '/sliders/slider1.webp', link: '/projects' }           
];

const config = useRuntimeConfig()

// تولید آرایه مهارت‌ها به صورت داینامیک بر اساس زبان
const translatedSkills = computed(() => [
  { name: 'Vue.js / Nuxt 3', level: t.value.levels.adv, color: 'bg-green-500' },
  { name: 'Django / Python', level: t.value.levels.adv, color: 'bg-emerald-600' },
  { name: 'React.js', level: t.value.levels.pro, color: 'bg-sky-400' },
  { name: 'Next.js', level: t.value.levels.pro, color: 'bg-slate-800 dark:bg-slate-400' },
  { name: 'Tailwind CSS v4', level: t.value.levels.pro, color: 'bg-cyan-400' },
  { name: 'WordPress', level: t.value.levels.adv, color: 'bg-blue-600' },
  { name: 'Graphic Design', level: t.value.levels.pro, color: 'bg-fuchsia-500' },
  { name: 'REST API', level: t.value.levels.adv, color: 'bg-purple-500' },
  { name: 'PostgreSQL', level: t.value.levels.mid, color: 'bg-blue-500' },
  { name: 'Docker', level: t.value.levels.basic, color: 'bg-blue-400' },
  { name: 'Git & GitHub', level: t.value.levels.adv, color: 'bg-orange-500' },
  { name: 'UI/UX Design', level: t.value.levels.mid, color: 'bg-pink-500' },
])

// دریافت پروژه‌ها
const { data: projectsData, pending: pendingProjects, error: errorProjects } = await useFetch('/projects/', {
  baseURL: config.public.apiBase,
  transform: (response) => response.results || response
})
const projects = computed(() => projectsData.value ? projectsData.value.slice(0, 3) : [])

// دریافت مقالات وبلاگ
const { data: postsData, pending: pendingPosts, error: errorPosts } = await useFetch('/blog/posts/', {
  baseURL: config.public.apiBase,
  transform: (response) => response.results || response
})
const latestPosts = computed(() => postsData.value ? postsData.value.slice(0, 3) : [])

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
</script>
