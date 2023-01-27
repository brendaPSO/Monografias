<template>
  <div id="monografia-table" v-if="pessoas">
    <div>
      <div id="monografia-table-heading">
        <div class="order-id">#:</div>
        <div>Nome:</div>
        <div>Tipo:</div>
        <div>Curso:</div>
        <div>Universidade:</div>
        <div>E-mail:</div>
        <div>Ações:</div>
        <div></div>
      </div>
    </div>
      <div id="monografia-table-rows">
        <div
          class="monografia-table-row"
          v-for="pessoa in pessoas"
          :key="pessoa.id"
        >
          <div class="order-number">{{ pessoa.id }}</div>
          <div>{{ pessoa.nome }}</div>
          <div>{{ pessoa.tipo == 1 ? 'autor' : pessoa.tipo == 2 ? 'orientador' : 'coorientador'}}</div>
          <div>{{ pessoa.curso }}</div>
          <div>{{ pessoa.universidade }}</div>
          <div class="email-div">{{ pessoa.email }}</div>
          <div class="acao">
            <button class="delete-btn" @click="deletePessoa(pessoa.id)">
              Excluir
            </button>
          </div>
          <div class="acao">
              <router-link v-bind:to="'/editarcadastro/' + pessoa.id">Editar</router-link>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <h2>Não há pessoas cadastradas!</h2>
    </div>
</template>
  
<script>
  import axios from "axios";
  
  export default {
    name: "Cadastro",
    data() {
      return {
        pessoas: null,
        nome: null,
        tipo: null,
        curso: null,
        Universidade: null,
        email: null,
      };
    },
    methods: {
      async getPessoas() {
        const req_pessoas = await axios.get(
          "http://127.0.0.1:8000/api/pessoa/"
        );
        const data_pessoas = await req_pessoas.data;
        this.pessoas = data_pessoas;
      },

      async deletePessoa(id) {
      const req = await axios.delete(
        `http://127.0.0.1:8000/api/pessoa/${id}/`
      ).then(function(response){
          location.reload();
      });

      const res = await req.json();

      this.msg = `Pessoa removido com sucesso!`;
      setTimeout(() => (this.msg = ""), 3000);

      this.getMonografiasAutores();
    }

    },
    mounted() {
      this.getPessoas();
    },
  };
</script>
  
<style scoped>
  #monografia-table {
    max-width: 1200px;
    margin: 0 auto;
  }
  #monografia-table-heading,
  #monografia-table-rows,
  .monografia-table-row {
    display: flex;
    flex-wrap: wrap;
  }
  #monografia-table-heading {
    font-weight: bold;
    padding: 12px;
    border-bottom: 3px solid #333;
  }
  .monografia-table-row {
    width: 100%;
    padding: 12px;
    border-bottom: 1px solid #ccc;
  }
  #monografia-table-heading div,
  .monografia-table-row div {
    width: 11%;
  }
  #monografia-table-heading .order-id,
  .monografia-table-row .order-number {
    width: 5%;
  }
  
  .monografia-table-row .acao {
    width: 8%;
  }
  
  button {
    background-color: #00719e;
    color: #fff;
    font-weight: bold;
    border: 2px solid #00587a;
    padding: 10px;
    font-size: 14px;
    margin: 0 auto;
    cursor: pointer;
    transition: 0.5s;
  }
  
  .delete-btn {
    background-color: #222;
    border: 2px solid #222;
    color: #fff;
  }
  
  button:hover {
    background-color: transparent;
    color: #222;
  }

  .email-div {
    margin-right: 7%;
  }
</style>