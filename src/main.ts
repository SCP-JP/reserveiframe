import { ViteSSG } from 'vite-ssg'
import { setupLayouts } from 'layouts-generated'
import generatedRoutes from 'virtual:generated-pages'
import './assets/style.css'
import App from './App.vue'

const routes = setupLayouts(generatedRoutes)

export const createApp = ViteSSG(
  App,
  { routes }
)
