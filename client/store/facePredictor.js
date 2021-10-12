import CustomError from "../utils/customError";

export const actions = {
  async findFaces({ dispatch }, file) {
    try {
      if (!file) {
        throw new CustomError('Selecione um arquivo!');
      }
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
      return dispatch('validateResult', result)
    } catch (error) {
      if ( error instanceof Error) {
        throw new CustomError('Algo deu errado!');
      }
      throw error
    }
  },

  validateResult ({_}, result) {
    if (!result?.data?.result || !result?.data) {
      throw new CustomError('Nenhum rosto encontrado!')
    }
    return result?.data || []
  }
}