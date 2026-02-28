<template>
  <div class="url-field">
    <span class="url-icon">
      <svg viewBox="0 0 16 16" fill="none">
        <circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.2"/>
        <path d="M2 8h12M8 2c-1.5 2-2.5 3.8-2.5 6S6.5 13 8 14M8 2c1.5 2 2.5 3.8 2.5 6S9.5 13 8 14" stroke="currentColor" stroke-width="1.1"/>
      </svg>
    </span>
    <input
      :value="modelValue"
      type="url"
      class="url-input"
      placeholder="https://example.com/article"
      :disabled="loading"
      @input="$emit('update:modelValue', $event.target.value)"
      @keydown.enter="$emit('submit')"
    />
  </div>
</template>

<script setup>
defineProps({
  modelValue: { type: String, default: '' },
  loading: { type: Boolean, default: false },
})
defineEmits(['update:modelValue', 'submit'])
</script>

<style scoped>
.url-field {
  position: relative;
  display: flex;
  align-items: center;
}

.url-icon {
  position: absolute;
  left: 0.9rem;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  pointer-events: none;
}

.url-icon svg {
  width: 15px;
  height: 15px;
}

.url-input {
  width: 100%;
  padding: 0.8rem 1rem 0.8rem 2.5rem;
  background: var(--bg);
  border: 1.5px solid var(--border);
  border-radius: 10px;
  color: var(--text);
  font-size: 0.95rem;
  font-family: inherit;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.url-input::placeholder { color: var(--text-muted); }

.url-input:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-glow);
}

.url-input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
