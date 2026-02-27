<template>
  <div class="chat-area">
    <ChatHeader
      :source-type="sourceType"
      :source-label="sourceLabel"
      @reset="$emit('reset')"
    />

    <div ref="messagesEl" class="messages">
      <ChatEmptyState
        v-if="messages.length === 0 && !loading"
        @select-suggestion="input = $event"
      />
      <TransitionGroup name="msg" tag="div" class="message-list">
        <ChatMessage
          v-for="(m, i) in messages"
          :key="i"
          :message="m"
        />
      </TransitionGroup>
      <TypingIndicator v-if="loading" />
    </div>

    <ChatInputBar
      ref="inputBarRef"
      v-model="input"
      :loading="loading"
      @send="send"
    />
  </div>
</template>

<script setup>
import { watch, nextTick, ref } from 'vue'
import { useChat } from '../composables/useChat'
import ChatHeader from './chat/ChatHeader.vue'
import ChatEmptyState from './chat/ChatEmptyState.vue'
import ChatMessage from './chat/ChatMessage.vue'
import TypingIndicator from './chat/TypingIndicator.vue'
import ChatInputBar from './chat/ChatInputBar.vue'

const props = defineProps({
  sessionId: { type: String, required: true },
  sourceType: { type: String, default: 'pdf' },
  sourceLabel: { type: String, default: '' },
})

defineEmits(['reset'])

const { messages, input, loading, messagesEl, send } = useChat(props.sessionId)
const inputBarRef = ref(null)

watch(loading, () => {
  if (!loading.value) nextTick(() => inputBarRef.value?.focus())
})
</script>

<style scoped>
.chat-area {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 140px);
  min-height: 500px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
}

.message-list {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.msg-enter-active {
  transition: opacity 0.25s ease, transform 0.25s ease;
}
.msg-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
</style>
