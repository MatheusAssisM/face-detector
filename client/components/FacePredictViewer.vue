<template>
  <b-container fluid class="p-4 bg-dark">
  <b-row>
    <b-col>
      <b-img 
        v-for="base64 of images"
        :key="base64"
        thumbnail 
        fluid 
        :src="`data:image/jpg;base64, ${base64}`" 
        alt="Image 1"
      />
    </b-col>
  </b-row>
</b-container>
</template>

<script>
export default {
  data () {
    return {
      images: []
    }
  },

  mounted () {
    this.$bus.$on('show-image', this.showImages)
  },

  methods: {
    showImages (imagesBase64) {
      this.images = imagesBase64
    }
  }
}
</script>

<style scoped>

</style>