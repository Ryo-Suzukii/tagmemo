<script setup lang="ts">
import { ref } from "vue";
import { useI18n } from "vue-i18n";
import { useRouter } from "vue-router";

import { useAuthData } from "../stores/AuthCommon";

const authData = useAuthData();
const { t } = useI18n();
const enc = new TextDecoder("utf-8");
const memoData = ref<Memo[]>([]);
const isLoading = ref(false);

const handleMemo = (mode: string) => {
  const url = 'api/live/dev-tagmemo-api-Function-Auth?user_id=' + authData.userId + '&mode=' + mode;
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

  isLoading.value = true;

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
            }
          });
        }
      }
    }).finally(() => {
      isLoading.value = false;
    });
  };

  const handleMemoAdd = (
    mode: string,
    userId: string,
    memoId: string,
    title: string,
    date: string,
    tags: Array<string>,
    content: string
  ) => {
  const url = 'api/live/dev-tagmemo-api-Function-Auth?user_id=' + userId + '&mode=' + mode + '&memo_id=' + memoId + '&title=' + title + '&date=' + date + '&tags=' + tags + '&content=' + content;
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
            }
          });
        }
      }
    })
  };

  const handleMemoDelete = (memoId: string) => {
  const url = 'api/live/dev-tagmemo-api-Function-Auth?user_id=' + authData.userId + '&mode=delete' + '&memo_id=' + memoId;
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
        console.log('success');
      }
    })
  };

handleMemo("get");

interface Memo {
  title: string;
  date: string;
  tags: string[];
  content: string;
  memo_id: string;
  index?: number;
  created_at?: string;
}

const editingMemo = ref<Memo | null>(null);

function startEditing(memoIndex: number) {
  const memo = memoData.value[memoIndex];
  if (typeof memo === 'object' && memo !== null) {
    editingMemo.value = { index: memoIndex, ...memo };
  }
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
    console.log(editingMemo.value.tags);

    if (index !== undefined) { // Update
      updatedMemo.tags = Array.from(updatedMemo.tags);
      memoData.value[index] = updatedMemo;
      handleMemoAdd(
        "add",
        authData.userId,
        updatedMemo.memo_id,
        updatedMemo.title,
        updatedMemo.date,
        updatedMemo.tags,
        updatedMemo.content
      );
      window.location.reload();
    } else { // Add
      updatedMemo.tags = Array.from(updatedMemo.tags);
      memoData.value.push(updatedMemo);
      handleMemoAdd(
        "add",
        authData.userId,
        authData.userId + '_' + Math.round(Math.random() * 1000),
        updatedMemo.title,
        updatedMemo.date,
        updatedMemo.tags,
        updatedMemo.content
      );
    }
    editingMemo.value = null;
    window.location.reload();
  }
}

function createNewMemo() {
  editingMemo.value = {
    title: "",
    date: new Date().toISOString().split("T")[0],
    tags: [],
    content: "",
    memo_id: "",
  };
}

function deleteMemo(index: number, memoId: string) {
  if (window.confirm("このメモを削除してもよろしいですか？")) {
    memoData.value.splice(index, 1);
    handleMemoDelete(memoId);
  }
}
</script>


<template>
  <div v-if="isLoading" class="loading-overlay">
    <div class="loading-spinner"></div>
    <p>Loading...</p>
  </div>
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
        <h3>最終更新:{{ memo.created_at }}</h3>
        <div>
            <h4 v-for="(tag, tagIndex) in memo.tags" :key="tagIndex" @click.stop="console.log(tag)">#{{ tag }}</h4>
        </div>
        <p>{{ memo.content }}</p>
        <p style="display: none;">{{ memo.memo_id }}</p>
      </div>
      <button class="delete-button" @click.stop="deleteMemo(index, memo.memo_id)">Delete</button>
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
  cursor: pointer;
}

h4L:hover {
  color: sandybrown;
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

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  color: white;
}

.spinner {
  border: 4px solid rgba(255, 255, 255, 0.2);
  border-left-color: white;
  border-radius: 50%;
  width: 3rem;
  height: 3rem;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

</style>
