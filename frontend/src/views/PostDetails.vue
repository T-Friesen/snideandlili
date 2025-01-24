<template>
  <div class="post-details">
    <!-- Display only if the post is loaded -->
    <div v-if="post">
      <h1>{{ post.title }}</h1>
      <img :src="post.post_image" alt="Post Image" class="post-image" />
      <p class="post-description" v-html="post.description"></p>

      <!-- Metadata Section -->
      <div class="post-meta">
        <p><strong>Author:</strong> {{ post.author }}</p>
        <p><strong>Published on:</strong> {{ formatDate(post.created_at) }}</p>
        <p v-if="post.tags.length">
          <strong>Tags:</strong>
          <span v-for="(tag, index) in post.tags" :key="index" class="tag">
            {{ tag.name }}
          </span>
        </p>
        <p v-if="post.categories.length">
          <strong>Categories:</strong>
          <span v-for="(category, index) in post.categories" :key="index" class="category">
            {{ category.name }}
          </span>
        </p>
      </div>
    </div>

    <!-- Error or Loading State -->
    <div v-else>
      <p>Loading post details...</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PostDetails',
  data() {
    return {
      post: null, // Single post data
    }
  },
  mounted() {
    const postId = this.$route.params.id // Get the post ID from the route
    axios
      .get(`http://127.0.0.1:8000/api/posts/${postId}/`) // Fetch the single post
      .then((response) => {
        this.post = response.data // Store the post data
      })
      .catch((error) => {
        console.error('Error fetching post:', error)
        this.post = null // Set post to null if an error occurs
      })
  },
  methods: {
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' }
      return new Date(date).toLocaleDateString(undefined, options)
    },
  },
}
</script>

<style scoped>
.post-details {
  padding: 1rem;
  max-width: 800px;
  margin: 0 auto;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.post-details h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.post-image {
  width: 100%;
  height: auto;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.post-description {
  font-size: 1.2rem;
  line-height: 1.8;
  margin-bottom: 1.5rem;
}

.post-meta {
  font-size: 1rem;
  color: #555;
}

.post-meta p {
  margin: 0.5rem 0;
}

.tag,
.category {
  display: inline-block;
  background-color: #6a0dad;
  color: white;
  padding: 0.2rem 0.5rem;
  margin-right: 0.5rem;
  border-radius: 4px;
  font-size: 0.9rem;
}
</style>
