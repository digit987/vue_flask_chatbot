<template>
  <div class="container">
    <div class="center">
      <img src="@/assets/logo.jpeg" alt="Logo" class="logo">
      <h1><span class="welcome-text">Welcome to Smile2Steps</span></h1>
    </div>
    <div class="strip">
      <div class="center faded-text">Empowering Parents, Enriching Childhood</div>
    </div>
    <div class="card-container">
      <div class="card" @click="populateInput('Help me with baby\'s first food')">Help me with baby's first food</div>
      <div class="card" @click="populateInput('How to improve my child\'s sleep?')">How to improve my child's sleep?</div>
      <div class="card" @click="populateInput('What are fun activities for toddlers?')">What are fun activities for toddlers?</div>
      <div class="card" @click="populateInput('When should my baby start crawling?')">When should my baby start crawling?</div>
    </div>
    <div v-if="messages.length > 0" class="messages-container" :style="{ maxHeight: `${maxHeight}px`, border: '1px solid #ccc' }">
      <div v-for="(message, index) in messages" :key="index" :class="[message.isSystem ? 'system-message-container' : 'user-message-container']">
        <img v-if="message.isSystem" src="@/assets/logo.jpeg" alt="Logo" class="small-logo">
        <div :class="[message.isSystem ? 'system-message' : 'user-message']">{{ message.text }}</div>
      </div>
    </div>
    <div class="input-container">
      <input type="text" class="input-field" v-model="newMessage" @keyup.enter="fetchData" placeholder="Ask a question...">
      <button class="input-btn" @click="fetchData">Enter</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatWindow',
  data() {
    return {
      messages: [],
      newMessage: '',
      maxHeight: 0, // Initial maxHeight for messages container
    };
  },
  methods: {
    async fetchData() {
      if (this.newMessage.trim() !== '') {
        try {
          const requestBody = { message: this.newMessage };
          const response = await fetch('http://pyany123.pythonanywhere.com/api/data', {
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
          this.$nextTick(() => {
            this.adjustMaxHeight();
            this.scrollToBottom();
          });
        } catch (error) {
          console.error('Error:', error);
        }
      }
    },
    scrollToBottom() {
      const container = this.$el.querySelector('.messages-container');
      if (container) {
        container.scrollTop = container.scrollHeight;
      }
    },
    adjustMaxHeight() {
      const singleLineHeight = 30; // Approximate height of one line
      const linesToShow = 6; // Number of lines to show for longer messages
      const minimumHeight = singleLineHeight * 2; // Height to show at least two lines

      // Calculate max height based on number of lines in messages
      let totalLines = 0;
      this.messages.forEach(message => {
        totalLines += Math.ceil(message.text.length / 50); // Assuming average characters per line is 50
      });

      this.maxHeight = Math.max(totalLines * singleLineHeight, minimumHeight, singleLineHeight * linesToShow);
    },
    populateInput(text) {
      this.newMessage = text;
    }
  },
  updated() {
    this.scrollToBottom();
  }
};
</script>

<style scoped>
/* Component-specific styles */
.container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.center {
  text-align: center;
}

.logo {
  max-width: 100px; /* Adjust the size of the logo */
  margin-bottom: 20px; /* Optional: Add some space between logo and text */
}

.strip {
  background-color: #f0f0f0;
  color: black;
  padding: 10px 0;
}

.strip .faded-text {
  font-weight: bold;
}

.card-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 20px;
  margin-bottom: 10px; /* Reduced space between cards and messages container */
}

.card {
  background-color: #f0f0f0;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  padding: 15px;
  border-radius: 5px;
  box-sizing: border-box;
  color: black;
  cursor: pointer;
}

.card:hover {
  background-color: #e0e0e0;
}

.messages-container {
  flex: 1;
  overflow-y: auto; /* Enable vertical scrolling */
  padding: 10px;
  border-radius: 5px;
  background-color: #fff;
  margin: 0; /* No margin between cards and messages container */
  transition: max-height 0.5s ease; /* Smooth transition for max height */
}

.user-message-container,
.system-message-container {
  display: flex;
  align-items: center;
  margin-bottom: 15px; /* Adjust the margin as needed */
}

.small-logo {
  max-width: 20px;
  margin-right: 10px; /* Add space between logo and message */
}

.system-message {
  background-color: #e0e0e0; /* Matching the card background color */
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  color: black;
  max-width: 70%;
  text-align: left;
}

.user-message {
  background-color: #f0f0f0; /* Matching the card background color */
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  color: black;
  max-width: 70%;
  margin-left: auto;
  text-align: right;
}

.input-container {
  display: flex;
  margin-top: 10px; /* Reduce space between messages container and input */
}

.input-field {
  flex: 1;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  text-align: right; /* Align text to the right */
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
</style>
