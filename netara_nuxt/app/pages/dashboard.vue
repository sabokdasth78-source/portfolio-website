<template>
  <div class="min-h-screen pt-28 pb-12 px-4 sm:px-6 lg:px-8 container mx-auto" :dir="lang === 'en' ? 'ltr' : 'rtl'">
    
    <!-- خوش‌آمدگویی -->
    <div class="mb-8 animate-fade-up">
      <h1 class="text-3xl md:text-4xl font-extrabold text-slate-900 dark:text-white mb-2">
        {{ t.hello }} <span class="text-transparent bg-clip-text bg-gradient-to-l from-cyan-500 to-purple-600">{{ username }}</span>! 👋
      </h1>
      <p class="text-slate-600 dark:text-slate-400">{{ t.welcome }}</p>
    </div>

    <!-- شبکه‌ی کارت‌ها -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 animate-fade-up" style="animation-delay: 0.1s;">
      
      <!-- کارت اطلاعات حساب -->
      <div class="bg-white/40 dark:bg-slate-900/40 backdrop-blur-xl p-6 md:p-8 rounded-[2.5rem] border border-slate-200/50 dark:border-white/5 shadow-xl relative overflow-hidden group">
        <div class="absolute -top-10 -right-10 w-32 h-32 bg-cyan-500/10 rounded-full blur-[30px] -z-10 group-hover:bg-cyan-500/20 transition-all duration-500"></div>
        <div class="flex items-center gap-4 mb-6">
          <div class="p-3 bg-cyan-100 dark:bg-cyan-500/20 rounded-2xl text-cyan-600 dark:text-cyan-400">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
          </div>
          <h2 class="text-xl font-bold text-slate-900 dark:text-white">{{ t.userInfo }}</h2>
        </div>
        <div class="space-y-3">
          <div class="flex justify-between border-b border-slate-200/50 dark:border-slate-800/50 pb-2">
            <span class="text-slate-500 dark:text-slate-400 text-sm">{{ t.usernameLabel }}</span>
            <span class="font-medium text-slate-800 dark:text-slate-200">{{ username }}</span>
          </div>
          <div class="flex justify-between border-b border-slate-200/50 dark:border-slate-800/50 pb-2">
            <span class="text-slate-500 dark:text-slate-400 text-sm">{{ t.statusLabel }}</span>
            <span class="font-medium text-emerald-600 dark:text-emerald-400 bg-emerald-100 dark:bg-emerald-500/10 px-2 py-0.5 rounded-lg text-xs">{{ t.active }}</span>
          </div>
        </div>
      </div>

      <!-- کارت مشاوره‌ها / پیام‌ها -->
      <div class="bg-white/40 dark:bg-slate-900/40 backdrop-blur-xl p-6 md:p-8 rounded-[2.5rem] border border-slate-200/50 dark:border-white/5 shadow-xl relative overflow-hidden group">
        <div class="absolute -bottom-10 -left-10 w-32 h-32 bg-purple-500/10 rounded-full blur-[30px] -z-10 group-hover:bg-purple-500/20 transition-all duration-500"></div>
        <div class="flex items-center gap-4 mb-6">
          <div class="p-3 bg-purple-100 dark:bg-purple-500/20 rounded-2xl text-purple-600 dark:text-purple-400">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
          </div>
          <h2 class="text-xl font-bold text-slate-900 dark:text-white">{{ t.myRequests }}</h2>
        </div>
        
        <!-- وضعیت در حال بارگذاری -->
        <div v-if="pendingRequests" class="flex justify-center py-4 text-slate-500 dark:text-slate-400 text-sm">
          {{ t.loading }}
        </div>
        
        <!-- حالت بدون پیام -->
        <div v-else-if="myRequests.length === 0" class="flex flex-col items-center justify-center py-4 text-center">
          <p class="text-slate-500 dark:text-slate-400 text-sm mb-4">{{ t.noRequests }}</p>
          <NuxtLink to="/contact" class="text-sm font-bold text-purple-600 dark:text-purple-400 hover:text-purple-700 dark:hover:text-purple-300 transition-colors">
            {{ t.newRequest }} <span v-html="lang === 'en' ? '&rarr;' : '&larr;'"></span>
          </NuxtLink>
        </div>

        <!-- لیست پیام‌ها -->
        <div v-else class="space-y-3 max-h-48 overflow-y-auto pr-2 custom-scrollbar">
          <div v-for="req in myRequests" :key="req.id" class="p-3 bg-white/50 dark:bg-slate-800/50 rounded-xl border border-slate-200/50 dark:border-slate-700/50">
            <p class="text-xs text-slate-400 mb-1">{{ req.date }}</p>
            <p class="text-sm text-slate-700 dark:text-slate-200 line-clamp-2">{{ req.description }}</p>
          </div>
          <div class="pt-2 text-center border-t border-slate-200/50 dark:border-slate-800/50 mt-2">
            <NuxtLink to="/contact" class="text-xs font-bold text-purple-600 dark:text-purple-400 hover:text-purple-700 dark:hover:text-purple-300 transition-colors">
              {{ t.newRequest }} <span v-html="lang === 'en' ? '&rarr;' : '&larr;'"></span>
            </NuxtLink>
          </div>
        </div>

      </div>

      <!-- کارت تنظیمات -->
      <div class="bg-white/40 dark:bg-slate-900/40 backdrop-blur-xl p-6 md:p-8 rounded-[2.5rem] border border-slate-200/50 dark:border-white/5 shadow-xl relative overflow-hidden group">
        <div class="absolute -top-10 left-10 w-32 h-32 bg-blue-500/10 rounded-full blur-[30px] -z-10 group-hover:bg-blue-500/20 transition-all duration-500"></div>
        <div class="flex items-center gap-4 mb-6">
          <div class="p-3 bg-blue-100 dark:bg-blue-500/20 rounded-2xl text-blue-600 dark:text-blue-400">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
          </div>
          <h2 class="text-xl font-bold text-slate-900 dark:text-white">{{ t.settings }}</h2>
        </div>
        <div class="space-y-4">
          <button @click="showPasswordModal = true" class="w-full text-right px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors text-sm font-medium" :class="{'text-left': lang === 'en'}">{{ t.btnChangePass }}</button>
          <button @click="logout" class="w-full text-right px-4 py-2 rounded-xl bg-red-50 dark:bg-red-500/10 text-red-600 dark:text-red-400 hover:bg-red-100 dark:hover:bg-red-500/20 transition-colors text-sm font-medium border border-transparent dark:border-red-500/10" :class="{'text-left': lang === 'en'}">{{ t.btnLogout }}</button>
        </div>
      </div>
      
    </div>

    <!-- مدال تغییر رمز عبور -->
    <div v-if="showPasswordModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm transition-opacity">
      <div class="bg-white dark:bg-slate-900 rounded-[2rem] border border-slate-200 dark:border-slate-800 shadow-2xl p-6 md:p-8 w-full max-w-md relative animate-fade-up">
        
        <button @click="showPasswordModal = false" class="absolute top-4 left-4 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>

        <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-6">{{ t.btnChangePass }}</h3>

        <form @submit.prevent="handleChangePassword" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">{{ t.currentPass }}</label>
            <input v-model.trim="oldPassword" type="password" required class="w-full px-4 py-3 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-cyan-500 outline-none transition-all" placeholder="••••••••" />
          </div>
          
          <div>
            <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">{{ t.newPass }}</label>
            <input v-model.trim="newPassword" type="password" required class="w-full px-4 py-3 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-cyan-500 outline-none transition-all" placeholder="••••••••" />
          </div>

          <!-- پیام‌های موفقیت و خطا -->
          <div v-if="passError" class="text-red-500 text-sm bg-red-50 dark:bg-red-500/10 p-3 rounded-lg border border-red-200 dark:border-red-500/20">{{ passError }}</div>
          <div v-if="passSuccess" class="text-emerald-500 text-sm bg-emerald-50 dark:bg-emerald-500/10 p-3 rounded-lg border border-emerald-200 dark:border-emerald-500/20">{{ passSuccess }}</div>

          <div class="flex gap-3 pt-4">
            <button type="submit" :disabled="passPending" class="flex-1 bg-gradient-to-r from-cyan-500 to-blue-500 text-white font-bold py-3 px-4 rounded-xl hover:from-cyan-600 hover:to-blue-600 focus:ring-2 focus:ring-cyan-500 focus:ring-offset-2 dark:focus:ring-offset-slate-900 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex justify-center items-center">
              <span v-if="passPending">{{ t.saving }}</span>
              <span v-else>{{ t.btnSave }}</span>
            </button>
            <button type="button" @click="showPasswordModal = false" class="flex-1 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold py-3 px-4 rounded-xl hover:bg-slate-200 dark:hover:bg-slate-700 transition-all">{{ t.btnCancel }}</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

