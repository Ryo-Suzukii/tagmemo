<script setup lang="ts">
import { ref } from "vue";
import { useI18n } from "vue-i18n";
import { useAuthData } from "../components/AuthCommon.vue";

const authData = useAuthData();
const { t } = useI18n();
const enc = new TextDecoder("utf-8");
const memoData = ref([]);

const handleLogin = () => {
  console.log(authData.userId);
  const url = 'api/live/dev-tagmemo-api-Function-Auth?user_id=' + authData.userId + '&mode=get';
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");
  myHeaders.append("Accept", "*/*");
  myHeaders.append("Host", "6f5dgikzng.execute-api.ap-northeast-1.amazonaws.com");
  myHeaders.append("Connection", "keep-alive");
  myHeaders.append("Access-Control-Allow-Origin", "*");

  var requestOptions: RequestInit = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow' as RequestRedirect,
  };

  fetch(url, requestOptions)
    .then(response => {
      if (response.status == 401) {
        console.log('error');
      } else if (response.status == 200) {
        if (response.body) {
          response.body.getReader().read().then(({ value, done }) => {
            if (!done && value) {
              const body = new Uint8Array(value.buffer);
              const bodyData = JSON.parse(enc.decode(body));
              for (let i = 0; i < bodyData.length; i++) {
                bodyData[i].tags = bodyData[i].tags.replace('[', '').replace(']','').split(',');
              }
              memoData.value = bodyData;
              console.log(memoData.value);
            }
          });
        }
      }
    })
  };

handleLogin();


interface Memo {
  title: string;
  date: string;
  tags: string[];
  content: string;
  index?: number;
}

const editingMemo = ref<Memo | null>(null);

function startEditing(memoIndex: number) {
  editingMemo.value = { index: memoIndex, ...memoData.value[memoIndex] };
}

function confirmAndCancelEditing() {
  if (window.confirm("編集を終了してもよろしいですか？")) {
    cancelEditing();
  }
}

function cancelEditing() {
  editingMemo.value = null;
}

function saveMemo() {
  if (editingMemo.value) {
    const { index, ...updatedMemo } = editingMemo.value;

    if (index !== undefined) {
      memoData.value[index] = updatedMemo;
    } else {
      memoData.value.push(updatedMemo);
    }
    editingMemo.value = null;
  }
}

function createNewMemo() {
  editingMemo.value = {
    title: "",
    date: new Date().toISOString().split("T")[0],
    tags: [],
    content: "",
  };
}

function deleteMemo(index: number) {
  if (window.confirm("このメモを削除してもよろしいですか？")) {
    memoData.value.splice(index, 1);
  }
}
</script>


<template>
  <div class="page-container" v-if="!authData.isLogin">
    <h1>{{ t("title") }}</h1>
    <p>{{ t("homePage.description") }}</p>
  </div>
  <div class="page-container" v-if="authData.isLogin">
    <h1>{{ authData.userId }}</h1>
    <h1>{{ t("homePage.welcome") }}</h1>
    <button class="create-memo-btn" @click="createNewMemo">Create New Memo</button>
  </div>
  <div class="memo-container" v-if="authData.isLogin">
    <div
      v-for="(memo, index) in memoData"
      :key="index"
      class="memo"
      @click="startEditing(index)"
    >
      <div class="memo-content">
        <h2>{{ memo.title }}</h2>
        <h3>{{ memo.date }}</h3>
        <h4>#{{ memo.tags.join(" #") }}</h4>
        <p>{{ memo.content }}</p>
      </div>
      <button class="delete-button" @click.stop="deleteMemo(index)">Delete</button>
    </div>
  </div>

  <div v-if="editingMemo" class="modal" @click.self="confirmAndCancelEditing">
    <div class="modal-content">
      <h2>Edit Memo</h2>
      <label>
        Title:
        <input v-model="editingMemo.title" />
      </label>
      <label>
        Date:
        <input type="date" v-model="editingMemo.date" />
      </label>
      <label>
        Tags (comma or space separated):
        <input
          v-model="editingMemo.tags"
            @input="(e) => { if (editingMemo && e.target) editingMemo.tags = (e.target as HTMLInputElement).value.split(/[\s,]+/); }"
        />
      </label>
      <label>
        Content:
        <textarea v-model="editingMemo.content"></textarea>
      </label>
      <div class="modal-actions">
        <button @click="saveMemo">Save</button>
        <button @click="confirmAndCancelEditing">Cancel</button>
      </div>
    </div>
  </div>
</template>



<style scoped>
.page-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.memo-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.memo {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0.5rem 0;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  backdrop-filter: blur(10px);
  position: relative;
}

.memo-content {
  flex-grow: 1;
}

.memo h2,
.memo h3 {
  display: inline;
  margin-right: 2%;
}

h4 {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 0.5rem;
  padding: 0.2rem;
  display: inline-block;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: rgba(255,255,255,0.1);
  padding: 2rem;
  border-radius: 1rem;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  width: 90%;
  max-width: 500px;
  color: white;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.modal-content h2 {
  text-align: center;
  font-size: 1.5rem;
  font-weight: bold;
  margin: 0;
}

.modal-content label {
  display: flex;
  flex-direction: column;
  font-size: 1rem;
  gap: 0.5rem;
}

.modal-content input,
.modal-content textarea {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  border-radius: 0.5rem;
  padding: 0.5rem;
  color: white;
  font-size: 1rem;
  outline: none;
}

.modal-content input::placeholder,
.modal-content textarea::placeholder {
  color: rgba(255, 255, 255, 0.7);
}

.modal-actions {
  margin-top: 1rem;
  display: flex;
  justify-content: space-between;
}

.modal-actions button {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

.modal-actions button:hover {
  background: rgba(255, 255, 255, 0.4);
}

.create-memo-btn {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease;
  margin-bottom: 1rem;
}

.create-memo-btn:hover {
  background: rgba(255, 255, 255, 0.4);
}

.delete-button {
  background: rgba(255, 0, 0, 0.2);
  color: white;
  border: none;
  border-radius: 0.5rem;
  padding: 0.5rem 0.5rem;
  cursor: pointer;
  transition: background 0.3s ease;
  font-size: 0.8rem;
  text-align: center;
  white-space: nowrap;
  width: auto;
}

.delete-button:hover {
  background: rgba(255, 0, 0, 0.5);
}
</style>
