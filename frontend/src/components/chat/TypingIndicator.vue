<template>
  <div class="message assistant">
    <span class="avatar">
      <svg viewBox="0 0 20 20" fill="none">
        <rect x="3" y="5" width="14" height="10" rx="3" stroke="currentColor" stroke-width="1.3"/>
        <path d="M7 9h6M7 12h4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
      </svg>
    </span>
    <div class="bubble-wrap">
      <span class="message-label">Assistant</span>
      <div class="bubble typing">
        <span></span><span></span><span></span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.message {
  display: flex;
  gap: 0.6rem;
  align-items: flex-start;
}

.avatar {
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: var(--surface-2);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: var(--text-muted);
}

.avatar svg {
  width: 14px;
  height: 14px;
}

.bubble-wrap {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.message-label {
  font-size: 0.72rem;
  color: var(--text-muted);
  padding: 0 0.25rem;
}

.bubble.typing {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 0.85rem 1rem;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: 2px 10px 10px 10px;
}

.bubble.typing span {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--text-muted);
  animation: bounce 1.2s infinite ease-in-out;
}

.bubble.typing span:nth-child(1) { animation-delay: 0s; }
.bubble.typing span:nth-child(2) { animation-delay: 0.2s; }
.bubble.typing span:nth-child(3) { animation-delay: 0.4s; }

@keyframes bounce {
  0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
  30% { transform: translateY(-5px); opacity: 1; }
}
</style>
