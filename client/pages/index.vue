<template>
  <div>
    <b-overlay :show="isLoading" rounded="sm">
      <b-row class="mt-5">
        <b-col class="d-flex justify-content-center" cols="12" >
          <FacePredictInput />
        </b-col>
        <b-col class="d-flex justify-content-center mt-5" cols="12">
          <FacePredictViewer />
        </b-col>
      </b-row>
    </b-overlay>
  </div>
</template>

<script>
export default {
  data () {
    return {}
  },

  computed: {
    isLoading () {
      return this.$store.state.loader.isLoading
    }
  }
}
</script>