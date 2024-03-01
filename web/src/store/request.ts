import { defineStore } from 'pinia'

export type ErrorType = { status: number | boolean, message?: string }
export type AlertType = { delay: number, message: string, type: 'success' | 'error' | 'warning' | 'info', id: number }
export type AlertItemType = Omit<AlertType, 'delay'>
let alertCount = 0;

export const useRequestStore = defineStore('request', {
  state: () => {
    const loadingNames: {
      [key: string]: boolean
    } = {}
    const alerts: Record<number, Partial<AlertType>> = {}
    return {
      loadingCount: 0, // 加载数
      loadingNames, // 加载中的请求
      alerts, // 提示
    }
  },
  actions: {
    startLoading(loadingName?: string) {
      if (loadingName) {
        this.loadingCount++
        this.loadingNames[loadingName] = true
      }
    },
    finishLoading(loadingName?: string) {
      if (loadingName) {
        this.loadingCount--
        delete this.loadingNames[loadingName]
      }
    },
    clearLoading() {
      this.loadingCount = 0
      this.loadingNames = {}
    },
    deleteAlert(id: number) {
      delete this.alerts[id]
    },
    setAlert(data: Partial<AlertType>) {
      const { message, type, delay } = data
      if (message) {
        const id = alertCount++;
        this.alerts = {
          ...this.alerts,
          [id]: {
            message,
            type: type || 'info',
            id
          }
        }
        const timer = setTimeout(() => {
          clearTimeout(timer)
          if (this.alerts[id]) {
            delete this.alerts[id]
          }
        }, delay || 3000)
      }
    }
  },
  getters: {
    isLoadingByName: (state) => (loadingName: string) => {
      return state.loadingNames[loadingName]
    },
    isLoading: (state) => () => {
      return state.loadingCount > 0
    },
    getAlerts: (state) => {
      return state.alerts
    }
  }
})