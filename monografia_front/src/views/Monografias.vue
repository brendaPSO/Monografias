<template>
   <div class="main-container">
    <h1>Cadastre Monografia:</h1>
    <MonografiaForm />
  </div>
</template>

<script>
  import MonografiaForm from '../components/MonografiaForm.vue'

  export default {
    name: 'Monografias',
    components: {
      MonografiaForm
    }
  }
</script>