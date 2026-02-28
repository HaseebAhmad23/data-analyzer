<template>
  <div
    class="dropzone"
    :class="{ dragging: isDragging, error: !!error, 'has-file': !!file }"
    @dragover.prevent="isDragging = true"
    @dragleave="isDragging = false"
    @drop.prevent="onDrop"
    @click="fileInput.click()"
  >
    <input
      ref="fileInput"
      type="file"
      accept=".pdf,application/pdf"
      class="hidden"
      @change="onSelect"
    />

    <div v-if="!file" class="dz-empty">
      <span class="dz-icon">
        <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="40" height="40" rx="10" fill="var(--surface-2)"/>
          <path d="M13 28V14a2 2 0 012-2h8l6 6v10a2 2 0 01-2 2H15a2 2 0 01-2-2z" stroke="var(--accent)" stroke-width="1.5" fill="none"/>
          <path d="M23 12v6h6" stroke="var(--accent)" stroke-width="1.5" stroke-linejoin="round"/>
          <path d="M17 22h6M17 25h4" stroke="var(--text-muted)" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
      </span>
      <p class="dz-title">Drop your PDF here</p>
      <p class="dz-hint">or <span class="dz-link">click to browse</span></p>
      <p class="dz-meta">PDF files only &middot; Max 10 MB</p>
    </div>

    <div v-else class="dz-file">
      <span class="dz-file-icon">
        <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M8 30V6a2 2 0 012-2h10l6 6v20a2 2 0 01-2 2H10a2 2 0 01-2-2z" fill="var(--surface-2)" stroke="var(--success)" stroke-width="1.5"/>
          <path d="M20 4v6h6" stroke="var(--success)" stroke-width="1.5" stroke-linejoin="round"/>
        </svg>
      </span>
      <div class="dz-file-info">
        <p class="dz-file-name">{{ file.name }}</p>
        <p class="dz-file-size">{{ formatSize(file.size) }}</p>
      </div>
      <button class="dz-remove" @click.stop="$emit('clear')">
        <svg viewBox="0 0 16 16" fill="none">
          <path d="M4 4l8 8M12 4l-8 8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  file: { type: Object, default: null },
  error: { type: String, default: '' },
})
const emit = defineEmits(['select', 'clear'])

const fileInput = ref(null)
const isDragging = ref(false)

function onSelect(e) {
  const f = e.target.files?.[0]
  if (f) emit('select', f)
  e.target.value = ''
}

function onDrop(e) {
  isDragging.value = false
  const f = e.dataTransfer?.files?.[0]
  if (f) emit('select', f)
}

function formatSize(bytes) {
  if (bytes < 1024) return `${bytes} B`
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
}
</script>

<style scoped>
.dropzone {
  border: 1.5px dashed var(--border);
  border-radius: 10px;
  cursor: pointer;
  transition: border-color 0.2s, background 0.2s;
  min-height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.dropzone:hover,
.dropzone.dragging {
  border-color: var(--accent);
  background: var(--accent-glow);
}

.dropzone.error { border-color: var(--error); }

.dropzone.has-file {
  border-style: solid;
  border-color: var(--success);
  background: rgba(52, 211, 153, 0.05);
}

.dz-empty {
  text-align: center;
  padding: 2rem 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
}

.dz-icon {
  display: block;
  width: 40px;
  height: 40px;
  margin-bottom: 0.25rem;
}

.dz-title {
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--text);
}

.dz-hint {
  font-size: 0.85rem;
  color: var(--text-muted);
}

.dz-link {
  color: var(--accent);
  text-decoration: underline;
}

.dz-meta {
  font-size: 0.78rem;
  color: var(--text-faint);
  margin-top: 0.25rem;
}

.dz-file {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.25rem;
  width: 100%;
}

.dz-file-icon {
  width: 32px;
  height: 32px;
  flex-shrink: 0;
}

.dz-file-icon svg {
  width: 32px;
  height: 32px;
}

.dz-file-info { flex: 1; min-width: 0; }

.dz-file-name {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.dz-file-size {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 0.1rem;
}

.dz-remove {
  margin-left: auto;
  background: transparent;
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text-muted);
  cursor: pointer;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  flex-shrink: 0;
}

.dz-remove:hover {
  color: var(--error);
  border-color: var(--error);
}

.dz-remove svg {
  width: 12px;
  height: 12px;
}

.hidden { display: none; }
</style>
