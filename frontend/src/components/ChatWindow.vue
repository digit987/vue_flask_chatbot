<template>
  <div class="container">
    <div class="center">
      <h1><span class="welcome-text">Welcome to Smile2Steps</span></h1>
    </div>
    <div class="strip">
      <div class="center faded-text">Empowering Parents, Enriching Childhood</div>
    </div>
    <div class="card-container">
      <!-- Cards here -->
      <a href="#" class="card">Help me with baby's first food</a>
      <a href="#" class="card">How to improve my child's sleep?</a>
      <a href="#" class="card">What are fun activities for toddlers?</a>
      <a href="#" class="card">When should my baby start crawling?</a>
    </div>
    <div class="messages-container">
      <!-- Messages container -->
      <div v-for="(message, index) in messages" :key="index" :class="[message.isSystem ? 'system-message' : 'user-message']">{{ message.text }}</div>
    </div>
    <div class="input-container">
      <input type="text" class="input-field" v-model="newMessage" @keyup.enter="sendMessage" placeholder="Ask a question...">
      <button class="input-btn" @click="fetchData">Enter</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatWindow',
  data() {
    return {
      messages: [
        // Sample messages
        { text: "Help me with baby's first food", isSystem: false },
        { text: "No recommendation available for this age group", isSystem: true },
        { text: "What is baby's first food, who is 8 months old?", isSystem: false }
        
      ],
      newMessage: ''
    };
  },
  methods: {
    async fetchData() {
      try {
        const requestBody = { message: this.newMessage };
        const response = await fetch('https://pyany123.pythonanywhere.com/api/data', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(requestBody)
        });
        const data = await response.json();
        this.messages.push({ text: this.newMessage, isSystem: false });
        this.messages.push({ text: data.message, isSystem: true });
        this.newMessage = '';
      } catch (error) {
        console.error('Error:', error);
      }
    },
    sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.messages.push({ text: this.newMessage, isSystem: false });
        this.newMessage = '';
      }
    }
  }
};
</script>

<style scoped>
/* Component-specific styles */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
.center {
  text-align: center;
}
.strip {
  background-color: #f0f0f0; /* Changed strip background color */
  color: black; /* Changed strip text color */
  padding: 10px 0;
}
.strip .faded-text {
  font-weight: bold; /* Added bold to faded text */
}
.card-container {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}
.card {
  width: 23%;
  background-color: #f0f0f0; /* Changed card background color */
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  padding: 15px;
  border-radius: 5px;
  box-sizing: border-box;
  color: black; /* Changed card text color */
  text-decoration: none; /* Removed underline from links */
}
.card:hover {
  background-color: #e0e0e0; /* Changed background color on hover */
}
.messages-container {
  margin-top: 20px;
}
.system-message {
  text-align: left;
  margin-left: 10px; /* Adjust spacing */
  color: green; /* Changed system message text color */
}
.user-message {
  text-align: right;
  margin-right: 10px; /* Adjust spacing */
  color: blue; /* Changed user message text color */
}
.message {
  margin-bottom: 10px;
}
.message-text {
  padding: 10px;
  border-radius: 10px;
  max-width: 70%;
}
.input-container {
  display: flex;
  margin-top: 20px;
}
.input-field {
  flex: 1;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}
.input-btn {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}
.welcome-text {
  font-weight: bold;
  color: black;
}
.system-message,
.user-message {
  color: black; /* Changed message text color */
}
</style>
