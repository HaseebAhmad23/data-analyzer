<template>
  <header class="app-header">
    <div class="header-inner">
      <div class="logo">
        <svg class="logo-icon" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="28" height="28" rx="7" fill="url(#logo-grad)"/>
          <path d="M7 9h14v2H7V9zm0 4h10v2H7v-2zm0 4h8v2H7v-2z" fill="#fff"/>
          <circle cx="20" cy="19" r="3.5" fill="#f97316"/>
          <defs>
            <linearGradient id="logo-grad" x1="0" y1="0" x2="28" y2="28" gradientUnits="userSpaceOnUse">
              <stop stop-color="#0ea5e9"/>
              <stop offset="1" stop-color="#6366f1"/>
            </linearGradient>
          </defs>
        </svg>
        <h1 class="logo-text">Data Analyzer</h1>
      </div>
      <p class="tagline">Upload a PDF or paste a URL — then ask anything about your data.</p>
    </div>
  </header>
</template>

<style scoped>
.app-header {
  position: sticky;
  top: 0;
  z-index: 10;
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  background: color-mix(in srgb, var(--bg) 88%, transparent);
  border-bottom: 1px solid var(--border);
}

.header-inner {
  max-width: 860px;
  margin: 0 auto;
  padding: 1rem 1.5rem;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.logo-icon {
  width: 28px;
  height: 28px;
  flex-shrink: 0;
}

.logo-text {
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  background: linear-gradient(90deg, var(--accent), var(--indigo));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.tagline {
  margin-top: 0.3rem;
  color: var(--text-muted);
  font-size: 0.85rem;
}
</style>
