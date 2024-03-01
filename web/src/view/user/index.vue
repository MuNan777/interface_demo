<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import { createUser, editUser, getUserById, getUsersPage, IUser, removeUser } from '../../api/user'
import DataTable, { ITHeaderItem } from '../../components/DataTable/index.vue'
import ConfirmDialogs from '../../components/Dialogs/ConfirmDialogs.vue'
import UserDetail from './detail.vue'
import Pagination, { IPageData } from '../../components/Pagination/index.vue'

export default defineComponent({
  components: {
    DataTable,
    ConfirmDialogs,
    UserDetail,
    Pagination
  },
  setup() {
    const users = ref<IUser[]>([])
    // 用户列表
    const page = ref(1)
    const pageSize = ref(10)
    const total = ref(0)
    // 获取用户列表
    const refreshUserList = async () => {
      const res = await getUsersPage(page.value, pageSize.value)
      users.value = res.list
      total.value = res.count
    }
    onMounted(async () => {
      await refreshUserList()
    })
    const headers = ref<ITHeaderItem[]>([])
    // 表头
    headers.value = [
      {
        name: 'uid',
        type: 'text',
        label: 'ID'
      },
      {
        name: 'name',
        type: 'text',
        label: 'Name'
      },
      {
        name: 'gender',
        type: 'text',
        label: 'Gender',
        // 自定义处理函数
        handler: (value: number) => {
          return value === 0 ? 'male' : 'female'
        }
      },
      {
        name: 'action',
        type: 'slot',
        label: 'Action'
      }
    ]
    const actionId = ref(0)
    const show = ref(false)
    // 显示删除弹出框
    const showDelete = (id: number) => {
      show.value = true
      actionId.value = id
    }
    // 删除用户
    const handleDelete = async () => {
      const res = await removeUser(actionId.value)
      await refreshUserList()
      console.log(res)
    }
    const userData = ref<IUser>({} as any)
    const showDialogs = ref(false)
    const isDetail = ref(false)
    // 打开新增或者编辑弹出框
    const handleAction = async (id: number | null, disabled?: boolean) => {
      // 如果id不为空，说明是编辑
      if (id != null) {
        const res = await getUserById(id)
        userData.value = res.data
      } else {
        userData.value = { name: '', gender: 0 } as IUser
      }
      isDetail.value = !!disabled
      showDialogs.value = true
    }
    // 处理新增或者编辑
    const handleCreateOrUpdate = async (user: IUser) => {
      // 如果id不为空，说明是编辑
      if (user.uid) {
        await editUser(user)
      } else {
        await createUser({ name: user.name, gender: user.gender })
      }
      showDialogs.value = false
      await refreshUserList()
    }
    // 分页
    const pageChange = (data: IPageData) => {
      page.value = data.page
      pageSize.value = data.pageSize
      refreshUserList()
    }
    return {
      users,
      headers,
      show,
      showDialogs,
      userData,
      isDetail,
      page,
      pageSize,
      total,
      pageChange,
      showDelete,
      handleDelete,
      handleAction,
      handleCreateOrUpdate
    }
  },
}) 
</script>
<template>
  <div class="mt-20 mx-auto w-[80%]">
    <div class="my-3 flex items-center justify-between">
      <div class="font-bold text-xl">User</div>
      <div>
        <button @click="() => handleAction(null, false)"
          class="bg-primary hover:bg-primary1 inline-flex w-full justify-center rounded-md px-5 sm:ml-5 py-2  text-sm font-semibold text-white shadow-lg m:ml-3 sm:w-auto">
          <span class=" i-lucide-plus"></span>
          Add
        </button>
      </div>
    </div>
    <DataTable :headers="headers" :data="users">
      <template #action="{ item }">
        <div class="flex space-x-2">
          <div class="flex items-center space-x-3.5">
            <button @click="() => handleAction(item.uid, true)" class="hover:border-strokedark">
              <span class=" i-lucide-view"></span>
            </button>
            <button @click="() => handleAction(item.uid, false)" class="hover:border-strokedark">
              <span class=" i-lucide-edit"></span>
            </button>
            <button class="hover:border-strokedark">
              <span @click="() => showDelete(item.uid)" class=" i-lucide-delete"></span>
            </button>
          </div>
        </div>
      </template>
    </DataTable>
    <Pagination :page="page" :pageSize="pageSize" :total="total" @change="pageChange" />
    <ConfirmDialogs v-model:show="show" type="danger" @confirm="handleDelete">
      <template #title>
        Delete confirmation
      </template>
      <template #body>
        Are you sure you want to delete this user?
      </template>
    </ConfirmDialogs>
    <UserDetail v-model:show="showDialogs" v-model:user="userData" :disabled="isDetail" @confirm="handleCreateOrUpdate" />
  </div>
</template>
