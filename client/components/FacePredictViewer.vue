<template>
  <b-row class="mb-5">
    <b-col class="d-flex flex-column flex-sm-row justify-content-center">
        <b-img-lazy
          v-for="base64 of images"
          :key="base64"
          :src="`data:image/jpg;base64, ${base64}`"
          width="200"
          height="200"
          class="ml-2 mb-2"
        />
    </b-col>
  </b-row>
</template>

<script>
export default {
  data () {
    return {
      images: [],
      mainProps: {
        blank: false, 
        blankColor: '#777', 
        width: 100, 
        height: 100, 
        class: 'm-0' 
      }
    }
  },

  mounted () {
    this.$bus.$on('show-image', this.showImages)
    this.$bus.$on('clear-images', this.clearImages)
  },

  methods: {
    showImages (imagesBase64) {
      this.images = imagesBase64
    },

    clearImages () {
      this.images = []
    }
  }
}
</script>

<style scoped>
.images-box {
  gap: 1rem;
}
</style>