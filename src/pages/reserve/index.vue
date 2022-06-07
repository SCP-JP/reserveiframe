<template>
  <p>
    <span class="printuser"><a v-bind:href="'http://www.wikidot.com/user:info/'+attributes.user">{{attributes.user}}</a></span>
    <span>{{attributes.starttime}}</span>
    -
    <span>{{attributes.endtime}}</span>
  </p>
</template>

<script>
import { attributes } from "/contents/content.md";
export default {
  data() {
    return {
      attributes,
    };
  },
};
</script>