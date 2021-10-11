export default ({ $axios }, inject) => {
  const faceApi = $axios.create({
    baseURL: 'http://localhost:8000',
  })

  inject('faceAPI', faceApi)
}