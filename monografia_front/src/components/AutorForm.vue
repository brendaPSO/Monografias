<template>
  <div>
    <Message :msg="msg" v-show="msg" />
    <div>
      <form id="autor-form" @submit="createAutor">
        <div class="input-container">
          <label for="nome">Nome:</label>
          <input type="text" id="nome" name="nome" v-model="nome" placeholder="Digite o nome">
        </div>

        <div class="input-container">
          <label for="tipo">Tipo de autor:</label>
          <select name="tipo" id="tipo" v-model="tipo">
            <option v-for="tipo in tipo_pessoa" :key="tipo.id" :value="tipo.id">{{tipo.tipo}}</option>
          </select>
        </div>

        <div class="input-container">
          <label for="curso">Curso:</label>
          <input type="text" id="curso" name="curso" v-model="curso" placeholder="Digite o curso">
        </div>

        <div class="input-container">
          <label for="universidade">Universidade:</label>
          <input type="text" id="universidade" name="universidade" v-model="universidade" placeholder="Digite a universidade">
        </div>

        <div class="input-container">
          <label for="email">E-mail:</label>
          <input type="email" id="email" name="email" v-model="email" placeholder="Digite o e-mail">
        </div>

        <div class="input-container">
          <label for="curriculo">Currículo:</label>
          <input type="text" id="curriculo" name="curriculo" v-model="curriculo" placeholder="Digite o link do curriculo">
        </div>

        <div class="input-container">
          <label for="google_scholar">Google Scholar:</label>
          <input type="text" id="google_scholar" name="google_scholar" v-model="google_scholar" placeholder="Digite o link do Google Scholar">
        </div>

        <div class="input-container">
          <label for="research_gate">Research Gate:</label>
          <input type="text" id="research_gate" name="research_gate" v-model="research_gate" placeholder="Digite o link do Research Gate">
        </div>

        <div class="input-container">
          <label for="linkedin">Linkedin:</label>
          <input type="text" id="linkedin" name="linkedin" v-model="linkedin" placeholder="Digite o link do Linkedin">
        </div>

        <div class="input-container">
          <label for="orcid">Orcid:</label>
          <input type="text" id="orcid" name="orcid" v-model="orcid" placeholder="Digite o link do Orcid">
        </div>

        <div class="input-container">
          <label for="github">Github:</label>
          <input type="text" id="github" name="github" v-model="github" placeholder="Digite o link do Github">
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
  </div>

</template>

<script>
  import Message from '../components/Message.vue'
  import axios from "axios";

  export default {
    name: "AutorForm",
    data() {
      return {
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
        msg: null
      }
    },
    methods: {
      async getTipo(){
        this.tipo_pessoa = [
          {"id": 1, "tipo": "autor"},
          {"id": 2, "tipo": "orientador"},
          {"id": 3, "tipo": "coorientador"}
        ]
      },
      async createAutor(e){
        e.preventDefault();
        
        const data = 
        {
          "nome": this.nome,
          "tipo": this.tipo,
          "curso": this.curso,
          "universidade": this.universidade,
          "email": this.email,
          "curriculo": this.curriculo,
          "google_scholar": this.google_scholar,
          "research_gate": this.research_gate,
          "linkedin": this.linkedin,
          "orcid": this.orcid,
          "github": this.github
        }

        const dataJson = JSON.stringify(data);

        const req = await axios({
          method: 'POST',
          url: 'http://localhost:8000/api/pessoa/',
          headers: { "Content-Type": "application/json" },
          data: dataJson
        }).then(function(response){
          location.reload();
        });
        
        const res = await req.json();
        this.msg = `Cadastro do(a) ${res.nome} realizado com sucesso`;

        setTimeout(() => this.msg = "", 10000);
        
        this.nome = "";
        this.tipo = "";
        this.curso = "";
        this.universidade = "";
        this.email = "";
        this.curriculo = "";
        this.google_scholar = "";
        this.research_gate = "";
        this.linkedin = "";
        this.orcid = "";
        this.github = "";
        
      }
    },
    mounted(){
      this.getTipo();
    },
    components: {
      Message
    }
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