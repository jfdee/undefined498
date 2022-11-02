import ajax from 'axios'

export default ({
    install(Vue){
        Vue.prototype.$ajax = ajax
    }
})