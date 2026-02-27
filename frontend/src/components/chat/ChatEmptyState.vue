<template>
  <div class="empty-state">
    <div class="empty-icon">
      <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="12" fill="var(--surface-2)"/>
        <path d="M14 16h20M14 22h16M14 28h12" stroke="var(--accent)" stroke-width="1.8" stroke-linecap="round"/>
        <circle cx="34" cy="34" r="5" stroke="var(--text-muted)" stroke-width="1.5"/>
        <path d="M37.5 37.5l3 3" stroke="var(--text-muted)" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </div>
    <p class="empty-title">Ready to answer your questions</p>
    <p class="empty-hint">Ask anything about the loaded document or page.</p>
    <div class="suggestions">
      <button
        v-for="s in suggestions"
        :key="s"
        class="suggestion-chip"
        @click="$emit('select-suggestion', s)"
      >
        {{ s }}
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  suggestions: {
    type: Array,
    default: () => [
      'Summarize the main topics',
      'What are the key points?',
      'Explain the most important section',
    ],
  },
})
defineEmits(['select-suggestion'])
</script>

<style scoped>
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 3rem 2rem;
  gap: 0.5rem;
  flex: 1;
}

.empty-icon {
  width: 48px;
  height: 48px;
  margin-bottom: 0.5rem;
}

.empty-title {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text);
}

.empty-hint {
  font-size: 0.85rem;
  color: var(--text-muted);
}

.suggestions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
  margin-top: 0.75rem;
}

.suggestion-chip {
  padding: 0.4rem 0.85rem;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: 99px;
  color: var(--text-muted);
  font-size: 0.82rem;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.suggestion-chip:hover {
  border-color: var(--accent);
  color: var(--accent);
  background: var(--accent-glow);
}
</style>
