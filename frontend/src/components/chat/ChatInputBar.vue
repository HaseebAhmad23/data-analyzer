<template>
  <div class="input-bar">
    <div class="input-area">
      <textarea
        ref="textareaRef"
        :value="modelValue"
        class="chat-input"
        placeholder="Ask a question about your data…"
        :disabled="loading"
        rows="1"
        @input="onInput"
        @keydown="onKeydown"
      ></textarea>
      <button
        class="send-btn"
        :disabled="!modelValue.trim() || loading"
        @click="$emit('send')"
        title="Send (Enter)"
      >
        <svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M3 10l14-7-5 7 5 7-14-7z" fill="currentColor"/>
        </svg>
      </button>
    </div>
    <p class="input-hint">
      Press <kbd>Enter</kbd> to send &middot; <kbd>Shift+Enter</kbd> for new line
    </p>
  </div>
</template>

<script setup>
import { ref, watch, nextTick } from 'vue'

const props = defineProps({
  modelValue: { type: String, default: '' },
  loading: { type: Boolean, default: false },
})
const emit = defineEmits(['update:modelValue', 'send'])

const textareaRef = ref(null)

watch(() => props.modelValue, (val) => {
  if (!val) nextTick(resetHeight)
})

function onInput(e) {
  emit('update:modelValue', e.target.value)
  autoResize()
}

function onKeydown(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    emit('send')
  }
}

function autoResize() {
  const el = textareaRef.value
  if (!el) return
  el.style.height = 'auto'
  el.style.height = Math.min(el.scrollHeight, 160) + 'px'
}

function resetHeight() {
  const el = textareaRef.value
  if (el) el.style.height = 'auto'
}

function focus() {
  textareaRef.value?.focus()
}

defineExpose({ focus })
</script>

<style scoped>
.input-bar {
  border-top: 1px solid var(--border);
  flex-shrink: 0;
}

.input-area {
  display: flex;
  gap: 0.5rem;
  padding: 0.75rem 1rem 0.5rem;
  align-items: flex-end;
}

.chat-input {
  flex: 1;
  padding: 0.7rem 1rem;
  background: var(--bg);
  border: 1.5px solid var(--border);
  border-radius: 10px;
  color: var(--text);
  font-size: 0.92rem;
  font-family: inherit;
  line-height: 1.5;
  resize: none;
  overflow-y: hidden;
  min-height: 42px;
  max-height: 160px;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.chat-input::placeholder { color: var(--text-muted); }

.chat-input:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-glow);
}

.chat-input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.send-btn {
  width: 42px;
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--accent-dim), var(--indigo));
  border: none;
  border-radius: 10px;
  color: #fff;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.1s;
  flex-shrink: 0;
}

.send-btn:hover:not(:disabled) {
  opacity: 0.9;
  transform: scale(1.05);
}

.send-btn:disabled {
  opacity: 0.35;
  cursor: not-allowed;
  transform: none;
}

.send-btn svg {
  width: 16px;
  height: 16px;
}

.input-hint {
  text-align: center;
  padding: 0.2rem 1rem 0.6rem;
  font-size: 0.72rem;
  color: var(--text-faint);
}

kbd {
  font-family: inherit;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 0.05rem 0.3rem;
  font-size: 0.7rem;
}
</style>
