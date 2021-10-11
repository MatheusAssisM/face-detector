export const actions = {
  async findFaces({_}, file) {
    try {
      const formData = new FormData();
      formData.append('image', file);
      const result = await this.$faceAPI.post(
        '/face-predictor/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      )
      return result.data || []
    } catch (error) {
      return null
    }
  }
}