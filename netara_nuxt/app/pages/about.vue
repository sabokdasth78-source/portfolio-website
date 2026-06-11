<template>
  <div class="space-y-16 md:space-y-24 pb-20 pt-6 md:pt-10 px-4 md:px-0">
    
    <!-- Hero / Intro Section -->
    <section class="relative bg-white/40 dark:bg-slate-900/40 backdrop-blur-sm rounded-[2rem] md:rounded-[3rem] p-6 sm:p-8 md:p-16 border border-slate-200/50 dark:border-white/5 shadow-lg overflow-hidden">
      <div class="absolute top-0 left-0 w-full h-full bg-gradient-to-br from-cyan-500/5 to-purple-600/5 -z-10"></div>
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 md:gap-12 items-center">
        <!-- Text Content -->
        <div class="lg:col-span-7 space-y-6 md:space-y-8 animate-fade-up order-2 lg:order-1 text-center lg:text-right">
          <div class="inline-block px-4 py-1.5 rounded-full bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 text-xs md:text-sm font-semibold border border-purple-200 dark:border-purple-800/50 shadow-sm">
            👋 سلام، به دنیای من خوش آمدید
          </div>
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight leading-tight text-slate-900 dark:text-white">
            من یک توسعه‌دهنده و طراح هستم که <br class="hidden md:block" />
            <span class="text-transparent bg-clip-text bg-gradient-to-l from-cyan-500 to-purple-600">کدها را با هنر</span> ترکیب می‌کنم.
          </h1>
          <p class="text-base md:text-lg text-slate-600 dark:text-slate-400 leading-relaxed text-justify lg:text-right">
            تخصص من تبدیل ایده‌های خام به محصولات دیجیتالِ زیبا، سریع و کاربردی است. من معتقدم که یک وب‌سایت موفق فقط نباید کدهای بی‌نقصی داشته باشد، بلکه باید تجربه‌ای لذت‌بخش برای کاربر خلق کند. به همین دلیل، من هم در زمینه طراحی بصری (UI/UX و گرافیک) و هم در برنامه‌نویسی سمت کاربر و سرور مهارت کسب کرده‌ام تا بتوانم صفر تا صد یک پروژه را با بالاترین کیفیت پیاده‌سازی کنم.
          </p>
          <div class="flex flex-col sm:flex-row flex-wrap justify-center lg:justify-start gap-4 pt-4">
            <NuxtLink to="/projects/projects" class="w-full sm:w-auto text-center px-8 py-3 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-bold hover:shadow-lg hover:shadow-cyan-500/30 transition-all transform hover:-translate-y-1">
              مشاهده نمونه‌کارها
            </NuxtLink>
            <NuxtLink to="/contact" class="w-full sm:w-auto text-center px-8 py-3 rounded-full bg-white/50 dark:bg-slate-800/50 backdrop-blur-md border border-slate-300 dark:border-white/20 text-slate-700 dark:text-white font-bold hover:bg-slate-100 dark:hover:bg-slate-700 transition-all transform hover:-translate-y-1">
              ارتباط با من
            </NuxtLink>
          </div>
        </div>

        <!-- Visual / Image Placeholder -->
        <div class="lg:col-span-5 relative animate-fade-up delay-100 order-1 lg:order-2 max-w-[280px] sm:max-w-sm md:max-w-md lg:max-w-none mx-auto w-full">
          <div class="aspect-square rounded-full bg-gradient-to-tr from-cyan-400 to-purple-500 p-1.5 shadow-2xl relative overflow-hidden">
            <div class="w-full h-full bg-slate-100 dark:bg-slate-800 rounded-full flex items-center justify-center overflow-hidden relative">
              
              <!-- تصویر شما -->
              <img src="/about.png" alt="درباره من" class="w-full h-full object-cover" />

            </div>
          </div>
          <!-- Decorative Elements -->
          <div class="absolute -top-4 -right-4 md:-top-6 md:-right-6 w-16 h-16 md:w-24 md:h-24 bg-cyan-500/20 rounded-full blur-xl md:blur-2xl"></div>
          <div class="absolute -bottom-4 -left-4 md:-bottom-6 md:-left-6 w-20 h-20 md:w-32 md:h-32 bg-purple-500/20 rounded-full blur-xl md:blur-2xl"></div>
        </div>
      </div>
    </section>

    <!-- Skills Section -->
    <section class="animate-fade-up delay-200">
      <div class="text-center mb-10 md:mb-12">
        <h2 class="text-2xl sm:text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-3 md:mb-4">جعبه ابزار <span class="text-cyan-500">تخصصی</span> من</h2>
        <p class="text-sm md:text-base text-slate-500 dark:text-slate-400 max-w-2xl mx-auto">تکنولوژی‌ها و ابزارهایی که برای خلق بهترین تجربه‌های کاربری استفاده می‌کنم.</p>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 md:gap-6 max-w-6xl mx-auto">
        <div v-for="(skill, index) in professionalSkills" :key="index" 
             class="group relative p-4 md:p-6 rounded-2xl md:rounded-3xl bg-white/40 dark:bg-slate-900/40 backdrop-blur-sm border border-slate-200/80 dark:border-white/5 hover:border-cyan-400/50 dark:hover:border-cyan-500/50 transition-all duration-300 hover:shadow-xl hover:-translate-y-1 flex flex-col items-center text-center gap-3 md:gap-4">
          <div :class="`w-12 h-12 md:w-14 md:h-14 rounded-2xl flex items-center justify-center bg-gradient-to-br ${skill.gradient} shadow-lg text-white mb-1 md:mb-2 group-hover:scale-110 transition-transform duration-300`">
            <span class="text-lg md:text-xl font-bold">{{ skill.iconText }}</span>
          </div>
          <h3 class="text-base md:text-lg font-bold text-slate-800 dark:text-slate-100">{{ skill.name }}</h3>
          <p class="text-xs md:text-sm text-slate-500 dark:text-slate-400">{{ skill.category }}</p>
        </div>
      </div>
    </section>

    <!-- Approach / Work Flow -->
    <section class="bg-slate-50/80 dark:bg-slate-950/80 backdrop-blur-md rounded-[2rem] md:rounded-[2.5rem] p-6 sm:p-10 md:p-16 border border-slate-200 dark:border-white/5 animate-fade-up delay-300">
      <h2 class="text-2xl sm:text-3xl font-bold text-center text-slate-900 dark:text-white mb-8 md:mb-12">چگونه کار می‌کنم؟</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-8 lg:gap-12 text-center md:text-right">
        <div class="space-y-3 md:space-y-4 flex flex-col items-center md:items-start">
          <div class="w-10 h-10 md:w-12 md:h-12 rounded-full bg-pink-100 dark:bg-pink-900/30 text-pink-500 flex items-center justify-center text-lg md:text-xl font-bold border border-pink-200 dark:border-pink-800/50">۱</div>
          <h3 class="text-lg md:text-xl font-bold text-slate-800 dark:text-white">طراحی و ایده‌پردازی</h3>
          <p class="text-slate-600 dark:text-slate-400 text-xs md:text-sm leading-relaxed max-w-xs md:max-w-none">ابتدا با استفاده از اصول UI/UX و طراحی گرافیک، نمای بصری و ساختار تعاملی پروژه را ترسیم می‌کنم تا بهترین مسیر برای کاربر خلق شود.</p>
        </div>
        <div class="space-y-3 md:space-y-4 flex flex-col items-center md:items-start">
          <div class="w-10 h-10 md:w-12 md:h-12 rounded-full bg-cyan-100 dark:bg-cyan-900/30 text-cyan-500 flex items-center justify-center text-lg md:text-xl font-bold border border-cyan-200 dark:border-cyan-800/50">۲</div>
          <h3 class="text-lg md:text-xl font-bold text-slate-800 dark:text-white">توسعه فرانت‌اند</h3>
          <p class="text-slate-600 dark:text-slate-400 text-xs md:text-sm leading-relaxed max-w-xs md:max-w-none">با بهره‌گیری از Nuxt/Vue یا Next/React به همراه Tailwind CSS، طرح‌ها را به کدهای زنده، ریسپانسیو و بهینه‌سازی شده تبدیل می‌کنم.</p>
        </div>
        <div class="space-y-3 md:space-y-4 flex flex-col items-center md:items-start">
          <div class="w-10 h-10 md:w-12 md:h-12 rounded-full bg-emerald-100 dark:bg-emerald-900/30 text-emerald-500 flex items-center justify-center text-lg md:text-xl font-bold border border-emerald-200 dark:border-emerald-800/50">۳</div>
          <h3 class="text-lg md:text-xl font-bold text-slate-800 dark:text-white">پیاده‌سازی بک‌اند</h3>
          <p class="text-slate-600 dark:text-slate-400 text-xs md:text-sm leading-relaxed max-w-xs md:max-w-none">با استفاده از قدرت Django (Python)، منطق تجاری، پایگاه داده و APIهای قدرتمند و امن را برای پشتیبانی از سیستم توسعه می‌دهم.</p>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
