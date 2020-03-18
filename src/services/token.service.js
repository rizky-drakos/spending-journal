const TOKEN_KEY = 'access_token'
    
const TokenService = {
    get_token() {
        return localStorage.getItem(TOKEN_KEY)
    },

    save_token(access_token) {
        localStorage.setItem(TOKEN_KEY, access_token)
    },

    remove_token() {
        localStorage.removeItem(TOKEN_KEY)
    }
}

export default TokenService