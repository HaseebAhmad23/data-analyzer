<template>
  <div class="source-cards">
    <button
      v-for="tab in tabs"
      :key="tab.id"
      :class="['source-card', { active: modelValue === tab.id }]"
      @click="$emit('update:modelValue', tab.id)"
    >
      <span class="source-icon" v-html="tab.icon"></span>
      <span class="source-label">{{ tab.label }}</span>
      <span class="source-desc">{{ tab.desc }}</span>
    </button>
  </div>
</template>

<script setup>
defineProps({ modelValue: { type: String, required: true } })
defineEmits(['update:modelValue'])

const tabs = [
  {
    id: 'pdf',
    label: 'PDF Document',
    desc: 'Upload a local PDF file',
    icon: `<svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M5 18V4a1 1 0 011-1h7l4 4v11a1 1 0 01-1 1H6a1 1 0 01-1-1z" stroke="currentColor" stroke-width="1.4" fill="none"/>
      <path d="M13 3v4h4" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/>
      <path d="M7 11h6M7 14h4" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
    </svg>`,
  },
  {
    id: 'url',
    label: 'Website URL',
    desc: 'Paste any web page link',
    icon: `<svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="10" cy="10" r="8" stroke="currentColor" stroke-width="1.4"/>
      <path d="M2 10h16M10 2c-2 2.5-3 5-3 8s1 5.5 3 8M10 2c2 2.5 3 5 3 8s-1 5.5-3 8" stroke="currentColor" stroke-width="1.3"/>
    </svg>`,
  },
]
</script>

<style scoped>
.source-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
}

.source-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  padding: 1.25rem;
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: var(--radius);
  cursor: pointer;
  text-align: center;
  transition: all 0.2s ease;
  color: var(--text-muted);
  font-family: inherit;
}

.source-card:hover {
  border-color: var(--border-hover);
  color: var(--text);
  background: var(--surface-2);
}

.source-card.active {
  border-color: var(--accent);
  background: var(--accent-glow);
  color: var(--text);
  box-shadow: 0 0 0 1px var(--accent);
}

.source-icon {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.source-icon :deep(svg) {
  width: 22px;
  height: 22px;
}

.source-label {
  font-size: 0.9rem;
  font-weight: 600;
}

.source-desc {
  font-size: 0.78rem;
  color: var(--text-muted);
}

.source-card.active .source-desc {
  color: var(--accent);
}
</style>
