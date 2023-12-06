<template>
  <br><br>
    <div class="form-login">
      <form @submit.prevent="submitForm">
        <h4>Inicio de Sesión</h4>
        <div>
          <input v-model="username" class="form-input" type="text" placeholder="Nombre de usuario" />
          <span v-if="errors.username" class="error">{{ errors.username }}</span>
        </div>
        <div>
          <input v-model="password" class="form-input" type="password" placeholder="Contraseña" />
          <span v-if="errors.password" class="error">{{ errors.password }}</span>
        </div>
        <input type="submit" class="form-button" value="Iniciar Sesión" />
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: "",
        password: "",
        errors: {},
      };
    },
    methods: {
      submitForm() {
        this.errors = {}; // Limpiar errores al enviar el formulario
  
        if (!this.username.trim()) {
          this.errors.username = "Debe ingresar un nombre de usuario.";
        }
  
        if (!this.password.trim()) {
          this.errors.password = "Debe ingresar una contraseña.";
        }
  
        if (Object.keys(this.errors).length === 0) {
          // aca podemos realizar la lógica de inicio de sesión si no hay errores
          console.log("Inicio de sesión válido. Procesar autenticación.");
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .form-login {
    width: 400px;
    background: #24303c;
    padding: 30px;
    margin: auto;
    margin-top: 100px;
    margin-bottom: 100px;
    border-radius: 4px;
    font-family: 'calibri';
    color: white;
    box-shadow: 7px 13px 37px #000;
  }
  
  .form-login h4 {
    font-size: 22px;
    margin-bottom: 20px;
    text-align: center;
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
    width: 100%;
    background: #1f53c5;
    border: none;
    padding: 12px;
    color: white;
    margin: 16px 0;
    font-size: 16px;
    cursor: pointer;
  }
  
  span {
    color: red;
    font-weight: bold;
  }
  </style>
  