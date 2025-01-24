<template>
  <nav class="navbar">
    <ul class="navbar-links">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/admin">Admin</router-link></li>
      <li><router-link to="/about">About</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>

<style scoped>
.navbar {
  background-color: #6a0dad; /* Purple */
  color: white;
  padding: 1rem;
  width: 100%; /* Ensure it spans the full width */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Optional shadow for appearance */
}

.navbar-links {
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.navbar-links a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.2rem;
  transition: color 0.3s;
}

.navbar-links a:hover {
  color: teal; /* Teal on hover */
}
</style>
