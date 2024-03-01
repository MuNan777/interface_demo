import { axiosWithLoadingName } from "../config/axios"
import { IBaseResp, IListData } from "../types"

export interface IUser {
  uid: number,
  name: string,
  gender: number
}

export const getUsers = async () => {
  const res = await axiosWithLoadingName<IListData<IUser>>(
    '/user/list',
    'user-list',
    { method: 'get' }
  )
  return res
}

export const getUsersPage = async (page: number, pageSize: number) => {
  const res = await axiosWithLoadingName<IListData<IUser>>(
    '/user/page',
    'user-page',
    { method: 'get', params: { page, pageSize } }
  )
  return res
}

export const getUserById = async (id: number) => {
  const res = await axiosWithLoadingName<IBaseResp<IUser>>(
    `/user/${id}`,
    'user-get',
    { method: 'get' }
  )
  return res
}

export const createUser = async (user: Omit<IUser, 'uid'>) => {
  const res = await axiosWithLoadingName<IBaseResp<IUser>>(
    `/user/`,
    'create-user',
    { method: 'post', data: user }
  )
  return res
}

export const editUser = async (user: IUser) => {
  const res = await axiosWithLoadingName<IBaseResp<IUser>>(
    `/user/${user.uid}`,
    'create-user',
    { method: 'post', data: user }
  )
  return res
}


export const removeUser = async (id: number) => {
  const res = await axiosWithLoadingName<IBaseResp<null>>(
    `/user/${id}`,
    'remove-user',
    { method: 'delete' }
  )
  return res
}