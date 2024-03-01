import axios, { AxiosError, AxiosRequestConfig, AxiosResponse } from 'axios'
import { useRequestStore } from '../store/request'
import { IBaseResp } from '../types'

export type loadingAxiosRequestConfig = AxiosRequestConfig & { loadingName?: string }

const loadAxiosInterceptor = () => {
  const requestStore = useRequestStore()
  axios.interceptors.request.use(config => {
    const { loadingName } = config as loadingAxiosRequestConfig
    requestStore.startLoading(loadingName)
    return config
  })
  axios.interceptors.response.use((resp: AxiosResponse<IBaseResp>) => {
    const { config, data } = resp
    const { loadingName } = config as loadingAxiosRequestConfig
    requestStore.finishLoading(loadingName)
    const { errno, message } = data
    if (errno !== 0) {
      requestStore.setAlert({ message, type: 'error' })
      return Promise.reject(data)
    } else {
      requestStore.setAlert({ message, type: 'success' })
    }
    return resp
  }, (e: AxiosError) => {
    if (e.message === 'Network Error') {
      requestStore.setAlert({ message: '网络错误', type: 'error' })
    }
    console.log(e)
    if (e.config) {
      const { loadingName } = e.config as loadingAxiosRequestConfig
      requestStore.finishLoading(loadingName)
    }
    // ElMessage.error(e.message)
    return Promise.reject(e)
  })
}



export default loadAxiosInterceptor