const { path } = require('@vuepress/utils')

const reserve = (options) => {
  return {
    name: 'vuepress-theme-reserve',
    layouts: {
      Layout: path.resolve(__dirname, 'layouts/Layout.vue'),
      404: path.resolve(__dirname, 'layouts/NotFound.vue'),
    },
    // ...
  }
}