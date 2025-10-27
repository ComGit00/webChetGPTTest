// DOM 요소
const chatMessages = document.getElementById('chatMessages');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

// 대화 기록 저장
let conversationHistory = [];

// 사용자 메시지 전송
sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// 메시지 전송 함수
async function sendMessage() {
    const message = messageInput.value.trim();
    
    if (!message) return;
    
    // UI 업데이트
    messageInput.value = '';
    sendButton.disabled = true;
    
    // 사용자 메시지 표시
    addMessage(message, 'user');
    
    // 타이핑 인디케이터 표시
    showTypingIndicator();
    
    try {
        // 서버로 메시지 전송
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message,
                conversationHistory
            })
        });
        
        const data = await response.json();
        
        // 타이핑 인디케이터 숨기기
        hideTypingIndicator();
        
        if (response.ok) {
            // 봇 응답 표시
            addMessage(data.response, 'bot');
            
            // 대화 기록 업데이트
            conversationHistory.push({ role: 'user', content: message });
            conversationHistory.push({ role: 'assistant', content: data.response });
        } else {
            // 오류 메시지 표시
            addMessage('죄송합니다. 오류가 발생했습니다: ' + data.error, 'bot');
        }
    } catch (error) {
        hideTypingIndicator();
        addMessage('연결 오류가 발생했습니다. 서버가 실행 중인지 확인해주세요.', 'bot');
        console.error('Error:', error);
    } finally {
        sendButton.disabled = false;
        messageInput.focus();
    }
}

// 메시지 추가 함수
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = text;
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    // 스크롤을 맨 아래로
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// 타이핑 인디케이터 표시
function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message';
    typingDiv.id = 'typingIndicator';
    
    const typingContent = document.createElement('div');
    typingContent.className = 'typing-indicator';
    typingContent.innerHTML = '<span></span><span></span><span></span>';
    
    typingDiv.appendChild(typingContent);
    chatMessages.appendChild(typingDiv);
    
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// 타이핑 인디케이터 숨기기
function hideTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

