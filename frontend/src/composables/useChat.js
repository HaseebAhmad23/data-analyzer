import { ref, nextTick } from 'vue'
import api from '../api'

export function useChat(sessionId) {
  const messages = ref([])
  const input = ref('')
  const loading = ref(false)
  const messagesEl = ref(null)

  function scrollToBottom() {
    nextTick(() => {
      if (messagesEl.value) {
        messagesEl.value.scrollTop = messagesEl.value.scrollHeight
      }
    })
  }

  async function send() {
    const text = input.value.trim()
    if (!text || loading.value) return

    messages.value.push({ role: 'user', content: text })
    input.value = ''
    loading.value = true
    scrollToBottom()

    try {
      const res = await api.chat(sessionId, text)
      messages.value.push({ role: 'assistant', content: res.response })
    } catch (err) {
      const msg = err.response?.data?.detail || err.message || 'Failed to get response.'
      messages.value.push({ role: 'assistant', content: `Error: ${msg}` })
    } finally {
      loading.value = false
      scrollToBottom()
    }
  }

  return { messages, input, loading, messagesEl, send }
}
