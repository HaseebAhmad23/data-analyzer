<template>
  <div :class="['message', message.role]">
    <span class="avatar">
      <template v-if="message.role === 'user'">
        <svg viewBox="0 0 20 20" fill="none">
          <circle cx="10" cy="7" r="3.5" stroke="currentColor" stroke-width="1.3"/>
          <path d="M3 17c0-3.3 3.1-6 7-6s7 2.7 7 6" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
        </svg>
      </template>
      <template v-else>
        <svg viewBox="0 0 20 20" fill="none">
          <rect x="3" y="5" width="14" height="10" rx="3" stroke="currentColor" stroke-width="1.3"/>
          <path d="M7 9h6M7 12h4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
        </svg>
      </template>
    </span>
    <div class="bubble-wrap">
      <span class="message-label">{{ message.role === 'user' ? 'You' : 'Assistant' }}</span>
      <div class="bubble">{{ message.content }}</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  message: { type: Object, required: true },
})
</script>

<style scoped>
.message {
  display: flex;
  gap: 0.6rem;
  align-items: flex-start;
  max-width: 88%;
}

.message.user {
  align-self: flex-end;
  flex-direction: row-reverse;
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

.message.user .avatar {
  background: rgba(29, 78, 216, 0.15);
  border-color: rgba(29, 78, 216, 0.35);
  color: var(--user-bubble);
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

.message.user .message-label {
  text-align: right;
}

.bubble {
  padding: 0.7rem 1rem;
  border-radius: 10px;
  font-size: 0.92rem;
  line-height: 1.55;
  white-space: pre-wrap;
  word-break: break-word;
  background: var(--surface-2);
  border: 1px solid var(--border);
  color: var(--text);
  border-radius: 2px 10px 10px 10px;
}

.message.user .bubble {
  background: var(--user-bubble);
  border-color: rgba(29, 78, 216, 0.5);
  color: #ffffff;
  border-radius: 10px 2px 10px 10px;
}
</style>
