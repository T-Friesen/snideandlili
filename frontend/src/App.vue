<template>
  <div id="app">
    <!-- Full-width Carousel -->
    <Carousel />

    <!-- Full-width Navbar -->
    <Navbar />

    <!-- Main Content Area -->
    <main class="content-container">
      <router-view />
    </main>

    <!-- Full-width Footer -->
    <Footer />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Carousel from './components/Carousel.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Carousel,
    Footer,
  },
}
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f8f8f8; /* Light background */
  color: #333; /* Dark text */
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Content Area */
.content-container {
  max-width: 1200px; /* Constrain content width */
  margin: 20px auto; /* Center content with vertical spacing */
  padding: 1rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for focus */
}
</style>
