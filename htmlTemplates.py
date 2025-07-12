css = '''
<style>
body {
    background-color: #0e0e0e;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

.chat-message {
    padding: 1rem;
    margin: 1.2rem 0;
    display: flex;
    border-radius: 16px;
    background: #1c1c1e;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    align-items: flex-start;
    transition: background 0.3s ease;
}

.chat-message.user {
    background: linear-gradient(135deg, #1e1e1e, #292929);
}

.chat-message.bot {
    background: linear-gradient(135deg, #2a3b4c, #1e2a38);
}

.chat-message .avatar {
    flex-shrink: 0;
    margin-right: 1rem;
    margin-top: 4px;
}

.chat-message .avatar img {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #3e3e3e;
    box-shadow: 0 0 6px rgba(255,255,255,0.08);
}

.chat-message .message {
    flex-grow: 1;
    color: #e4e4e4;
    font-size: 1.05rem;
    line-height: 1.6;
    padding: 0.5rem 0.8rem;
    background-color: rgba(255,255,255,0.05);
    border-radius: 12px;
    word-break: break-word;
}

.chat-message .message:hover {
    background-color: rgba(255,255,255,0.08);
}
</style>
'''
user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/6NsQz3F/user-avatar.png" alt="User Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
