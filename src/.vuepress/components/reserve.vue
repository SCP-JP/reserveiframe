<template>
  <p>
    <span class="printuser"><a v-bind:href="'http://www.wikidot.com/user:info/'+data.user" target="_blank">{{data.user}}</a></span>
    <span>{{data.starttime}}</span>
    -
    <span>{{data.endtime}}</span>
  </p>
</template>

<script>
export default {
  computed: {
  data() {
    return this.$page.frontmatter
  },
}}
</script>