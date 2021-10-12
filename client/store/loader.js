export const state = () => ({
  isLoading: false,
})

export const mutations = {
  set (state, [key, value]) {
    state[key] = value
  }
}

export const actions = {
  switchLoader ({commit, state}) {
    commit('set', ['isLoading', !state.isLoading])
  }
}