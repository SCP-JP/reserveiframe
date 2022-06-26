module.exports = {
  head: [["link", { rel: "icon", href: "/favicon.ico" }]],
  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  title: "翻訳予約index",
  dest: 'dist/',
  base: '/reserveiframe/',
  themeConfig: {
    repo: '',
    editLinks: false,
    docsDir: '',
    editLinkText: '',
    lastUpdated: false,
    navbar: false,
  },
  plugins: {
    'clean-urls': {
      normalSuffix: '/',
    },
  }
}
