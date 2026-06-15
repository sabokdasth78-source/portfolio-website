<template>
  <div class="space-y-16 pb-20 animate-fade-up">
    
    <!-- هدر صفحه -->
    <section class="text-center space-y-6 pt-10">
      <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 dark:text-white tracking-tight">
        {{ t.titleStart }} <span class="text-transparent bg-clip-text bg-gradient-to-l from-cyan-500 to-purple-600">{{ t.titleHighlight }}</span>
      </h1>
      <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl mx-auto">
        {{ t.description }}
      </p>
    </section>

    <!-- راهنمای ثبت سفارش -->
    <section class="relative bg-white/40 dark:bg-slate-900/40 backdrop-blur-xl rounded-[2.5rem] p-8 md:p-12 border border-slate-200/50 dark:border-white/5 shadow-lg">
      <h2 class="text-2xl font-bold mb-8 text-center text-slate-800 dark:text-slate-100">{{ t.howToOrder }}</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 relative">
        <!-- خط اتصال دهنده‌ی مراحل در دسکتاپ -->
        <div class="hidden md:block absolute top-1/2 left-0 right-0 h-0.5 bg-gradient-to-r from-cyan-500/20 via-purple-500/20 to-cyan-500/20 -z-10 -translate-y-1/2"></div>
        
        <div v-for="(step, index) in t.orderSteps" :key="index" class="relative bg-white/80 dark:bg-slate-800/80 p-6 rounded-2xl border border-slate-100 dark:border-slate-700 shadow-sm hover:shadow-md transition-shadow text-center group">
          <div class="w-12 h-12 mx-auto bg-gradient-to-br from-cyan-500 to-purple-600 text-white rounded-full flex items-center justify-center font-bold text-xl mb-4 shadow-lg group-hover:scale-110 transition-transform">
            {{ index + 1 }}
          </div>
          <h3 class="text-lg font-bold text-slate-800 dark:text-slate-200 mb-2">{{ step.title }}</h3>
          <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">{{ step.desc }}</p>
        </div>
      </div>
    </section>

    <!-- بخش فرم و اطلاعات تماس -->
    <section class="grid grid-cols-1 lg:grid-cols-2 gap-12">
      
      <!-- اطلاعات تماس -->
      <div class="space-y-8 bg-slate-50/80 dark:bg-slate-950/80 backdrop-blur-md rounded-3xl border border-slate-200 dark:border-white/5 p-8 shadow-sm">
        <h3 class="text-2xl font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-800 pb-4">{{ t.contactInfo }}</h3>
        
        <div class="space-y-6">
          <div class="flex items-center gap-4 group">
            <div class="w-12 h-12 rounded-full bg-cyan-100 dark:bg-cyan-900/30 text-cyan-600 dark:text-cyan-400 flex items-center justify-center group-hover:bg-cyan-500 group-hover:text-white transition-colors">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
            </div>
            <div>
              <p class="text-sm text-slate-500 dark:text-slate-400">{{ t.email }}</p>
              <a href="mailto:sabokdasth78@gmail.com" class="text-lg font-medium text-slate-800 dark:text-slate-200 hover:text-cyan-500">sabokdasth78@gmail.com</a>
            </div>
          </div>

          <div class="flex items-center gap-4 group">
            <div class="w-12 h-12 rounded-full bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 flex items-center justify-center group-hover:bg-purple-500 group-hover:text-white transition-colors">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
            </div>
            <div>
              <p class="text-sm text-slate-500 dark:text-slate-400">{{ t.phoneWA }}</p>
              <a href="tel:+989213691245" class="text-lg font-medium text-slate-800 dark:text-slate-200 hover:text-purple-500" dir="ltr">+98 921 369 1245</a>
            </div>
          </div>
          
          <div class="flex items-center gap-4 group">
             <div class="w-12 h-12 rounded-full bg-emerald-100 dark:bg-emerald-900/30 text-emerald-600 dark:text-emerald-400 flex items-center justify-center group-hover:bg-emerald-500 group-hover:text-white transition-colors">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path></svg>
            </div>
            <div>
              <p class="text-sm text-slate-500 dark:text-slate-400">{{ t.telegram }}</p>
              <a href="https://t.me/netaraweb" class="text-lg font-medium text-slate-800 dark:text-slate-200 hover:text-emerald-500" dir="ltr">@netaraweb</a>
            </div>
          </div>
        </div>
      </div>

      <!-- فرم تماس -->
      <div class="bg-white/30 dark:bg-slate-800/30 backdrop-blur-xl rounded-3xl border border-slate-200/50 dark:border-white/5 p-8 shadow-sm">
        <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-6">{{ t.directMessage }}</h3>
        <form @submit.prevent="submitForm" class="space-y-5 text-start">
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">{{ t.fullName }}</label>
            <input v-model="form.full_name" type="text" :placeholder="t.plName" required class="w-full px-4 py-3 rounded-xl bg-white/50 dark:bg-slate-900/50 border border-slate-200 dark:border-slate-700 focus:ring-2 focus:ring-cyan-500 outline-none transition-all dark:text-white">
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div>
              <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">{{ t.phoneLabel }}</label>
              <input v-model="form.phone" type="tel" :placeholder="t.plPhone" required class="w-full px-4 py-3 rounded-xl bg-white/50 dark:bg-slate-900/50 border border-slate-200 dark:border-slate-700 focus:ring-2 focus:ring-cyan-500 outline-none transition-all dark:text-white" dir="ltr">
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">{{ t.emailLabel }}</label>
              <input v-model="form.email" type="email" placeholder="email@example.com" class="w-full px-4 py-3 rounded-xl bg-white/50 dark:bg-slate-900/50 border border-slate-200 dark:border-slate-700 focus:ring-2 focus:ring-cyan-500 outline-none transition-all dark:text-white" dir="ltr">
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">{{ t.messageLabel }}</label>
            <textarea v-model="form.description" rows="4" :placeholder="t.plMessage" required class="w-full px-4 py-3 rounded-xl bg-white/50 dark:bg-slate-900/50 border border-slate-200 dark:border-slate-700 focus:ring-2 focus:ring-cyan-500 outline-none transition-all dark:text-white resize-none"></textarea>
          </div>

          <button type="submit" :disabled="isSubmitting" class="w-full py-4 rounded-xl bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-bold hover:shadow-[0_0_20px_rgba(6,182,212,0.4)] hover:scale-[1.02] transition-all duration-300 flex justify-center items-center gap-2 disabled:opacity-70 disabled:cursor-not-allowed">
            <span v-if="isSubmitting">{{ t.sending }}</span>
            <template v-else>
              {{ t.btnSubmit }}
              <svg class="w-5 h-5 rtl:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </template>
          </button>
        </form>
      </div>

    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useCookie, useHead } from '#app'

