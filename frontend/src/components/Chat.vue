<!-- eslint-disable vue/multi-word-component-names -->

<template>
  <div class="chat">
    <div v-for="(message, index) in messages" :key="index" class="message">
      {{ message }}
    </div>
    <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message...">
    <button @click="fetchData">Fetch Data from Flask Backend</button>
    <div v-if="flaskData" class="flask-data">{{ flaskData }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [],
      newMessage: '',
      flaskData: null
    };
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.messages.push(this.newMessage);
        this.newMessage = '';
      }
    },
    async fetchData() {
      try {
        const response = await fetch('https://pyany123.pythonanywhere.com/api/data');
        const data = await response.json();
        this.flaskData = data.message;
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
};
</script>

<style scoped>
.chat {
  border: 1px solid #ccc;
  padding: 10px;
}

.message {
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 5px;
  margin-top: 10px;
}

button {
  margin-top: 10px;
}

.flask-data {
  margin-top: 10px;
  font-style: italic;
}
</style>
