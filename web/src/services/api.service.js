import axios from 'axios'

import TokenService from './token.service'


const ApiService = {
    init(base_url) {
        axios.defaults.baseURL=base_url
    },

    set_access_token() {
        axios.defaults.headers.common["Authorization"] = 
        `Bearer ${TokenService.get_token()}`
    },

    get(resource) {
        return axios.get(resource)
    },

    delete(resource) {
        return axios.delete(resource)
    },

    post(resource, data) {
        return axios.post(resource, data)
    },

    put(resource, data) {
        return axios.put(resource, data)
    },

    make_custom_request(request_config) {
        return axios(request_config)
    }
}

export default ApiService