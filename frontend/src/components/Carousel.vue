<template>
  <div class="carousel">
    <div
      v-for="(slide, index) in slides"
      :key="index"
      class="carousel-slide"
      :class="{ active: currentIndex === index }"
    >
      <img :src="slide.image" :alt="slide.alt" />
      <h2>{{ slide.caption }}</h2>
    </div>
    <button @click="prevSlide" class="carousel-control prev">❮</button>
    <button @click="nextSlide" class="carousel-control next">❯</button>
  </div>
</template>

<script>
export default {
  name: 'Carousel',
  data() {
    return {
      currentIndex: 0,
      slides: [
        { image: '/images/RyomaBattle.png', caption: 'Welcome to Our Blog', alt: 'Slide 1' },
        { image: '/images/RyomaLove.png', caption: 'Discover New Insights', alt: 'Slide 2' },
        { image: '/images/RyomaShop1.png', caption: 'Stay Updated', alt: 'Slide 3' },
        { image: '/images/shop.png', caption: 'Our Shop', alt: 'Slide 4' },
      ],
    }
  },
  methods: {
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.slides.length
    },
    prevSlide() {
      this.currentIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length
    },
  },
}
</script>

<style scoped>
.carousel {
  position: relative;
  width: 100%;
  height: 400px; /* Set carousel height */
  overflow: hidden;
}

.carousel-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0; /* Hidden by default */
  transition: opacity 0.5s ease-in-out; /* Smooth transition effect */
}

.carousel-slide.active {
  opacity: 1; /* Show the active slide */
  z-index: 1;
}

.carousel img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* Ensure images fill the carousel area */
}

.carousel h2 {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.6);
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 1.2rem;
}

.carousel-control {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  cursor: pointer;
  padding: 10px 20px;
  border-radius: 50%;
  font-size: 1.5rem;
  z-index: 2;
}

.carousel-control.prev {
  left: 20px;
}

.carousel-control.next {
  right: 20px;
}
</style>
