import axios from 'axios'

const baseURL = import.meta.env.VITE_API_BASE_URL || ''

const client = axios.create({
  baseURL,
  timeout: 180000,
  headers: { 'Content-Type': 'application/json' },
})

export default {
  async uploadPdf(formData) {
    const { data } = await client.post('/api/upload/pdf', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    return data
  },

  async uploadUrl(url) {
    const { data } = await client.post('/api/upload/url', { url })
    return data
  },

  async chat(sessionId, message) {
    const { data } = await client.post('/api/chat', { session_id: sessionId, message })
    return data
  },
}
