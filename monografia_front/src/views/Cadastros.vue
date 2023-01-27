<template>
  <div class="main-container">
    <h1>Listar Cadastros:</h1>
    <ListaCadastros />
  </div>
</template>
  
<script>
  import ListaCadastros from '../components/ListaCadastros.vue'
  
  export default {
    name: 'Cadastros',
    components: {
      ListaCadastros
    }
  }
</script>