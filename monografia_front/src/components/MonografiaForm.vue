<template>
  <div>
    <Message :msg="msg" v-show="msg" />
    <div>
      <form id="monografia-form" @submit="createMonografia">
        <div class="input-container">
          <label for="titulo">Título:</label>
          <input
            type="text"
            id="titulo"
            name="titulo"
            v-model="titulo"
            placeholder="Digite o título"
          />
        </div>

        <div class="input-container">
          <label for="autor">Autor:</label>
          <select name="autor" id="autor" v-model="autor">
            <option v-for="autor in autores" :key="autor.id" :value="autor.id">
              {{ autor.tipo }}
            </option>
          </select>
        </div>

        <div class="input-container">
          <label for="orientador">Orientador:</label>
          <select name="orientador" id="orientador" v-model="orientador">
            <option
              v-for="orientador in orientadores"
              :key="orientador.id"
              :value="orientador.id"
            >
              {{ orientador.tipo }}
            </option>
          </select>
        </div>

        <div class="input-container">
          <label for="coorientador">Coorientador:</label>
          <select name="coorientador" id="coorientador" v-model="coorientador">
            <option
              v-for="coorientador in coorientadores"
              :key="coorientador.id"
              :value="coorientador.id"
            >
              {{ coorientador.tipo }}
            </option>
          </select>
        </div>

        <div class="input-container">
          <label for="data">Data:</label>
          <input
            type="date"
            id="data"
            name="data"
            v-model="data"
            placeholder="Digite o data de publicação"
          />
        </div>

        <div class="input-container">
          <label for="resumo">Resumo:</label>
          <input
            type="text"
            id="resumo"
            name="resumo"
            v-model="resumo"
            placeholder="Digite o resumo"
          />
        </div>

        <div class="input-container">
          <label for="palavrachave">Palavra-chave:</label>
          <input
            type="text"
            id="palavrachave"
            name="palavrachave"
            v-model="palavrachave"
            placeholder="Digite a palavra-chave"
          />
        </div>

        <div class="input-container">
          <label for="universidade">Universidade:</label>
          <input
            type="text"
            id="universidade"
            name="universidade"
            v-model="universidade"
            placeholder="Digite a universidade"
          />
        </div>

        <div class="input-container">
          <label for="curso">Curso:</label>
          <input
            type="text"
            id="curso"
            name="curso"
            v-model="curso"
            placeholder="Digite o curso"
          />
        </div>

        <div class="input-container">
          <label for="link">Link da monografia:</label>
          <input
            type="text"
            id="link"
            name="link"
            v-model="link"
            placeholder="Digite o link da monografia"
          />
        </div>

        <!-- <div id="opcionais-container" class="input-container">
          <label class="opcionais-title" for="opcionais"> Selecione os opcionais </label>
          <div class="checkbox-container" v-for="opcional in opcionaisdata" :key="opcional.id">
            <input type="checkbox" name="opcionais" v-model="opcionais" :value="opcional.tipo">
            <span>{{opcional.tipo}}</span>
          </div>
        </div> -->

        <div class="input-container">
          <input type="submit" class="submit-btn" value="Cadastrar" />
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import Message from "../components/Message.vue";
import axios from "axios";

export default {
  name: "MonografiaForm",
  data() {
    return {
      autores: [],
      orientadores: [],
      coorientadores: [],
      tipo_pessoa: null,
      titulo: null,
      autor: null,
      orientador: null,
      coorientador: null,
      data: null,
      resumo: null,
      palavrachave: null,
      universidade: null,
      curso: null,
      link: null,
      msg: null,
    };
  },
  methods: {
    async getAutores() {
      const req = await axios.get("http://localhost:8000/api/pessoa/");
      const data = req.data;

      for (const idx in data) {
        if (data[idx].tipo == 1) {
          this.autores.push({ id: data[idx].id, tipo: data[idx].nome });
        } else if (data[idx].tipo == 2) {
          this.orientadores.push({ id: data[idx].id, tipo: data[idx].nome });
        } else {
          this.coorientadores.push({ id: data[idx].id, tipo: data[idx].nome });
        }
      }
    },
    async createMonografia(e) {
      e.preventDefault();

      const data = {
        titulo: this.titulo,
        autor: `http://localhost:8000/api/pessoa/${this.autor}/`,
        orientador: `http://localhost:8000/api/pessoa/${this.orientador}/`,
        coorientador: `http://localhost:8000/api/pessoa/${this.coorientador}/`,
        data: this.data,
        resumo: this.resumo,
        palavrachave: this.palavrachave,
        universidade: this.universidade,
        curso: this.curso,
        link: this.link,
      };

      const dataJson = JSON.stringify(data);
      const req = await axios({
        method: "POST",
        url: "http://localhost:8000/api/monografia/",
        headers: { "Content-Type": "application/json" },
        data: dataJson,
      }).then(function(response){
        location.reload();
      });

      const res = await req.json();
      this.msg = `Cadastro da monografia realizado com sucesso`;

      setTimeout(() => (this.msg = ""), 10000);

      this.titulo = "";
      this.autor = "";
      this.orientador = "";
      this.coorientador = "";
      this.data = "";
      this.resumo = "";
      this.palavrachave = "";
      this.universidade = "";
      this.curso = "";
      this.link = "";
    },
  },
  mounted() {
    this.getAutores();
  },
  components: {
    Message
  }
}
</script>

<style scoped>
#monografia-form {
  max-width: 300px;
  margin: 0 auto;
}
.input-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}
label {
  font-weight: bold;
  margin-bottom: 15px;
  color: #222;
  padding: 5px 10px;
  border-left: 4px solid #00719e;
}
input,
select {
  padding: 5px 10px;
  width: 300px;
}
#opcionais-container {
  flex-direction: row;
  flex-wrap: wrap;
}
#opcionais-title {
  width: 100%;
}
.checkbox-container {
  display: flex;
  align-items: flex-start;
  width: 50%;
  margin-bottom: 20px;
}
.checkbox-container span,
.checkbox-container input {
  width: auto;
}
.checkbox-container span {
  margin-left: 6px;
  font-weight: bold;
}
.submit-btn {
  background-color: #00719e;
  color: #fff;
  font-weight: bold;
  border: 2px solid #00587a;
  padding: 10px;
  font-size: 16px;
  margin: 0 auto;
  cursor: pointer;
  transition: 0.5s;
}
.submit-btn:hover {
  background-color: transparent;
  color: #222;
  border: 2px solid #222;
}
</style>