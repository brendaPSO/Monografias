<template>
    <div class="main-container">
      <h1>Editar Cadastro:</h1>
      <form id="autor-form" @submit="editData">
        <div class="input-container">
          <label for="nome">Nome:</label>
          <input type="text" id="nome" name="nome" v-model="this.nome" placeholder="Digite o nome">
        </div>

        <div class="input-container">
          <label for="tipo">Tipo de autor:</label>
          <select name="tipo" id="tipo" v-model="tipo">
            <option v-for="tipo in tipo_pessoa" :key="tipo.id" :value="tipo.id">{{tipo.tipo}}</option>
          </select>
        </div>

        <div class="input-container">
          <label for="curso">Curso:</label>
          <input type="text" id="curso" name="curso" v-model="this.curso" placeholder="Digite o curso">
        </div>

        <div class="input-container">
          <label for="universidade">Universidade:</label>
          <input type="text" id="universidade" name="universidade" v-model="this.universidade" placeholder="Digite a universidade">
        </div>

        <div class="input-container">
          <label for="email">E-mail:</label>
          <input type="email" id="email" name="email" v-model="this.email" placeholder="Digite o e-mail">
        </div>

        <div class="input-container">
          <label for="curriculo">Currículo:</label>
          <input type="text" id="curriculo" name="curriculo" v-model="this.curriculo" placeholder="Digite o link do curriculo">
        </div>

        <div class="input-container">
          <label for="google_scholar">Google Scholar:</label>
          <input type="text" id="google_scholar" name="google_scholar" v-model="this.google_scholar" placeholder="Digite o link do Google Scholar">
        </div>

        <div class="input-container">
          <label for="research_gate">Research Gate:</label>
          <input type="text" id="research_gate" name="research_gate" v-model="this.research_gate" placeholder="Digite o link do Research Gate">
        </div>

        <div class="input-container">
          <label for="linkedin">Linkedin:</label>
          <input type="text" id="linkedin" name="linkedin" v-model="this.linkedin" placeholder="Digite o link do Linkedin">
        </div>

        <div class="input-container">
          <label for="orcid">Orcid:</label>
          <input type="text" id="orcid" name="orcid" v-model="this.orcid" placeholder="Digite o link do Orcid">
        </div>

        <div class="input-container">
          <label for="github">Github:</label>
          <input type="text" id="github" name="github" v-model="this.github" placeholder="Digite o link do Github">
        </div>

        <!-- <div id="opcionais-container" class="input-container">
          <label class="opcionais-title" for="opcionais"> Selecione os opcionais </label>
          <div class="checkbox-container" v-for="opcional in opcionaisdata" :key="opcional.id">
            <input type="checkbox" name="opcionais" v-model="opcionais" :value="opcional.tipo">
            <span>{{opcional.tipo}}</span>
          </div>
        </div> -->

        <div class="input-container">
          <input type="submit" class="submit-btn" value="Cadastrar">
        </div>
      </form>
    </div>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        pessoa: null,
        id: this.$route.params.id,
        tipo_pessoa: null,
        nome: null,
        tipo: null,
        curso: null,
        universidade: null,
        email: null,
        curriculo: null,
        google_scholar: null,
        research_gate: null,
        linkedin: null,
        orcid: null,
        github: null,
      }
    },
    
    methods: {    

      //-------------------------------------
      // Metodo para pegar os tipo de pessoa
      //-------------------------------------

      async getTipo(){
        this.tipo_pessoa = [
          {"id": 1, "tipo": "autor"},
          {"id": 2, "tipo": "orientador"},
          {"id": 3, "tipo": "coorientador"}
        ]
      },

      //------------------------------------
      //Metodo para trazer os valores atuais
      //------------------------------------ 
  
      async getPessoa() {
        const req_pessoa = await axios.get(
          `http://localhost:8000/api/pessoa/${this.id}/`
        );
        const data_pessoa = await req_pessoa.data;
        this.pessoa = data_pessoa;
        this.nome = data_pessoa.nome;
        this.tipo = data_pessoa.tipo;
        this.curso = data_pessoa.curso;
        this.universidade = data_pessoa.universidade;
        this.email = data_pessoa.email;
        this.curriculo = data_pessoa.curriculo;
        this.google_scholar = data_pessoa.google_scholar;
        this.research_gate = data_pessoa.research_gate;
        this.linkedin = data_pessoa.linkedin;
        this.orcid = data_pessoa.orcid;
        this.github = data_pessoa.github;
      },
  
      //------------------------------------
      //Metodo para enviar as mudanças
      //------------------------------------ 
  
      async editData(e) {
        e.preventDefault();
  
        const data = {
          id: this.id,
          nome: this.nome,
          tipo: this.tipo,
          curso: this.curso,
          universidade: this.universidade,
          email: this.email,
          curriculo: this.curriculo,
          google_scholar: this.google_scholar,
          research_gate: this.research_gate,
          linkedin: this.linkedin,
          orcid: this.orcid,
          github: this.github,
        };
        const dataJson = JSON.stringify(data)
        await axios({
          method: "PATCH",
          url: `http://127.0.0.1:8000/api/pessoa/${this.id}/`,
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
      this.getPessoa();
      this.getTipo();
    },
  }
</script>
  
<style scoped>
  #autor-form {
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

  input, select {
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
    transition: .5s;
  }

  .submit-btn:hover {
    background-color: transparent;
    color: #222;
    border: 2px solid #222;
  }
</style>
  
  