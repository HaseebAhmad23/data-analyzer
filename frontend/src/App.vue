<template>
  <div class="app">
    <AppHeader />

    <main class="main">
      <transition name="fade" mode="out-in">
        <DataInput
          v-if="!sessionId"
          key="input"
          @data-ready="onDataReady"
        />
        <ChatArea
          v-else
          key="chat"
          :session-id="sessionId"
          :source-type="sourceType"
          :source-label="sourceLabel"
          @reset="onReset"
        />
      </transition>
    </main>

    <AppFooter />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import AppHeader from './components/layout/AppHeader.vue'
import AppFooter from './components/layout/AppFooter.vue'
import DataInput from './components/DataInput.vue'
import ChatArea from './components/ChatArea.vue'

const sessionId = ref(null)
const sourceType = ref(null)
const sourceLabel = ref(null)

function onDataReady({ session_id, source_type, label }) {
  sessionId.value = session_id
  sourceType.value = source_type
  sourceLabel.value = label
}

function onReset() {
  sessionId.value = null
  sourceType.value = null
  sourceLabel.value = null
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --bg: #f0f4f8;
  --surface: #ffffff;
  --surface-2: #e2e8f0;
  --border: #c2cfe0;
  --border-hover: #7a9ab8;
  --text: #0f172a;
  --text-muted: #4a6281;
  --text-faint: #8fa3bc;
  --accent: #0284c7;
  --accent-dim: #0369a1;
  --accent-glow: rgba(2, 132, 199, 0.12);
  --indigo: #4f46e5;
  --error: #dc2626;
  --success: #059669;
  --user-bubble: #1d4ed8;
  --radius: 12px;
}

html { scroll-behavior: smooth; }

body {
  font-family: 'IBM Plex Sans', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: var(--border-hover); }

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main {
  flex: 1;
  max-width: 860px;
  width: 100%;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(8px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>
