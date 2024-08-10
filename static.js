// static/script.js
const chatMessages = document.getElementById('chat-messages');
const messageInput = document.getElementById('message-input');

function sendMessage() {
    const message = messageInput.value.trim();
    if (message) {
        addMessage('User', message);
        messageInput.value = '';
        getBotResponse(message);
    }
}

function addMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function getBotResponse(message) {
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        });
        const data = await response.json();
        addMessage('Bot', data.response);
    } catch (error) {
        console.error('Error:', error);
        addMessage('Bot', 'Sorry, I encountered an error.');
    }
}

messageInput.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});