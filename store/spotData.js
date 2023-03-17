import axios from 'axios'

export const state = () => ({
    spotData: []
})

export const getters = {
    getSpotData: state => state.spotData
}

export const mutations = {
    setSpotData(state, data) {
        state.spotData = data;
    }
}

export const actions = {
    async onLoadSpotData({ commit, state }, { spotsId }) {
        this.$axios.get("/api/spot_data/" + spotsId)
        .then((response) => {
            commit('setSpotData', response.data);
        })   
    }
}