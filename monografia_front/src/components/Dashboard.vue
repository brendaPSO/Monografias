<template>
  <div id="monografia-table" v-if="monografias">
    <Message :msg="msg" v-show="msg" />
    <div>
      <div id="monografia-table-heading">
        <div class="order-id">#:</div>
        <div>Título:</div>
        <div>Autor:</div>
        <div>Orientador:</div>
        <div>Coorientador:</div>
        <div>Data:</div>
        <div>Palavra-chave:</div>
        <div>Ações:</div>
        <div></div>
      </div>
    </div>
    <div id="monografia-table-rows">
      <div
        class="monografia-table-row"
        v-for="monografia in monografias"
        :key="monografia.id"
      >
        <div class="order-number">{{ monografia.id }}</div>
        <div>{{ monografia.titulo }}</div>
        <div>{{ monografia.autor }}</div>
        <div>{{ monografia.orientador }}</div>
        <div>{{ monografia.coorientador }}</div>
        <div>{{ monografia.data }}</div>
        <div>{{ monografia.palavrachave }}</div>
        <div class="acao">
          <button class="view-btn" @click="viewMonografia(monografia.id)">
            Visualizar
          </button>
        </div>
        <div class="acao">
          <button class="delete-btn" @click="deleteMonografia(monografia.id)">
            Excluir
          </button>
        </div>
        <div class="acao">
            <router-link v-bind:to="'/editar/' + monografia.id">Editar</router-link>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <h2>Não há monografias cadastradas!</h2>
  </div>
</template>

<script>
import Message from "./Message.vue";
import axios from "axios";

export default {
  name: "Dashboard",
  data() {
    return {
      monografias: null,
      autores: null,
      titulo: null,
      autor: null,
      orientador: null,
      coorientador: null,
      data: null,
      palavrachave: null,
      msg: null,
    };
  },
  components: {
    Message,
  },
  methods: {
    async getMonografiasAutores() {
      const req_monografias = await axios.get(
        "http://127.0.0.1:8000/api/monografia/"
      );
      const data_monografias = await req_monografias.data;

      for (var i = 0; i < data_monografias.length; i++) {
        data_monografias[i].autor = (
          await (
            await axios.get(data_monografias[i].autor)
          ).data
        ).nome;
        data_monografias[i].orientador = (
          await (
            await axios.get(data_monografias[i].orientador)
          ).data
        ).nome;
        data_monografias[i].coorientador = (
          await (
            await axios.get(data_monografias[i].coorientador)
          ).data
        ).nome;
      }

      this.monografias = data_monografias;
    },

    async deleteMonografia(id) {
      const req = await axios.delete(
        `http://127.0.0.1:8000/api/monografia/${id}/`
      ).then(function(response){
          location.reload();
      });

      const res = await req.json();

      this.msg = `Pedido removido com sucesso!`;
      setTimeout(() => (this.msg = ""), 3000);

      this.getMonografiasAutores();
    }
  },
  mounted() {
    this.getMonografiasAutores();
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
</style>