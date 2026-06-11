<template>
  <div class="min-h-[80vh] flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 animate-fade-up">
    <div class="max-w-md w-full space-y-8 bg-white/40 dark:bg-slate-900/40 backdrop-blur-xl p-8 md:p-10 rounded-[2.5rem] border border-slate-200/50 dark:border-white/5 shadow-2xl relative overflow-hidden">
      <!-- Background Effects -->
      <div class="absolute -top-20 -left-20 w-40 h-40 bg-cyan-500/20 rounded-full blur-[50px] -z-10"></div>
      <div class="absolute -bottom-20 -right-20 w-40 h-40 bg-purple-500/20 rounded-full blur-[50px] -z-10"></div>

      <div>
        <h2 class="text-center text-3xl font-extrabold text-slate-900 dark:text-white mb-2">ورود به حساب</h2>
        <p class="text-center text-sm text-slate-500 dark:text-slate-400">برای دسترسی به پنل کاربری وارد شوید</p>
      </div>

      <form class="mt-8 space-y-6" @submit.prevent="handleLogin">
        <div class="space-y-4">
          <div>
            <label for="username" class="text-sm font-medium text-slate-700 dark:text-slate-300 block mb-1">نام کاربری</label>
            <input id="username" v-model="username" type="text" required class="appearance-none rounded-xl relative block w-full px-4 py-3 border border-slate-300 dark:border-slate-700 placeholder-slate-400 text-slate-900 dark:text-white bg-white/50 dark:bg-slate-800/50 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent transition-all" placeholder="نام کاربری خود را وارد کنید">
          </div>
          <div>
            <label for="password" class="text-sm font-medium text-slate-700 dark:text-slate-300 block mb-1">رمز عبور</label>
            <input id="password" v-model="password" type="password" required class="appearance-none rounded-xl relative block w-full px-4 py-3 border border-slate-300 dark:border-slate-700 placeholder-slate-400 text-slate-900 dark:text-white bg-white/50 dark:bg-slate-800/50 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent transition-all" placeholder="••••••••">
          </div>
        </div>

        <div v-if="errorMsg" class="text-red-500 text-sm text-center bg-red-50 dark:bg-red-500/10 py-2 rounded-lg border border-red-200 dark:border-red-500/20">
          {{ errorMsg }}
        </div>

        <div>
          <button type="submit" :disabled="pending" class="w-full flex justify-center py-3.5 px-4 border border-transparent text-sm font-bold rounded-xl text-white bg-gradient-to-r from-cyan-500 to-purple-600 hover:shadow-lg hover:shadow-cyan-500/25 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500 disabled:opacity-50 transition-all transform hover:-translate-y-0.5">
            <span v-if="pending">در حال ورود...</span>
            <span v-else>ورود</span>
          </button>
        </div>
        
        <div class="text-center mt-6">
          <span class="text-slate-600 dark:text-slate-400 text-sm">حساب کاربری ندارید؟ </span>
          <NuxtLink to="/register" class="text-sm font-bold text-cyan-600 hover:text-cyan-500 dark:text-cyan-400 transition-colors">ثبت‌نام کنید</NuxtLink>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
const username = ref('')
const password = ref('')
const errorMsg = ref('')
const pending = ref(false)
const config = useRuntimeConfig()
const router = useRouter()

const handleLogin = async () => {
  pending.value = true
  errorMsg.value = ''
  
  try {
    const response = await $fetch('/login/', {
      baseURL: config.public.apiBase || 'http://localhost:8000',
      method: 'POST',
      body: { username: username.value, password: password.value }
    })
    
    // ذخیره توکن‌ها در کوکی
    const accessToken = useCookie('access_token', { maxAge: 60 * 60 * 24 }) // 1 day
    const refreshToken = useCookie('refresh_token', { maxAge: 60 * 60 * 24 * 7 }) // 7 days
    const usernameCookie = useCookie('username')
    
    accessToken.value = response.access
    refreshToken.value = response.refresh
    usernameCookie.value = response.username
    
    // انتقال به صفحه اصلی
    router.push('/')
  } catch (error) {
    errorMsg.value = error.response?._data?.error || 'نام کاربری یا رمز عبور اشتباه است.'
  } finally {
    pending.value = false
  }
}
</script>
