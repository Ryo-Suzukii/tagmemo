import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from "vite-plugin-vuetify";

import Icons from 'vite-plugin-icons'
import { FileSystemIconLoader } from 'unplugin-icons/dist/loaders.cjs';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vuetify(),
    Icons({
      customCollections: {
        svg: FileSystemIconLoader('src/assets/icons'),
      }
    })
  ],
  server: {
    proxy: {
      '/api': {
        target: 'https://6f5dgikzng.execute-api.ap-northeast-1.amazonaws.com',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''), 
      },
    },
  },
})
