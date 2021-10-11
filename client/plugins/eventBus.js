import Vue from 'vue'

export default ({_}, inject) => {
  const bus = new Vue()
  inject('bus', bus);
}