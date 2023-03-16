import axios from 'axios'

export const state = () => ({
    cameraData: []
})

export const getters = {
    getCameraData: state => state.cameraData
}

export const mutations = {
    setCameraData(state, data) {
        state.cameraData = data;
    }
}

export const actions = {
    async onLoadCameraData({ commit, state }, { spotsId }) {
        this.$axios.get("/api/camera_data/" + spotsId)
        .then((response) => {
            commit('setCameraData', response.data);
        })   
    }
}