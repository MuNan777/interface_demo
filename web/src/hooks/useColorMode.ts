import { onMounted } from "vue";
import useLocalStorage from "./useLocalStorage";


const useColorMode = () => {
  const { storedValue, setValue } = useLocalStorage<"dark" | "light">("color-theme", "light");

  const setColorMode = (mode: "dark" | "light") => {
    const className = "dark";
    const bodyClass = window.document.body.classList;

    storedValue.value === "dark"
      ? bodyClass.add(className)
      : bodyClass.remove(className);
    setValue(mode);
  }

  onMounted(() => {
    setColorMode(storedValue.value);
  })

  return {
    colorMode: storedValue, setColorMode
  };
};

export default useColorMode;