<template>
   <div class="main-container">
    <h1>Cadastre Autor:</h1>
    <AutorForm />
  </div>
</template>

<script>
  import AutorForm from '../components/AutorForm.vue'

  export default {
    name: 'Autores',
    components: {
      AutorForm
    }
  }
</script>