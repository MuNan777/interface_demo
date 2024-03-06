import { Ref, UnwrapRef, onMounted, ref } from 'vue';

const useLocalStorage = <T extends any>(
  key: string,
  initialValue: T
) => {
  const storedValue = ref<T>(initialValue) as Ref<T>;
  const setValue = (value: T) => {
    storedValue.value = value;
    window.localStorage.setItem(key, JSON.stringify(storedValue.value));
  }

  onMounted(() => {
    setValue(JSON.parse(window.localStorage.getItem(key) || 'null') || initialValue);
  })

  return {
    storedValue,
    setValue
  }
}

export default useLocalStorage;
