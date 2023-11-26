<template>
  <div>
    <!-- 悬浮按钮 -->
    <div class="fixed-button">
      <button type="button" class="btn btn-danger" @click="handleButtonClick">智能客服</button>
    </div>

    <!-- 聊天框 -->
    <div v-if="showChatBox" class="chat-box">
      <div class="chat-history" ref="chatHistory">
        <div v-for="message in messages" :key="message.id" class="message">
            {{ message.text }}     
        </div>
      </div>
      <div class="chat-input">
        <input v-model="inputText" @keydown.enter="sendMessage" type="text" placeholder="输入消息" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
        showChatBox: false,  // 控制聊天框的显示与隐藏
        inputText: '',  // 输入框中的文本
        messages: []  // 聊天消息列表            
        }
    },
    methods: {
        handleButtonClick(){
            this.showChatBox = !this.showChatBox;
            if (this.showChatBox) {
                this.scrollToBottom();
            }
        },
        scrollToBottom(){
            this.$nextTick(() => {
                const chatHistory = this.$refs.chatHistory;
                chatHistory.scrollTop = chatHistory.scrollHeight;
            });
        },
        sendMessage() {
        const message = {
            id: new Date().getTime(),
            text: this.inputText,
            fromUser: true
        };
        this.messages.push(message);
        this.inputText = '';
        this.scrollToBottom();

        // 发送消息给机器人
        axios.post('/api/chat/', { message: message.text })
            .then(response => {
            const reply = response.data.reply;
            const replyMessage = {
                id: new Date().getTime(),
                text: reply,
                fromUser: false
            };
            this.messages.push(replyMessage);
            this.scrollToBottom();
            })
            .catch(error => {
            console.error('发送消息失败：', error);
            });
        }
  
    },
}
</script>

<style>
.fixed-button {
  position: fixed;
  width: 60px;
  height: 60px;
  bottom: 20px;  /* 距离底部的距离 */
  right: 20px;  /* 距离右侧的距离 */
  z-index: 999; /* 设置按钮的堆叠顺序 */
},
.chat-box {
  position: fixed;
  bottom: 80px;
  right: 20px;
  width: 300px;
  height: 400px;
  background-color: #fff;
  border: 1px solid #ccc;
  z-index: 999;
  overflow: hidden;
}

.chat-history {
  height: calc(100% - 40px);
  overflow-y: scroll;
  padding: 10px;
}

.message {
  margin-bottom: 10px;
}

.chat-input {
  border-top: 1px solid #ccc;
  padding: 5px;
}

.chat-input input {
  width: 100%;
  padding: 5px;
  border: none;
}
</style>