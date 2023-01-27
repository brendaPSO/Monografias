<template>
  <div class="main-container">
    <h1>Editar Monografia: {{ this.id }}</h1>
    <form id="monografia-form" @submit="editData">
      <div class="input-container"><label for="titulo">Título:</label><input v-model="this.titulo" type="text" placeholder="Titulo"></div>
      
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

      <div class="input-container"><label for="data">Data:</label><input type="date" v-model="this.data" placeholder="Data"></div>
      <div class="input-container"><label for="resumo">Resumo:</label><input v-model="this.resumo" type="text" placeholder="Resumo"></div>
      <div class="input-container"><label for="palavrachave">Palavra-chave:</label><input v-model="this.palavrachave" type="text" placeholder="Palavrachave"></div>
      <div class="input-container"><label for="universidade">Universidade:</label><input v-model="this.universidade" type="text" placeholder="Universidade"></div>
      <div class="input-container"><label for="curso">Curso:</label><input v-model="this.curso" type="text" placeholder="Curso"></div>
      <div class="input-container"><label for="link">Link da monografia:</label><input v-model="this.link" type="text" placeholder="Link"></div>
      <div class="input-container">
          <input type="submit" class="submit-btn" value="Editar" />
        </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      monografia: null,
      id: this.$route.params.id,
      autores: [],
      orientadores: [],
      coorientadores: [],
      titulo: "",
      autor: "",
      orientador: "",
      coorientador: "",
      data: "",
      resumo: "",
      palavrachave: "",
      universidade: "",
      curso: "",
      link: ""
    }
  },
  
  methods: {

    //-----------------------------------------
    //Metodo para trazer os autores disponiveis
    //-----------------------------------------

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

    //------------------------------------
    //Metodo para trazer os valores atuais
    //------------------------------------ 

    async getMonografia() {
      const req_monografias = await axios.get(
        `http://localhost:8000/api/monografia/${this.id}/`
      );
      const data_monografias = await req_monografias.data;
      this.monografias = data_monografias;
      this.titulo = data_monografias.titulo;
      this.autor = (await (await axios.get(data_monografias.autor)).data).id;
      this.orientador = (await (await axios.get(data_monografias.orientador)).data).id;
      this.coorientador = (await (await axios.get(data_monografias.coorientador)).data).id;
      this.data = data_monografias.data;
      this.resumo = data_monografias.resumo;
      this.palavrachave = data_monografias.palavrachave;
      this.universidade = data_monografias.universidade;
      this.curso = data_monografias.curso;
      this.link = data_monografias.link;

    },

    //------------------------------------
    //Metodo para enviar as mudanças
    //------------------------------------ 

    async editData(e) {
      e.preventDefault();

      const data = {
        id: this.id,
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
      const dataJson = JSON.stringify(data)
      await axios({
        method: "PATCH",
        url: `http://127.0.0.1:8000/api/monografia/${this.id}/`,
        headers: { "Content-Type": "application/json" },
        data: dataJson,
      }).then(function(response){
        location.reload();
      });
      //const res = await req.json();
      console.log(dataJson)
    }
  },
  mounted() {
    this.getMonografia();
    this.getAutores();
  },
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

