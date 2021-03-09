<template>
  <div class="home">
    <NlDeFlow msg="Please select date range"/>
  </div>
</template>

<script>
// @ is an alias to /src
import NlDeFlow from '@/components/NlDeFlow.vue'

export default {
  name: 'Home',
  components: {
    NlDeFlow,
  }
}
</script>