const lang = useCookie('lang', { default: () => 'fa' })

const t = computed(() => {
  return lang.value === 'en' ? {
    titleStart: 'Contact Me &',
    titleHighlight: 'Order a Project',
    description: 'To start a new project, get a consultation, or ask any questions, you can contact me via the form below or my contact details.',
    howToOrder: 'How to order a website?',
    orderSteps: [
      { title: 'Send Requirements', desc: 'First, send your website features and requirements via the form below or messengers.' },
      { title: 'Consultation & Pricing', desc: 'After review, we will have a free consultation session to estimate time and cost.' },
      { title: 'Design & Coding', desc: 'User Interface (UI) design will be done, and upon your approval, Backend and Frontend development will start.' },
      { title: 'Delivery & Support', desc: 'The site will be deployed on your server, and management training along with initial support will be provided.' }
    ],
    contactInfo: 'Contact Information',
    email: 'Email',
    phoneWA: 'Phone & WhatsApp',
    telegram: 'Telegram ID',
    directMessage: 'Send a Direct Message',
    fullName: 'Full Name',
    plName: 'Your Name',
    phoneLabel: 'Phone Number',
    plPhone: '+1 234...',
    emailLabel: 'Email (Optional)',
    messageLabel: 'Project Description or Message',
    plMessage: 'Write the details of the project you have in mind...',
    sending: 'Sending...',
    btnSubmit: 'Send Message',
    msgSuccess: 'Your message has been sent successfully.',
    msgError: 'An error occurred while sending the message. Please try again.',
    metaTitle: 'Contact Me & Order Project | Portfolio',
    metaDesc: 'Contact me for website design, programming, or consultation.'
  } : {
    titleStart: 'تماس با من و',
    titleHighlight: 'ثبت سفارش',
    description: 'برای شروع یک پروژه جدید، دریافت مشاوره یا مطرح کردن سوالات خود، می‌توانید از طریق فرم زیر یا اطلاعات تماس با من در ارتباط باشید.',
    howToOrder: 'چطور یک سایت سفارش دهم؟',
    orderSteps: [
      { title: 'ارسال نیازمندی‌ها', desc: 'ابتدا از طریق فرم پایین یا پیام‌رسان‌ها، امکانات و نیازمندی‌های سایت خود را ارسال کنید.' },
      { title: 'مشاوره و قیمت‌گذاری', desc: 'پس از بررسی، یک جلسه مشاوره رایگان خواهیم داشت و برآورد زمان و هزینه اعلام می‌شود.' },
      { title: 'شروع طراحی و کدنویسی', desc: 'طراحی رابط کاربری (UI) انجام شده و پس از تایید شما، توسعه بک‌اِند و فرانت‌اِند شروع می‌شود.' },
      { title: 'تحویل و پشتیبانی', desc: 'سایت روی سرور شما مستقر شده و آموزش مدیریت آن به همراه پشتیبانی اولیه ارائه می‌گردد.' }
    ],
    contactInfo: 'اطلاعات ارتباطی',
    email: 'ایمیل',
    phoneWA: 'تلفن و واتس‌اپ',
    telegram: 'آیدی تلگرام',
    directMessage: 'ارسال پیام مستقیم',
    fullName: 'نام و نام خانوادگی',
    plName: 'نام شما',
    phoneLabel: 'شماره تماس',
    plPhone: '09...',
    emailLabel: 'ایمیل (اختیاری)',
    messageLabel: 'توضیحات پروژه یا پیام شما',
    plMessage: 'جزئیات پروژه‌ای که در ذهن دارید را اینجا بنویسید...',
    sending: 'در حال ارسال...',
    btnSubmit: 'ارسال پیام',
    msgSuccess: 'پیام شما با موفقیت ثبت شد.',
    msgError: 'خطایی در ارسال پیام رخ داد. لطفا دوباره تلاش کنید.',
    metaTitle: 'تماس با من و سفارش سایت | پورتفولیو',
    metaDesc: 'برای سفارش طراحی سایت، برنامه‌نویسی و یا مشاوره با من در ارتباط باشید.'
  }
})

useHead(() => ({
  title: t.value.metaTitle,
  meta: [
    { name: 'description', content: t.value.metaDesc }
  ]
}))

const form = ref({
  full_name: '',
  phone: '',
  email: '',
  description: ''
})
const isSubmitting = ref(false)
const accessToken = useCookie('access_token')

const submitForm = async () => {
  isSubmitting.value = true
  try {
    const headers = {}
    if (accessToken.value) {
      headers['Authorization'] = `Bearer ${accessToken.value}`
    }

    await $fetch(`${config.public.apiBase}/requests/`, {
      method: 'POST',
      headers,
      body: form.value
    })
    
    alert(t.value.msgSuccess)
    form.value = { full_name: '', phone: '', email: '', description: '' }
  } catch (error) {
    alert(t.value.msgError)
  } finally {
    isSubmitting.value = false
  }
}
</script>
