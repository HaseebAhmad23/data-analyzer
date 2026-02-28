<template>
  <div class="data-input">
    <div class="hero">
      <h2>Analyze your data with AI</h2>
      <p class="subtitle">Choose a source, upload or enter a URL, and start asking questions.</p>
    </div>

    <SourceSelector v-model="activeTab" />

    <transition name="panel-slide" mode="out-in">
      <div v-if="activeTab === 'pdf'" key="pdf" class="panel">
        <FileDropzone
          :file="selectedFile"
          :error="uploadError"
          @select="setFile"
          @clear="clearFile"
        />
        <p v-if="uploadError" class="error-text">
          <svg viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.2"/><path d="M8 5v4M8 11v.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
          {{ uploadError }}
        </p>
        <button class="submit-btn" :disabled="!selectedFile || loading" @click="handlePdfSubmit">
          <span v-if="loading" class="btn-spinner"></span>
          <span>{{ loading ? 'Processing PDF…' : 'Upload & Start Chat' }}</span>
        </button>
      </div>

      <div v-else key="url" class="panel">
        <UrlSubmitter v-model="url" :loading="loading" @submit="handleUrlSubmit" />
        <p v-if="urlError" class="error-text">
          <svg viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.2"/><path d="M8 5v4M8 11v.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
          {{ urlError }}
        </p>
        <button class="submit-btn" :disabled="!url.trim() || loading" @click="handleUrlSubmit">
          <span v-if="loading" class="btn-spinner"></span>
          <span>{{ loading ? 'Fetching page…' : 'Fetch & Start Chat' }}</span>
        </button>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { useUpload } from '../composables/useUpload'
import SourceSelector from './upload/SourceSelector.vue'
import FileDropzone from './upload/FileDropzone.vue'
import UrlSubmitter from './upload/UrlSubmitter.vue'

const emit = defineEmits(['data-ready'])

const {
  activeTab,
  selectedFile,
  url,
  loading,
  uploadError,
  urlError,
  setFile,
  clearFile,
  submitPdf,
  submitUrl,
} = useUpload()

async function handlePdfSubmit() {
  const result = await submitPdf()
  if (result) emit('data-ready', result)
}

async function handleUrlSubmit() {
  const result = await submitUrl()
  if (result) emit('data-ready', result)
}
</script>

<style scoped>
.data-input {
  display: flex;
  flex-direction: column;
  gap: 1.75rem;
}

.hero {
  text-align: center;
  padding-top: 0.5rem;
}

h2 {
  font-size: 1.6rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  background: linear-gradient(90deg, var(--accent-dim), var(--indigo));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.subtitle {
  margin-top: 0.4rem;
  color: var(--text-muted);
  font-size: 0.9rem;
}

.panel {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
}

.submit-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  width: 100%;
  padding: 0.85rem;
  background: linear-gradient(135deg, var(--accent-dim), var(--indigo));
  border: none;
  border-radius: 10px;
  color: #fff;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.1s;
  font-family: inherit;
}

.submit-btn:hover:not(:disabled) {
  opacity: 0.9;
  transform: translateY(-1px);
}

.submit-btn:active:not(:disabled) {
  transform: translateY(0);
}

.submit-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
  transform: none;
}

.btn-spinner {
  width: 14px;
  height: 14px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: #fff;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
  flex-shrink: 0;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-text {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: var(--error);
  font-size: 0.85rem;
}

.error-text svg {
  width: 14px;
  height: 14px;
  flex-shrink: 0;
}

.panel-slide-enter-active,
.panel-slide-leave-active {
  transition: opacity 0.15s ease, transform 0.15s ease;
}
.panel-slide-enter-from {
  opacity: 0;
  transform: translateX(8px);
}
.panel-slide-leave-to {
  opacity: 0;
  transform: translateX(-8px);
}
</style>