const router = useRouter()
const username = useCookie('username')
const accessToken = useCookie('access_token')
const lang = useCookie('lang', { default: () => 'fa' })

const t = computed(() => {
  return lang.value === 'en' ? {
    hello: 'Hello,',
    welcome: 'Welcome to your dashboard.',
    userInfo: 'User Information',
    usernameLabel: 'Username:',
    statusLabel: 'Account Status:',
    active: 'Active',
    myRequests: 'My Requests',
    loading: 'Loading...',
    noRequests: 'You haven\'t submitted any consultation requests yet.',
    newRequest: 'Submit New Request',
    settings: 'Settings',
    btnChangePass: 'Change Password',
    btnLogout: 'Logout',
    currentPass: 'Current Password',
    newPass: 'New Password',
    saving: 'Saving...',
    btnSave: 'Save Changes',
    btnCancel: 'Cancel',
    msgPassSuccess: 'Password changed successfully.',
    msgPassError: 'An error occurred. Please try again.'
  } : {
    hello: 'سلام،',
    welcome: 'به پنل کاربری خود خوش آمدید.',
    userInfo: 'اطلاعات کاربری',
    usernameLabel: 'نام کاربری:',
    statusLabel: 'وضعیت حساب:',
    active: 'فعال',
    myRequests: 'درخواست‌های من',
    loading: 'در حال بارگذاری...',
    noRequests: 'تا کنون درخواست مشاوره‌ای ثبت نکرده‌اید.',
    newRequest: 'ثبت درخواست جدید',
    settings: 'تنظیمات',
    btnChangePass: 'تغییر رمز عبور',
    btnLogout: 'خروج از حساب',
    currentPass: 'رمز عبور فعلی',
    newPass: 'رمز عبور جدید',
    saving: 'در حال ثبت...',
    btnSave: 'ذخیره تغییرات',
    btnCancel: 'لغو',
    msgPassSuccess: 'رمز عبور با موفقیت تغییر کرد.',
    msgPassError: 'خطایی رخ داده است. لطفا دوباره تلاش کنید.'
  }
})

