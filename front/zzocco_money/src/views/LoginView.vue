<template>

	<div class="login-container">
		<h1>로그인</h1>
		<form @submit.prevent="handleLogin">
		<div class="form-group">
			<label for="username">아이디</label>
			<input type="text" id="username" v-model="username" placeholder="아이디를 입력하세요" required />
		</div>
		<div class="form-group">
			<label for="password">비밀번호</label>
			<input type="password" id="password" v-model="password" placeholder="비밀번호를 입력하세요" required />
		</div>
		<div class="form-group">
			<button type="submit" class="submit-button">로그인</button>
		</div>
		</form>

		<p class="signup-link">
		계정이 없으신가요? <RouterLink to="/signup">회원가입</RouterLink>
		</p>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/account';

const router = useRouter()
const store = useAccountStore()
// 이메일과 비밀번호를 바인딩
const username = ref(null)
const password = ref(null)

// 로그인 처리 함수
const handleLogin = () => {
  store.logIn({
    username: username.value,
    password: password.value
  })
// 실제 로그인 로직 (백엔드 API 호출 등) 필요
// console.log('로그인 시도:', username.value, password.value)

// 성공적으로 로그인한 후 메인 페이지로 리다이렉트
// 여기에 인증 로직을 추가해야 합니다.

}
</script>

<style scoped>
.login-container {
width: 300px;
margin: 100px auto 0;
padding: 20px;
border: 1px solid #ddd;
border-radius: 5px;
background-color: #fff;
}


h1 {
  margin: 20px;
  font-size: 36px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.submit-button {
width: 100%;
padding: 10px;
background-color: #3f2411;
color: white;
border: none;
border-radius: 5px;
cursor: pointer;
}

.submit-button:hover {
background-color: #3f2411;
}

.signup-link {
text-align: center;
margin-top: 20px;
}

.signup-link a {
text-decoration: none;
color: #583423;
}
</style>