<template>
  <div class="app-wrapper">
    <div class="nav">
      <NavBar class="container"/>
    </div>
    <div class="content">
      <RouterView class="container" />
    </div>

    <footer>
      <br>
      Copyrights ⓒ 2024 zcmn All Rights reserved.
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useAccountStore } from '@/stores/account';

import NavBar from '@/components/navbars/NavBar.vue';

const store = useAccountStore()
// const userId = ref(store.user.id)

onMounted(() => {
  const accountStore = useAccountStore();
  if (accountStore.token) {
    accountStore.fetchUser(); // 토큰이 있으면 사용자 정보 로드
  }
});

</script>



<style scoped>
.app-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.content {
  flex: 1;
}

.nav {
  background-color: #3f2411;
}

footer {
  margin-top: 40px;
  height: 100px;
  background-color: #3f2411;
  text-align: center;
  color: white;
  font-size: 12px;
  padding: 20px 0;
}
</style>