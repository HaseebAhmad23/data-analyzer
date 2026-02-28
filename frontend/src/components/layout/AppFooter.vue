<template>
  <footer class="app-footer">
    <span>Data Analyzer &copy; {{ year }} Haseeb Studios</span>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear()
</script>

<style scoped>
.app-footer {
  text-align: center;
  padding: 1rem;
  color: var(--text-faint);
  font-size: 0.78rem;
  border-top: 1px solid var(--border);
}
</style>
