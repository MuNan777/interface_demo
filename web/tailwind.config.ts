import type { Config } from 'tailwindcss'
import { iconsPlugin, getIconCollections, dynamicIconsPlugin } from "@egoist/tailwindcss-icons"
import MyTheme from './theme'

const config: Config = {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: MyTheme,
  plugins: [
    iconsPlugin({
      collections: getIconCollections(["lucide"]),
      scale: 1.3,
      extraProperties: {
        marginTop: '0.1rem'
      }
    }),
    dynamicIconsPlugin()
  ],
}
export default config
