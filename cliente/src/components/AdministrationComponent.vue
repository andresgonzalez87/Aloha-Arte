<template>
    <div>
      <div class="form-properties">
        <form @submit.prevent="submitForm">
          <h4>Agregar propiedad</h4>
          <div class="form-row">
            <div>
              <input v-model="title" class="form-input" type="text" placeholder="Categoría" />
              <span v-if="errors.title" class="error">{{ errors.title }}</span>
            </div>
            <div>
              <input v-model="description" class="form-input" type="text" placeholder="Descripción" />
              <span v-if="errors.description" class="error">{{ errors.description }}</span>
            </div>
            <input type="hidden" class="" name="id" id="id_property" v-model="id_property">
            <input type="submit" class="form-button" value="Agregar" />
          </div>
        </form>
      </div>
  
      <br />
  
      <div class="table-container">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Categoría</th>
              <th scope="col">Descripción</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="propertie in properties" :key="propertie.id">
              <td>{{ propertie.title }}</td>
              <td>{{ propertie.description }}</td>
              <td><button><i class="fas fa-trash-alt" @click="deletePropertie(propertie.id)"></i></button></td>
            </tr>
          </tbody>
        </table>
        <br>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        id_property:'',
        properties: [],
        api_server: "http://127.0.0.1:8000",
        title: "",
        description: "",
        errors: {},
      };
    },
    methods: {

      submitForm() {
        this.errors = {};
        if (!this.title.trim()) {
          this.errors.title = "Debe ingresar un nombre de usuario.";
        }
        if (!this.description.trim()) {
          this.errors.description = "Debe ingresar una contraseña.";
        }
        if (Object.keys(this.errors).length === 0) {
          console.log("Formulario válido, enviar datos.");
          const formData = new FormData();
          formData.append('title', this.title);
          formData.append('description', this.description);
          this.sendFormData(`${this.api_server}/api/createpropertie/`, formData, 'POST');
        }
      },

      sendFormData(url,formData,method){
        fetch(url, {
          method:method,
          body:formData,
        })
        .then((response)=>response.json())
        .then(()=>{
          alert('Registro creado:')
          this.getProperties();
        })
        .catch((error)=>{
          console.log('Error al enviar el formulario', error)
        })
      },

      getProperties(){
        fetch(`${this.api_server}/api/getproperties/`)
        .then((response)=> response.json())
        .then((data)=>{
            this.properties=data;
            console.log(data)  
        })
        .catch((err)=>{
            console.error(err);
        });
      },
      deletePropertie(id_property){
        fetch(`${this.api_server}/api/deletepropertie/${id_property}/`, {
          method: 'DELETE',
        })
        .then((response)=>response.json())
        .then(()=>{
          alert('Registro eliminado')
          this.getProperties(`${this.api_server}/api/getproperties`);
        })
        .catch((error)=>{
          console.error('Error al eliminar', error)
        })
      }

    },
    created() {
        this.getProperties()
     
    },
  };
  </script>
  
  <style scoped>
  .form-properties {
    width: 700px;
    background: #191c1f;
    padding: 20px;
    margin: auto;
    margin-top: 100px;
    margin-bottom: 40px;
    border-radius: 4px;
    font-family: 'calibri';
    color: white;
    box-shadow: 7px 13px 37px #000;
  }
  
  .form-properties h4 {
    font-size: 22px;
    margin-bottom: 20px;
    text-align: center;
  }
  
  .form-row {
    display: flex;
    justify-content: space-between;
  }
  
  .form-row div {
    width: 48%;
  }
  
  .form-input {
    width: 100%;
    background: #24303c;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 16px;
    border: 1px solid #1f53c5;
    font-family: 'calibri';
    font-size: 18px;
    color: white;
  }
  
  .form-button {
    width: 30%;
    background: #1f53c5;
    border: none;
    padding: 12px;
    color: white;
    margin-bottom: 16px ;
    font-size: 16px;
    cursor: pointer;
  }
  
  .table {
    width: 100%;
    border-collapse: collapse;
   
  }
  
  .table th, .table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  .table th {
    background-color: #1f53c5;
    color: white;
  }
  </style>
  