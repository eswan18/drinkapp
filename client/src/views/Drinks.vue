<template>
  <div class="drinks">
    <img alt="Vue logo" src="../assets/logo.png">
    <Drinks/>
  </div>
</template>

<script>
// @ is an alias to /src
import Drinks from '@/components/Drinks.vue';

export default {
  name: 'DrinksView',
  components: {
    Drinks,
  },
};
</script>