// متغیرهای مدیریت مدال تغییر رمز عبور
const showPasswordModal = ref(false)
const oldPassword = ref('')
const newPassword = ref('')
const passError = ref('')
const passSuccess = ref('')
const passPending = ref(false)

// متغیرهای مدیریت درخواست‌ها
const myRequests = ref([])
const pendingRequests = ref(true)

// دریافت درخواست‌ها از API
const fetchRequests = async () => {
  try {
    const response = await $fetch(`${config.public.apiBase}/requests/`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${accessToken.value}`
      }
    })
    myRequests.value = response
  } catch (error) {
    console.error('خطا در دریافت درخواست‌ها:', error)
  } finally {
    pendingRequests.value = false
  }
}

// اگر کاربر لاگین نبود، به صفحه ورود منتقل شود
onMounted(() => {
  if (!username.value) {
    router.push('/login')
  } else {
    fetchRequests()
  }
})

// منطق تغییر رمز عبور
const handleChangePassword = async () => {
  passError.value = ''
  passSuccess.value = ''
  passPending.value = true
  
  try {
    const response = await $fetch(`${config.public.apiBase}/change-password/`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${accessToken.value}`
      },
      body: {
        old_password: oldPassword.value,
        new_password: newPassword.value
      }
    })
    
    passSuccess.value = response.message || t.value.msgPassSuccess
    oldPassword.value = ''
    newPassword.value = ''
    
    // بستن مدال پس از چند ثانیه
    setTimeout(() => {
      showPasswordModal.value = false
      passSuccess.value = ''
    }, 2500)
    
  } catch (error) {
    passError.value = error.data?.error || t.value.msgPassError
  } finally {
    passPending.value = false
  }
}

const logout = () => {
  const refreshToken = useCookie('refresh_token')
  
  accessToken.value = null
  refreshToken.value = null
  username.value = null
  
  router.push('/login')
}
</script>

<style scoped>
/* برای زیباتر شدن اسکرول‌بار در لیست درخواست‌ها */
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(148, 163, 184, 0.3);
  border-radius: 4px;
}
.dark .custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(71, 85, 105, 0.5);
}
</style>
