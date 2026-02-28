<template>
  <div class="chat-header">
    <div class="header-left">
      <span :class="['badge', sourceType]">{{ sourceType === 'pdf' ? 'PDF' : 'URL' }}</span>
      <span class="source-label" :title="sourceLabel">{{ truncate(sourceLabel, 50) }}</span>
    </div>
    <button class="reset-btn" @click="$emit('reset')" title="Analyze a new document">
      <svg viewBox="0 0 16 16" fill="none">
        <path d="M2 8A6 6 0 1 0 8 2" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
        <path d="M2 4v4h4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      New document
    </button>
  </div>
</template>

<script setup>
defineProps({
  sourceType: { type: String, default: 'pdf' },
  sourceLabel: { type: String, default: '' },
})
defineEmits(['reset'])

function truncate(str, len) {
  if (!str) return ''
  return str.length > len ? str.slice(0, len) + '…' : str
}
</script>

<style scoped>
.chat-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.85rem 1.25rem;
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
  gap: 0.75rem;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  min-width: 0;
}

.badge {
  padding: 0.2rem 0.55rem;
  border-radius: 6px;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  flex-shrink: 0;
}

.badge.pdf {
  background: rgba(79, 70, 229, 0.1);
  color: var(--indigo);
  border: 1px solid rgba(79, 70, 229, 0.35);
}

.badge.url {
  background: rgba(2, 132, 199, 0.1);
  color: var(--accent-dim);
  border: 1px solid rgba(2, 132, 199, 0.35);
}

.source-label {
  font-size: 0.82rem;
  color: var(--text-muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.reset-btn {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.35rem 0.75rem;
  background: transparent;
  border: 1px solid var(--border);
  border-radius: 7px;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 0.82rem;
  white-space: nowrap;
  transition: all 0.2s;
  flex-shrink: 0;
  font-family: inherit;
}

.reset-btn:hover {
  color: var(--text);
  border-color: var(--border-hover);
  background: var(--surface-2);
}

.reset-btn svg {
  width: 13px;
  height: 13px;
}
</style>
