
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'



export const store = new Vuex.Store({
    plugins: [createPersistedState({
        storage: window.sessionStorage,
    })],
    state: {
      pk_change: false,
      current_user : '',
      side_bar : false,
      page : 'Welcome',
      home_cols : 10,
      home_dir : "center",
      url : 'http://127.0.0.1:8000/',
      api_url : 'http://127.0.0.1:8000/api/'
    },

    mutations: {
    //init all the state
    init (state) {
      state.pk_change = false,
      state.current_user = '',
      state.side_bar = false,
      state.page = 'Welcome',
      state.home_cols = 10,
      state.admin = false,
      state.url = 'http://127.0.0.1:8000/',
      state.api_url = 'http://127.0.0.1:8000/api/'
    },
    //the pk mutation method
      set_pk_change (state, value) {
        state.pk_change = value
      },
   
    //the side_bar mutation methods
    //1
      change_side_bar(state){
          state.side_bar = !state.side_bar
      },
    //2
      set_side_bar(state, value){
            state.side_bar = value
      },
    //set the current page
      set_page(state, value){
          state.page = value
      },
      //the home cols mutation method
      set_home_cols (state, value) {
        state.home_cols = value
      },
      //the home dir mutation method
      set_home_dir (state, value) {
        state.home_dir = value
      },
      //the admin mutation method
      set_admin (state, value) {
        state.admin = value
      }
    }
  })