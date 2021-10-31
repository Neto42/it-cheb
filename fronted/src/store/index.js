import {createStore} from 'vuex'
import {HTTP} from "../api/common";

export default createStore({
    state: {
        result: []
    },
    mutations: {
        updateResult(state, result) {
            state.result = result
        }
    },
    actions: {
        results({commit}, url) {
            HTTP.get(url)
                .then(resp => {
                    commit('updateResult', resp.data)
                })
                .catch(err => {
                    console.log(err)
                })
        }
    },
    getters: {
        allResults(state) {
            return state.result
        }
    }
})
