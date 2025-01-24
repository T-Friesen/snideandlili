<template>
  <div class="admin-panel">
    <h1>Admin Panel</h1>

    <!-- Post List -->
    <div v-if="posts.length" class="post-list">
      <h2>Manage Blog Posts</h2>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Created At</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="post in posts" :key="post.id">
            <td>{{ post.title }}</td>
            <td>{{ getAuthorName(post.author) }}</td>
            <td>{{ formatDate(post.created_at) }}</td>
            <td>
              <button @click="editPost(post)" class="edit-btn">Edit</button>
              <button @click="deletePost(post.id)" class="delete-btn">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Create/Edit Post Form -->
    <div class="post-form">
      <h2>{{ editMode ? 'Edit Post' : 'Create New Post' }}</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="title">Title</label>
          <input
            id="title"
            v-model="form.title"
            type="text"
            placeholder="Enter the post title"
            required
          />
        </div>
        <div class="form-group">
          <label for="short_description">Short Description</label>
          <textarea
            id="short_description"
            v-model="form.short_description"
            placeholder="Write a short description"
            required
          ></textarea>
        </div>
        <div class="form-group">
          <label for="description">Description</label>
          <textarea
            id="description"
            v-model="form.description"
            placeholder="Write the full post description"
            required
          ></textarea>
        </div>
        <div class="form-group">
          <label for="post_image">Post Image</label>
          <div
            class="image-upload"
            @dragover.prevent
            @drop.prevent="handleImageDrop"
            @click="triggerFileInput"
          >
            <p v-if="!form.post_image">Drag & Drop or Click to Upload</p>
            <img v-if="form.post_imagePreview" :src="form.post_imagePreview" alt="Preview" />
            <input
              id="post_image"
              type="file"
              @change="handleImageUpload"
              accept="image/*"
              hidden
            />
          </div>
        </div>
        <div class="form-group">
          <label for="author">Author</label>
          <select id="author" v-model="form.author" required>
            <option v-for="author in authors" :key="author.id" :value="author.id">
              {{ author.user }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="tags">Tags</label>
          <select id="tags" v-model="form.tags" multiple>
            <option v-for="tag in tags" :key="tag.id" :value="tag.id">
              {{ tag.name }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="categories">Categories</label>
          <select id="categories" v-model="form.categories" multiple>
            <option v-for="category in categories" :key="category.id" :value="category.id">
              {{ category.name }}
            </option>
          </select>
        </div>
        <div class="form-actions">
          <button type="submit" class="primary-btn">
            {{ editMode ? 'Update Post' : 'Create Post' }}
          </button>
          <button type="button" v-if="editMode" @click="cancelEdit" class="secondary-btn">
            Cancel
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AdminPanel',
  data() {
    return {
      posts: [],
      authors: [],
      tags: [],
      categories: [],
      form: {
        id: null,
        title: '',
        short_description: '',
        description: '',
        post_image: null,
        post_imagePreview: null,
        author: '',
        tags: [],
        categories: [],
      },
      editMode: false,
    }
  },
  mounted() {
    this.fetchPosts()
    this.fetchAuthors()
    this.fetchTags()
    this.fetchCategories()
    // Set default author
    if (this.authors.length > 0) {
      this.form.author = this.authors[0].id
    }
  },
  methods: {
    fetchPosts() {
      axios.get('http://127.0.0.1:8000/api/posts/').then((response) => {
        this.posts = response.data
      })
    },
    fetchAuthors() {
      axios
        .get('http://127.0.0.1:8000/api/authors/')
        .then((response) => {
          this.authors = response.data
        })
        .catch((error) => {
          console.error('Error fetching authors:', error)
          alert('Failed to load authors. Please try again later.')
        })
    },
    fetchTags() {
      axios.get('http://127.0.0.1:8000/api/tags/').then((response) => {
        this.tags = response.data
      })
    },
    fetchCategories() {
      axios.get('http://127.0.0.1:8000/api/categories/').then((response) => {
        this.categories = response.data
      })
    },
    submitForm() {
      const formData = new FormData()
      Object.keys(this.form).forEach((key) => {
        if (key === 'tags' || key === 'categories') {
          formData.append(key, JSON.stringify(this.form[key]))
        } else {
          formData.append(key, this.form[key])
        }
      })

      if (this.editMode) {
        axios.put(`http://127.0.0.1:8000/api/posts/${this.form.id}/`, formData).then(() => {
          this.fetchPosts()
          this.resetForm()
        })
      } else {
        axios.post('http://127.0.0.1:8000/api/posts/', formData).then(() => {
          this.fetchPosts()
          this.resetForm()
        })
      }
    },
    handleImageUpload(event) {
      const file = event.target.files[0]
      this.form.post_image = file
      this.form.post_imagePreview = URL.createObjectURL(file)
    },
    handleImageDrop(event) {
      const file = event.dataTransfer.files[0]
      this.form.post_image = file
      this.form.post_imagePreview = URL.createObjectURL(file)
    },
    triggerFileInput() {
      document.getElementById('post_image').click()
    },
    deletePost(postId) {
      if (confirm('Are you sure?')) {
        axios.delete(`http://127.0.0.1:8000/api/posts/${postId}/`).then(() => {
          this.fetchPosts()
        })
      }
    },
    editPost(post) {
      this.editMode = true
      this.form = { ...post, post_imagePreview: post.post_image }
    },
    cancelEdit() {
      this.resetForm()
    },
    resetForm() {
      this.form = {
        id: null,
        title: '',
        short_description: '',
        description: '',
        post_image: null,
        post_imagePreview: null,
        author: '',
        tags: [],
        categories: [],
      }
      this.editMode = false
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString()
    },
    getAuthorName(authorId) {
      const author = this.authors.find((a) => a.id === authorId)
      return author ? author.username : 'Unknown'
    },
  },
}
</script>

<style scoped>
.post-form {
  max-width: 600px;
  margin: 2rem auto;
  background: #f9f9f9;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
.form-group {
  margin-bottom: 1rem;
}
.form-group label {
  font-weight: bold;
  margin-bottom: 0.5rem;
  display: block;
}
.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-top: 0.5rem;
}
.image-upload {
  border: 2px dashed #ccc;
  border-radius: 8px;
  padding: 1rem;
  text-align: center;
  cursor: pointer;
  background: #fff;
}
.image-upload img {
  max-width: 100%;
  border-radius: 8px;
}
.primary-btn {
  background: #6a0dad;
  color: white;
  border: none;
  padding: 0.7rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}
.primary-btn:hover {
  background: teal;
}
.secondary-btn {
  background: #ddd;
  color: #333;
  border: none;
  padding: 0.7rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  margin-left: 1rem;
}
.secondary-btn:hover {
  background: #bbb;
}
</style>
