<template>
  <div class="bg-[#0C0C0C] min-h-screen text-[#D7E2EA] overflow-x-clip selection:bg-purple-500/30 w-full" 
       :class="lang === 'fa' ? 'font-sans' : 'font-kanit'"
       :dir="lang === 'fa' ? 'rtl' : 'ltr'">
    
    <!-- 1. HERO SECTION -->
    <section class="relative h-screen flex flex-col justify-between overflow-x-clip pt-6 md:pt-8 px-6 md:px-10 pb-7 sm:pb-8 md:pb-10">
      
      <!-- Navbar -->
      <nav class="reveal flex flex-wrap justify-between items-center w-full z-50 gap-4 relative">
        
        <!-- دکمه منوی همبرگری (موبایل) -->
        <button @click="isMenuOpen = !isMenuOpen" class="md:hidden p-1 text-white hover:opacity-70 transition-opacity z-50">
          <svg v-if="!isMenuOpen" class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
          <svg v-else class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>

        <!-- لینک‌های مسیر (دسکتاپ) -->
        <div class="hidden md:flex gap-4 sm:gap-6 text-sm md:text-lg lg:text-[1.2rem] font-medium uppercase tracking-wider items-center">
          <NuxtLink to="/about" class="hover:opacity-70 transition-opacity">{{ t.nav.about }}</NuxtLink>
          <NuxtLink to="/services" class="hover:opacity-70 transition-opacity">{{ t.nav.services }}</NuxtLink>
          <NuxtLink to="/projects" class="hover:opacity-70 transition-opacity">{{ t.nav.projects }}</NuxtLink>
          <NuxtLink to="/blog" class="hover:opacity-70 transition-opacity">{{ t.nav.blog }}</NuxtLink>
        </div>

        <!-- منوی کشویی موبایل -->
        <div v-if="isMenuOpen" class="absolute top-12 left-0 w-full bg-[#151515] border border-white/10 rounded-2xl p-4 flex flex-col gap-4 md:hidden shadow-2xl z-40">
          <NuxtLink @click="isMenuOpen = false" to="/about" class="text-base font-medium">{{ t.nav.about }}</NuxtLink>
          <hr class="border-white/5" />
          <NuxtLink @click="isMenuOpen = false" to="/services" class="text-base font-medium">{{ t.nav.services }}</NuxtLink>
          <hr class="border-white/5" />
          <NuxtLink @click="isMenuOpen = false" to="/projects" class="text-base font-medium">{{ t.nav.projects }}</NuxtLink>
          <hr class="border-white/5" />
          <NuxtLink @click="isMenuOpen = false" to="/blog" class="text-base font-medium">{{ t.nav.blog }}</NuxtLink>
        </div>
        
        <!-- دکمه‌های ورود، ثبت‌نام، مشاوره و زبان -->
        <div class="flex items-center gap-2 sm:gap-3 text-xs sm:text-sm font-medium z-50">
          <NuxtLink to="/login" class="hover:opacity-70 transition-opacity px-2">{{ t.nav.login }}</NuxtLink>
          <NuxtLink to="/register" class="px-3 py-1.5 sm:px-4 sm:py-2 rounded-full border border-white/20 hover:bg-white/10 transition-colors">{{ t.nav.register }}</NuxtLink>
          <NuxtLink to="/contact" class="hidden sm:inline-flex px-4 py-2 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white">{{ t.nav.consult }}</NuxtLink>
          <button @click="toggleLang" class="w-8 h-8 sm:w-10 sm:h-10 flex items-center justify-center rounded-full border border-white/20 hover:bg-white/10 transition-colors">
            {{ t.nav.lang }}
          </button>
        </div>
      </nav>

      <!-- Center Portrait (Magnet Effect & Avatar) -->
      <div class="absolute top-1/2 sm:top-auto sm:bottom-0 left-1/2 -translate-x-1/2 -translate-y-1/2 sm:translate-y-0 z-10 w-[280px] sm:w-[360px] md:w-[440px] lg:w-[520px]"
           ref="magnetEl" @mousemove="onMouseMove" @mouseleave="onMouseLeave">
        <img src="/avatar.webp" 
             alt="Happy Portrait" 
             class="w-full h-auto object-contain reveal delay-500 drop-shadow-[0_0_30px_rgba(255,255,255,0.05)] pointer-events-none" />
      </div>

      <!-- Hero Heading -->
      <div class="absolute top-[40%] sm:top-1/2 left-0 w-full -translate-y-1/2 sm:-translate-y-[60%] z-0 flex justify-center mt-6 sm:mt-4 md:-mt-5">
        <!-- کلاس whitespace-nowrap برای موبایل حذف شد تا متن مخفی نشود -->
        <h1 class="reveal delay-200 hero-heading font-black uppercase tracking-tight text-[12vw] sm:text-[8vw] md:text-[8.5vw] lg:text-[9vw] text-center px-4 sm:px-0 sm:whitespace-nowrap" 
            :class="lang === 'fa' ? 'leading-tight pb-2' : 'leading-none'"
            :dir="lang === 'fa' ? 'rtl' : 'ltr'">
          {{ t.greeting }}
        </h1>
      </div>

      <!-- Bottom Bar -->
      <div class="reveal delay-300 flex justify-between items-end z-20 w-full">
        <p class="font-light uppercase tracking-wide leading-snug text-[clamp(0.75rem,1.4vw,1.5rem)] max-w-[160px] sm:max-w-[220px] md:max-w-[260px]">
          {{ t.heroDescShort }}
        </p>
        
        <NuxtLink to="/contact" class="contact-btn px-8 py-3 sm:px-10 sm:py-3.5 md:px-12 md:py-4 rounded-full text-white font-medium uppercase tracking-widest text-xs sm:text-sm md:text-base transition-transform hover:scale-105 active:scale-95">
          {{ t.ctaBtn }}
        </NuxtLink>
      </div>
    </section>

    <!-- 2. MARQUEE SECTION -->
    <section ref="marqueeSec" class="pt-24 sm:pt-32 md:pt-40 pb-10 overflow-hidden bg-[#0C0C0C]">
      <div class="flex flex-col gap-3" dir="ltr">
        <div class="flex gap-3 w-max will-change-transform" :style="{ transform: `translateX(${marqueeOffset - 200}px)` }">
          <img v-for="i in 10" :key="'r1'+i" :src="gifs[i % gifs.length]" class="w-[300px] h-[200px] sm:w-[420px] sm:h-[270px] rounded-2xl object-cover" />
        </div>
        <div class="flex gap-3 w-max will-change-transform" :style="{ transform: `translateX(${-(marqueeOffset - 200)}px)` }">
          <img v-for="i in 10" :key="'r2'+i" :src="gifs[(i+5) % gifs.length]" class="w-[300px] h-[200px] sm:w-[420px] sm:h-[270px] rounded-2xl object-cover" />
        </div>
      </div>
    </section>

    <!-- 3. ABOUT SECTION -->
    <section class="relative min-h-screen flex flex-col items-center justify-center px-5 sm:px-8 md:px-10 py-20 overflow-hidden">
      <!-- Decorative Images -->
      <img src="https://shrug-person-78902957.figma.site/_components/v2/ebb2b8f25d8e24d5f0a5ca8af4c950de81aa2fd7/moon_icon.11395d36.png" class="reveal delay-100 absolute top-[4%] left-[1%] sm:left-[2%] md:left-[4%] w-[120px] sm:w-[160px] md:w-[210px] opacity-70" />
      <img src="https://shrug-person-78902957.figma.site/_components/v2/ebb2b8f25d8e24d5f0a5ca8af4c950de81aa2fd7/p59_1.4659672e.png" class="reveal delay-200 absolute bottom-[8%] left-[3%] sm:left-[6%] md:left-[10%] w-[100px] sm:w-[140px] md:w-[180px] opacity-70" />
      <img src="https://shrug-person-78902957.figma.site/_components/v2/ebb2b8f25d8e24d5f0a5ca8af4c950de81aa2fd7/lego_icon-1.703bb594.png" class="reveal delay-300 absolute top-[4%] right-[1%] sm:right-[2%] md:right-[4%] w-[120px] sm:w-[160px] md:w-[210px] opacity-70" />
      <img src="https://shrug-person-78902957.figma.site/_components/v2/ebb2b8f25d8e24d5f0a5ca8af4c950de81aa2fd7/Group_134-1.2e04f3ce.png" class="reveal delay-400 absolute bottom-[8%] right-[3%] sm:right-[6%] md:right-[10%] w-[130px] sm:w-[170px] md:w-[220px] opacity-70" />

      <h2 class="reveal hero-heading font-black uppercase tracking-tight text-center text-[clamp(3rem,12vw,160px)] mb-10 sm:mb-14 md:mb-16" 
          :class="lang === 'fa' ? 'leading-tight pb-3' : 'leading-none'"
          :dir="lang === 'fa' ? 'rtl' : 'ltr'">
        {{ t.aboutHeading }}
      </h2>
      
      <p class="reveal delay-200 font-medium text-center leading-relaxed max-w-[560px] text-[clamp(1rem,2vw,1.35rem)] text-[#D7E2EA] opacity-80 mb-16 sm:mb-20 md:mb-24 px-4">
        <span v-html="t.heroDesc"></span>
      </p>

      <NuxtLink to="/contact" class="reveal delay-300 contact-btn px-8 py-3 sm:px-10 sm:py-3.5 md:px-12 md:py-4 rounded-full text-white font-medium uppercase tracking-widest text-xs sm:text-sm md:text-base transition-transform hover:scale-105 active:scale-95">
        {{ t.letsTalkBtn }}
      </NuxtLink>
    </section>

    <!-- 4. SERVICES SECTION -->
    <section class="bg-white text-[#0C0C0C] rounded-t-[40px] sm:rounded-t-[50px] md:rounded-t-[60px] px-5 sm:px-8 md:px-10 py-20 sm:py-24 md:py-32 relative z-10 mt-10">
      <h2 class="reveal font-black uppercase text-center text-[clamp(3rem,12vw,160px)] mb-16 sm:mb-20 md:mb-28 tracking-tight" 
          :class="lang === 'fa' ? 'leading-tight pb-3' : 'leading-none'"
          :dir="lang === 'fa' ? 'rtl' : 'ltr'">
        {{ t.servicesHeading }}
      </h2>

      <div class="max-w-5xl mx-auto flex flex-col">
        <div v-for="(service, i) in translatedServices" :key="i" 
             class="reveal border-b border-[#0C0C0C]/15 py-8 sm:py-10 md:py-12 flex flex-col md:flex-row md:items-center gap-6 md:gap-12 group hover:bg-slate-50 transition-colors px-4 rounded-xl"
             :style="{ transitionDelay: `${i * 100}ms` }">
          <div class="font-black text-[clamp(3rem,10vw,140px)] text-[#0C0C0C]/20 group-hover:text-[#0C0C0C] transition-colors leading-none w-32" dir="ltr">
            0{{ i + 1 }}
          </div>
          <div class="flex-1">
            <h3 class="font-medium uppercase text-[clamp(1rem,2.2vw,2.1rem)] mb-2">{{ service.title }}</h3>
            <p class="font-light leading-relaxed text-[clamp(0.85rem,1.6vw,1.25rem)] opacity-60 max-w-2xl">
              {{ service.desc }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. PROJECTS SECTION -->
    <section class="bg-[#0C0C0C] rounded-t-[40px] sm:rounded-t-[50px] md:rounded-t-[60px] -mt-10 sm:-mt-12 md:-mt-14 relative z-20 px-5 sm:px-8 md:px-10 py-20 pb-0">
      <h2 class="reveal hero-heading font-black uppercase text-center text-[clamp(3rem,12vw,160px)] mb-20 tracking-tight" 
          :class="lang === 'fa' ? 'leading-tight pb-3' : 'leading-none'"
          :dir="lang === 'fa' ? 'rtl' : 'ltr'">
        {{ t.projectsHeading }}
      </h2>

      <div class="max-w-6xl mx-auto relative pb-20">
        <div v-if="pendingProjects" class="flex justify-center py-20">
          <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#D7E2EA]"></div>
        </div>
        
        <div v-else class="flex flex-col space-y-10">
          <div v-for="(project, idx) in projects" :key="project.id" 
               class="sticky top-24 md:top-32 bg-[#0C0C0C] border-2 border-[#D7E2EA] rounded-[40px] sm:rounded-[50px] md:rounded-[60px] p-4 sm:p-6 md:p-8 flex flex-col gap-6 shadow-2xl"
               :style="{ top: `${80 + (idx * 20)}px` }">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
              <div class="flex items-center gap-4 sm:gap-6">
                <span class="font-black text-5xl md:text-7xl text-[#D7E2EA]/30" dir="ltr">0{{ idx + 1 }}</span>
                <div>
                  <span class="text-xs sm:text-sm font-medium opacity-50 uppercase tracking-widest">{{ t.projectsHighlight }}</span>
                  <h3 class="text-xl sm:text-3xl md:text-4xl font-bold uppercase mt-1">{{ project.title }}</h3>
                </div>
              </div>
              <NuxtLink :to="`/projects/${project.id}`" class="live-project-btn px-8 py-3 sm:px-10 sm:py-3.5 rounded-full border-2 border-[#D7E2EA] text-[#D7E2EA] font-medium uppercase tracking-widest text-sm sm:text-base hover:bg-[#D7E2EA]/10 transition-colors whitespace-nowrap">
                {{ t.liveProjectBtn }}
              </NuxtLink>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-5 gap-4">
              <div class="md:col-span-2 flex flex-col gap-4">
                <div class="h-[clamp(130px,16vw,230px)] rounded-[30px] sm:rounded-[40px] bg-slate-800 overflow-hidden relative group">
                  <div class="absolute inset-0 bg-[#0C0C0C]/20 group-hover:bg-transparent transition-colors z-10"></div>
                  <img v-if="project.mockup_image || (project.images && project.images.length > 0)" 
                       :src="getMediaUrl(project.mockup_image || project.images[0].image)" 
                       class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <div class="h-[clamp(160px,22vw,340px)] rounded-[30px] sm:rounded-[40px] bg-slate-800 overflow-hidden relative group">
                  <div class="absolute inset-0 bg-[#0C0C0C]/20 group-hover:bg-transparent transition-colors z-10"></div>
                  <img v-if="project.mockup_image || (project.images && project.images.length > 0)" 
                       :src="getMediaUrl(project.mockup_image || project.images[0].image)" 
                       class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
              </div>
              <div class="md:col-span-3 h-full min-h-[300px] rounded-[30px] sm:rounded-[40px] sm:rounded-[50px] bg-slate-800 overflow-hidden relative group">
                <div class="absolute inset-0 bg-[#0C0C0C]/20 group-hover:bg-transparent transition-colors z-10"></div>
                <img v-if="project.mockup_image || (project.images && project.images.length > 0)" 
                     :src="getMediaUrl(project.mockup_image || project.images[0].image)" 
                     class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. FOOTER SECTION -->
    <footer class="mt-10 border-t border-[#D7E2EA]/10 bg-[#0C0C0C] relative z-20">
      <div class="container mx-auto px-6 py-12" :dir="lang === 'en' ? 'ltr' : 'rtl'">
        <div class="grid grid-cols-1 md:grid-cols-12 gap-10 mb-12">
          <div class="md:col-span-5 space-y-6">
            <NuxtLink href="/" class="flex items-center gap-3">
              <img src="/logo.png" alt="لوگو" class="h-12 w-12 object-contain drop-shadow-sm" />
              <span class="text-2xl font-black tracking-tighter text-[#D7E2EA]">
                {{ t.footer.logoPart1 }}<span class="text-cyan-500">{{ t.footer.logoPart2 }}</span>
              </span>
            </NuxtLink>
            <p class="text-[#D7E2EA]/70 text-sm leading-relaxed max-w-sm">{{ t.footer.description }}</p>
          </div>
          <div class="md:col-span-3 space-y-4">
            <h3 class="text-lg font-bold text-[#D7E2EA]">{{ t.footer.quickLinksTitle }}</h3>
            <ul class="space-y-3">
              <li><NuxtLink href="/" class="text-[#D7E2EA]/70 hover:text-cyan-400 transition-colors text-sm">{{ t.footer.linkHome }}</NuxtLink></li>
              <li><NuxtLink href="/projects" class="text-[#D7E2EA]/70 hover:text-cyan-400 transition-colors text-sm">{{ t.footer.linkProjects }}</NuxtLink></li>
              <li><NuxtLink href="/blog" class="text-[#D7E2EA]/70 hover:text-cyan-400 transition-colors text-sm">{{ t.footer.linkBlog }}</NuxtLink></li>
              <li><NuxtLink href="/about" class="text-[#D7E2EA]/70 hover:text-cyan-400 transition-colors text-sm">{{ t.footer.linkAbout }}</NuxtLink></li>
            </ul>
          </div>
          <div class="md:col-span-4 space-y-4">
            <h3 class="text-lg font-bold text-[#D7E2EA]">{{ t.footer.contactTitle }}</h3>
            <ul class="space-y-3">
              <li class="flex items-center gap-2 text-[#D7E2EA]/70 text-sm">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                <a href="mailto:sabokdasth78@gmail.com" class="hover:text-cyan-400 transition-colors">sabokdasth78@gmail.com</a>
              </li>
              <li class="flex items-center gap-2 text-[#D7E2EA]/70 text-sm">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                {{ t.footer.location }}
              </li>
            </ul>
            <div class="flex gap-4 pt-2">
              <a href="https://github.com/sabokdasth78-source" target="_blank" rel="noopener noreferrer" class="p-2 rounded-full bg-white/5 text-[#D7E2EA]/70 hover:bg-white/10 hover:text-cyan-400 transition-all">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
              </a>
              <a href="https://www.linkedin.com/in/hengame-sabokdast-198662414" target="_blank" rel="noopener noreferrer" class="p-2 rounded-full bg-white/5 text-[#D7E2EA]/70 hover:bg-white/10 hover:text-cyan-400 transition-all">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
              </a>
            </div>
          </div>
        </div>
        <div class="border-t border-[#D7E2EA]/10 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p class="text-[#D7E2EA]/60 text-sm">{{ t.footer.copyright }}</p>
          <p class="text-[#D7E2EA]/60 text-sm flex items-center gap-1">{{ t.footer.developedBy }} <span class="text-red-500 animate-pulse">❤</span></p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed, ref, onMounted, onUnmounted } from 'vue'
import { useCookie, useRuntimeConfig } from '#app'

const config = useRuntimeConfig()
const lang = useCookie('lang', { default: () => 'fa' })
const isMenuOpen = ref(false) // اضافه کردن متغیر برای مدیریت منوی موبایل

// تابع تغییر زبان
const toggleLang = () => {
  lang.value = lang.value === 'fa' ? 'en' : 'fa'
}

// --- All Translations ---
const t = computed(() => {
  const isEn = lang.value === 'en'
  return {
    nav: {
      about: isEn ? 'About' : 'درباره من',
      services: isEn ? 'Services' : 'خدمات',
      projects: isEn ? 'Projects' : 'پروژه‌ها',
      contact: isEn ? 'Contact' : 'ارتباط با من',
      blog: isEn ? 'Blog' : 'وبلاگ',
      login: isEn ? 'Login' : 'ورود',
      register: isEn ? 'Register' : 'ثبت‌نام',
      consult: isEn ? 'Consultation' : 'دریافت مشاوره',
      lang: isEn ? 'FA' : 'EN'
    },
    greeting: isEn ? "Hi, I'm Hengame" : "سلام، من هنگامه هستم",
    heroDescShort: isEn ? 'A Web Creator driven by crafting striking and unforgettable interfaces' : 'توسعه‌دهنده وب، متمرکز بر خلق رابط‌های کاربری چشم‌گیر و فراموش‌نشدنی',
    ctaBtn: isEn ? 'Contact Me' : 'تماس با من',
    aboutHeading: isEn ? 'About Me' : 'درباره من',
    heroDesc: isEn ? "With more than years of experience in development, I focus on web design, and user experience. Let's build something incredible together!" : "با سال‌ها تجربه در زمینه توسعه، تمرکز من بر طراحی وب و تجربه کاربری است. من واقعاً از همکاری با کسب‌وکارهایی که می‌خواهند متمایز باشند و بهترین تصویر خود را ارائه دهند لذت می‌برم.",
    letsTalkBtn: isEn ? "Let's Talk" : "شروع گفتگو",
    servicesHeading: isEn ? 'Services' : 'خدمـات',
    projectsHeading: isEn ? 'Projects' : 'پروژه‌ها',
    projectsHighlight: isEn ? 'Selected Work' : 'پروژه منتخب',
    liveProjectBtn: isEn ? 'Live Project' : 'مشاهده آنلاین',
    footer: isEn ? {
      logoPart1: 'Net',
      logoPart2: 'Ara',
      description: 'Full-stack developer focused on creating modern, fast, and functional user experiences. Ready to turn your ideas into clean code and scalable products.',
      quickLinksTitle: 'Quick Links',
      linkHome: 'Home',
      linkProjects: 'My Projects',
      linkBlog: 'Blog & Articles',
      linkAbout: 'About Me & Resume',
      contactTitle: 'Contact Me',
      location: 'Tehran, Iran',
      copyright: '© 2026 All rights reserved.',
      developedBy: 'Designed and developed with'
    } : {
      logoPart1: 'نت',
      logoPart2: ' آرا ',
      description: 'توسعه‌دهنده فول‌استک با تمرکز بر خلق تجربه‌های کاربری مدرن، سریع و کاربردی. آماده برای تبدیل ایده‌های شما به کدهای تمیز و محصولات مقیاس‌پذیر.',
      quickLinksTitle: 'لینک‌های سریع',
      linkHome: 'صفحه اصلی',
      linkProjects: 'پروژه‌های من',
      linkBlog: 'وبلاگ و مقالات',
      linkAbout: 'درباره من و رزومه',
      contactTitle: 'ارتباط با من',
      location: 'تهران، ایران',
      copyright: '© ۱۴۰۵ تمامی حقوق محفوظ است.',
      developedBy: 'طراحی و توسعه با'
    }
  }
})

const translatedServices = computed(() => {
  const isEn = lang.value === 'en'
  return [
    { title: isEn ? 'Web App Development' : 'توسعه وب‌اپلیکیشن', desc: isEn ? 'Creation of detailed applications tailored to specific client needs.' : 'طراحی سامانه‌های اختصاصی و برنامه‌های پیچیده تحت وب متناسب با نیاز شما.' },
    { title: isEn ? 'Corporate & E-Commerce' : 'سایت شرکتی و فروشگاهی', desc: isEn ? 'Designing clean, conversion-focused websites with attention to layout.' : 'طراحی وب‌سایت‌های مدرن، فروشگاه‌های آنلاین امن و پلتفرم‌های معرفی برند.' },
    { title: isEn ? 'UI/UX & Branding' : 'طراحی رابط کاربری', desc: isEn ? 'Crafting cohesive visual identities that communicate a clear presence.' : 'طراحی رابط کاربری جذاب و کاربرپسند برای ایجاد تجربه‌ای فراموش‌نشدنی.' },
    { title: isEn ? 'SEO & Optimization' : 'سئو و بهینه‌سازی', desc: isEn ? 'High-quality optimizations that bring concepts to life.' : 'بهینه‌سازی سرعت و ساختار سایت برای ارتقای رتبه در موتورهای جستجو.' }
  ]
})

// --- API Fetching ---
const { data: projectsData, pending: pendingProjects } = await useLazyFetch('/projects/', {
  baseURL: config.public.apiBase,
  server: false, 
  transform: (response) => response.results || response
})

const projects = computed(() => projectsData.value ? projectsData.value.slice(0, 3) : [])

const getMediaUrl = (path) => {
  if (!path) return null
  try {
    if (path.startsWith('http')) return path;
    return `${config.public.apiBaseHost}${path}`
  } catch (e) { return path }
}

const gifs = [
  'https://motionsites.ai/assets/hero-space-voyage-preview-eECLH3Yc.gif',
  'https://motionsites.ai/assets/hero-codenest-preview-Cgppc2qV.gif',
  'https://motionsites.ai/assets/hero-vex-ventures-preview-BczMFIiw.gif',
  'https://motionsites.ai/assets/hero-stellar-ai-v2-preview-DjvxjG3C.gif',
  'https://motionsites.ai/assets/hero-asme-preview-B_nGDnTP.gif',
  'https://motionsites.ai/assets/hero-transform-data-preview-Cx5OU29N.gif',
]

const marqueeSec = ref(null)
const marqueeOffset = ref(0)
const magnetEl = ref(null)

const onMouseMove = (e) => {
  if (!magnetEl.value) return;
  const { left, top, width, height } = magnetEl.value.getBoundingClientRect();
  const x = (e.clientX - (left + width / 2)) / 3;
  const y = (e.clientY - (top + height / 2)) / 3;
  magnetEl.value.style.transform = `translate3d(${x}px, ${y}px, 0)`;
  magnetEl.value.style.transition = 'transform 0.3s ease-out';
}
const onMouseLeave = () => {
  if (!magnetEl.value) return;
  magnetEl.value.style.transform = `translate3d(0, 0, 0)`;
  magnetEl.value.style.transition = 'transform 0.6s ease-in-out';
}

let observer = null;
const handleScroll = () => {
  if (!marqueeSec.value) return;
  const rect = marqueeSec.value.getBoundingClientRect();
  const sectionTop = rect.top + window.scrollY;
  marqueeOffset.value = (window.scrollY - sectionTop + window.innerHeight) * 0.3;
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

  document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
  if (observer) observer.disconnect();
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;700;900&display=swap');

.font-kanit {
  font-family: 'Kanit', 'Vazirmatn', sans-serif;
}

.hero-heading {
  background: linear-gradient(180deg, #646973 0%, #BBCCD7 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.contact-btn {
  background: linear-gradient(123deg, #18011F 7%, #B600A8 37%, #7621B0 72%, #BE4C00 100%);
  box-shadow: 0px 4px 4px rgba(181, 1, 167, 0.25), inset 4px 4px 12px #7721B1;
  outline: 2px solid white;
  outline-offset: -3px;
}

.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.25, 0.1, 0.25, 1), transform 0.8s cubic-bezier(0.25, 0.1, 0.25, 1);
  will-change: opacity, transform;
}

.reveal.active {
  opacity: 1;
  transform: translateY(0);
}

.delay-100 { transition-delay: 100ms; }
.delay-200 { transition-delay: 200ms; }
.delay-300 { transition-delay: 300ms; }
.delay-400 { transition-delay: 400ms; }
.delay-500 { transition-delay: 500ms; }

.sticky { position: -webkit-sticky; position: sticky; }
</style>