useHead({
  title: 'درباره من | توسعه دهنده و طراح',
  meta: [
    { name: 'description', content: 'با من و مهارت‌های توسعه وب، طراحی UI/UX و گرافیک بیشتر آشنا شوید.' }
  ]
})

const professionalSkills = [
  { name: 'Nuxt 3', category: 'Framework', gradient: 'from-green-400 to-green-600', iconText: 'Nx' },
  { name: 'Vue.js', category: 'Frontend', gradient: 'from-emerald-400 to-teal-600', iconText: 'V' },
  { name: 'Next.js', category: 'Framework', gradient: 'from-slate-600 to-slate-900', iconText: 'Nx' },
  { name: 'React', category: 'Frontend', gradient: 'from-blue-400 to-blue-600', iconText: 'Re' },
  { name: 'Django', category: 'Backend', gradient: 'from-emerald-600 to-green-800', iconText: 'Dj' },
  { name: 'Tailwind CSS', category: 'Styling', gradient: 'from-cyan-400 to-blue-500', iconText: 'Tw' },
  { name: 'UI/UX Design', category: 'Design', gradient: 'from-pink-400 to-rose-600', iconText: 'UI' },
  { name: 'Graphic Design', category: 'Design', gradient: 'from-purple-400 to-fuchsia-600', iconText: 'Ps' }
]
</script>
