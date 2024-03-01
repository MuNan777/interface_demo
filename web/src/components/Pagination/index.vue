<script lang="ts">
export interface IPageData { page: number, pageSize: number, total: number }

import { computed, defineComponent } from 'vue'
export default defineComponent({
  props: {
    page: {
      type: Number,
      required: true
    },
    total: {
      type: Number,
      required: true
    },
    pageSize: {
      type: Number,
      required: true
    },
  },
  emits: ['change'],
  setup(props, { emit }) {
    const pages = computed(() => Math.ceil(Number((props.total / props.pageSize))));
    const pageSizeOptions = [10, 20, 30, 40]
    const handleSizeChange = (size: number) => {
      emit('change', {
        page: 1,
        pageSize: size,
        total: props.total
      })
    }
    const handlePageChange = (page: number, count: number = 0) => {
      if (page + count > 0 && page + count <= pages.value) {
        emit('change', {
          page: page + count,
          pageSize: props.pageSize,
          total: props.total
        })
      }
    }
    const generateArray = (count: number, current: number) => {
      const result = [];

      if (count <= 7) {
        for (let i = 1; i <= count; i++) {
          result.push(i);
        }
      } else {
        result.push(1);
        if (current > 3) {
          result.push('...');
        }

        if (current <= 3) {
          result.push(...[2, 3, 4, 5]);
        } else if (current >= count - 3) {
          result.push(...[count - 4, count - 3, count - 2, count - 1]);
        } else {
          result.push(current - 1);
          result.push(current);
          result.push(current + 1);
        }

        if (current < count - 3) {
          result.push('...');
        }
        result.push(count);
      }

      return result;
    }
    return {
      pages,
      pageSizeOptions,
      generateArray,
      handleSizeChange,
      handlePageChange
    }
  }
})
</script>
<template>
  <div class="flex items-center justify-between px-1 sm:bg-white dark:border-strokedark dark:bg-boxdark py-3">
    <div class="hidden sm:flex sm:flex-1 sm:items-center sm:justify-between">
      <div>
        <p class="text-sm flex items-center">
          <span class="hidden md:block">
            Showing
            <span class="font-medium px-2">{{ page }}</span>
            to
          </span>
          <span class="font-medium px-0 md:px-2">
            <select id="countries" :value="pageSize"
              @change="(event) => { handleSizeChange(Number((event.target as any).value)) }"
              class="bg-white dark:border-strokedark dark:bg-boxdark text-sm rounded-lg border px-1 py-1">
              <template v-for="item of pageSizeOptions" :key="item">
                <option :value="item">{{ item }}</option>
              </template>
            </select>
          </span>
          <span class="hidden md:block">
            of
            <span class="font-medium px-2">{{ total }}</span>
            results
          </span>
        </p>
      </div>
      <div>
        <nav class="isolate inline-flex -space-x-px rounded-md shadow-sm " aria-label="Pagination">
          <a href="#"
            class="inline-flex items-center rounded-l-md px-2 py-2 ring-1 ring-inset ring-stroke hover:bg-stroke hover:text-strokedark">
            <span class=" i-lucide-chevron-left" @click="() => handlePageChange(page, -1)"></span>
          </a>
          <template v-for="(item, index) of generateArray(pages, page)" :key="index">
            <a href="#" v-if="typeof item === 'number'" @click="() => handlePageChange(item)"
              :class="`${page === item && 'bg-stroke text-strokedark'} inline-flex items-center px-4 py-2 ring-1 ring-inset ring-stroke hover:bg-stroke hover:text-strokedark`">
              {{ item }}
            </a>
            <span v-else
              class='inline-flex items-center px-4 py-2 ring-1 ring-inset ring-stroke hover:bg-stroke hover:text-strokedark'>
              {{ item }}
            </span>
          </template>
          <a href="#"
            class="inline-flex items-center rounded-r-md px-2 ring-1 ring-inset ring-stroke py-2 hover:bg-stroke hover:text-strokedark">
            <span class=" i-lucide-chevron-right" @click="() => handlePageChange(page, 1)"></span>
          </a>
        </nav>
      </div>
    </div>
  </div>
</template>