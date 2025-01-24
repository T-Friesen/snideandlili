<template>
  <div class="home">
    <h1>Welcome to Our Blog</h1>
    <p>Explore the latest posts below:</p>
    <ul>
      <li v-for="post in posts" :key="post.id" class="post-item">
        <img :src="post.post_image" alt="Post Image" />
        <h2>
          <router-link :to="`/post/${post.id}`">{{ post.title }}</router-link>
        </h2>
        <p>{{ post.short_description }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      posts: [], // Store blog posts here
    }
  },
  mounted() {
    // Fetch posts from the backend
    axios
      .get('http://127.0.0.1:8000/api/posts/') // Replace with your backend URL
      .then((response) => {
        this.posts = response.data // Store the list of blog posts
      })
      .catch((error) => {
        console.error('Error fetching posts:', error)
      })
  },
}
</script>

<style scoped>
.home {
  padding: 1rem;
}

.post-item {
  margin-bottom: 2rem;
  list-style: none;
}

.post-item img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin-bottom: 0.5rem;
}
</style>
