<template>
  <div class="min-h-[80vh] flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 animate-fade-up">
    <div class="max-w-md w-full space-y-8 bg-white/40 dark:bg-slate-900/40 backdrop-blur-xl p-8 md:p-10 rounded-[2.5rem] border border-slate-200/50 dark:border-white/5 shadow-2xl relative overflow-hidden">
      <!-- Background Effects -->
      <div class="absolute -top-20 -right-20 w-40 h-40 bg-purple-500/20 rounded-full blur-[50px] -z-10"></div>
      <div class="absolute -bottom-20 -left-20 w-40 h-40 bg-cyan-500/20 rounded-full blur-[50px] -z-10"></div>

      <div>
        <h2 class="text-center text-3xl font-extrabold text-slate-900 dark:text-white mb-2">{{ t.title }}</h2>
        <p class="text-center text-sm text-slate-500 dark:text-slate-400">{{ t.subtitle }}</p>
      </div>

      <form class="mt-8 space-y-6" @submit.prevent="handleRegister">
        <div class="space-y-4">
          <div>
            <label for="username" class="text-sm font-medium text-slate-700 dark:text-slate-300 block mb-1">{{ t.lblUsername }}</label>
            <input id="username" v-model="username" type="text" required class="appearance-none rounded-xl relative block w-full px-4 py-3 border border-slate-300 dark:border-slate-700 placeholder-slate-400 text-slate-900 dark:text-white bg-white/50 dark:bg-slate-800/50 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all" :placeholder="t.plUsername">
          </div>
          <div>
            <label for="password" class="text-sm font-medium text-slate-700 dark:text-slate-300 block mb-1">{{ t.lblPassword }}</label>
            <input id="password" v-model="password" type="password" required class="appearance-none rounded-xl relative block w-full px-4 py-3 border border-slate-300 dark:border-slate-700 placeholder-slate-400 text-slate-900 dark:text-white bg-white/50 dark:bg-slate-800/50 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all" placeholder="••••••••">
          </div>
        </div>

        <div v-if="errorMsg" class="text-red-500 text-sm text-center bg-red-50 dark:bg-red-500/10 py-2 rounded-lg border border-red-200 dark:border-red-500/20">
          {{ errorMsg }}
        </div>
        <div v-if="successMsg" class="text-emerald-500 text-sm text-center bg-emerald-50 dark:bg-emerald-500/10 py-2 rounded-lg border border-emerald-200 dark:border-emerald-500/20">
          {{ successMsg }}
        </div>

        <div>
          <button type="submit" :disabled="pending" class="w-full flex justify-center py-3.5 px-4 border border-transparent text-sm font-bold rounded-xl text-white bg-gradient-to-r from-purple-600 to-cyan-500 hover:shadow-lg hover:shadow-purple-500/25 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 disabled:opacity-50 transition-all transform hover:-translate-y-0.5">
            <span v-if="pending">{{ t.loading }}</span>
            <span v-else>{{ t.btnRegister }}</span>
          </button>
        </div>
        
        <div class="text-center mt-6">
          <span class="text-slate-600 dark:text-slate-400 text-sm">{{ t.haveAccount }} </span>
          <NuxtLink to="/login" class="text-sm font-bold text-purple-600 hover:text-purple-500 dark:text-purple-400 transition-colors">{{ t.btnLogin }}</NuxtLink>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useCookie } from '#app'

const lang = useCookie('lang', { default: () => 'fa' })

const t = computed(() => {
  return lang.value === 'en' ? {
    title: 'Create an Account',
    subtitle: 'Join us today',
    lblUsername: 'Username',
    plUsername: 'Choose a username',
    lblPassword: 'Password',
    loading: 'Registering...',
    btnRegister: 'Sign Up',
    haveAccount: 'Already have an account? ',
    btnLogin: 'Sign In',
    msgSuccess: 'Registration successful. Redirecting to login...',
    msgError: 'An error occurred in the system. Please try again.'
  } : {
    title: 'ساخت حساب کاربری',
    subtitle: 'به جمع ما بپیوندید',
    lblUsername: 'نام کاربری',
    plUsername: 'یک نام کاربری انتخاب کنید',
    lblPassword: 'رمز عبور',
    loading: 'در حال ثبت‌نام...',
    btnRegister: 'ثبت‌نام',
    haveAccount: 'قبلاً ثبت‌نام کرده‌اید؟ ',
    btnLogin: 'وارد شوید',
    msgSuccess: 'ثبت‌نام با موفقیت انجام شد. در حال انتقال به صفحه ورود...',
    msgError: 'خطایی در سیستم رخ داد. لطفاً دوباره تلاش کنید.'
  }
})

const username = ref('')
const password = ref('')
const errorMsg = ref('')
const successMsg = ref('')
const pending = ref(false)
const config = useRuntimeConfig()
const router = useRouter()

const handleRegister = async () => {
  pending.value = true
  errorMsg.value = ''
  successMsg.value = ''
  
  try {
    await $fetch('/register/', {
      baseURL: config.public.apiBase || `${config.public.apiBase}`,
      method: 'POST',
      body: { username: username.value, password: password.value }
    })
    
    successMsg.value = t.value.msgSuccess
    
    setTimeout(() => {
      router.push('/login')
    }, 2000)
    
  } catch (error) {
    errorMsg.value = error.response?._data?.error || t.value.msgError
  } finally {
    pending.value = false
  }
}
</script>
