import axios from 'axios'

export const state = () => ({
    settingData: ""
})

export const getters = {
    getSettingData: state => state.settingData
}

export const mutations = {
    setSettingData(state, data) {
        state.settingData = data;
    }
}

export const actions = {
    async onLoadSettingData({ commit, state }, { spotsName }) {
        commit('setSettingData', spotsName);
    }
}