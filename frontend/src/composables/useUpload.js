import { ref, watch } from 'vue'
import api from '../api'

export function useUpload() {
  const activeTab = ref('pdf')
  const selectedFile = ref(null)
  const url = ref('')
  const loading = ref(false)
  const uploadError = ref('')
  const urlError = ref('')

  watch(activeTab, () => {
    uploadError.value = ''
    urlError.value = ''
    selectedFile.value = null
    url.value = ''
  })

  function setFile(file) {
    if (!file) return
    if (file.type === 'application/pdf') {
      selectedFile.value = file
      uploadError.value = ''
    } else {
      uploadError.value = 'Please select a valid PDF file.'
    }
  }

  function clearFile() {
    selectedFile.value = null
    uploadError.value = ''
  }

  async function submitPdf() {
    if (!selectedFile.value || loading.value) return null
    loading.value = true
    uploadError.value = ''
    try {
      const form = new FormData()
      form.append('file', selectedFile.value)
      const res = await api.uploadPdf(form)
      return { ...res, label: selectedFile.value.name }
    } catch (err) {
      uploadError.value = err.response?.data?.detail || err.message || 'Upload failed.'
      return null
    } finally {
      loading.value = false
    }
  }

  async function submitUrl() {
    if (!url.value.trim() || loading.value) return null
    urlError.value = ''
    try {
      new URL(url.value)
    } catch {
      urlError.value = 'Please enter a valid URL.'
      return null
    }
    loading.value = true
    try {
      const res = await api.uploadUrl(url.value.trim())
      return { ...res, label: url.value.trim() }
    } catch (err) {
      urlError.value = err.response?.data?.detail || err.message || 'Failed to fetch URL.'
      return null
    } finally {
      loading.value = false
    }
  }

  return {
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
  }
}
