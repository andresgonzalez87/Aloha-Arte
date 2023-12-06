<template>
  <br>
    <div class="form-register">
      <form @submit.prevent="submitForm">
        <h4>Formulario de registro</h4>
        <div>
          <input v-model="firstName" class="form-input" type="text" placeholder="Ingrese su nombre" />
          <span v-if="errors.firstName" class="error">{{ errors.firstName }}</span>
        </div>
        <div>
          <input v-model="lastName" class="form-input" type="text" placeholder="Ingrese su apellido" />
          <span v-if="errors.lastName" class="error">{{ errors.lastName }}</span>
        </div>
        <div>
          <input v-model="email" class="form-input" type="email" placeholder="Ingrese su email" />
          <span v-if="errors.email" class="error">{{ errors.email }}</span>
        </div>
        <div>
          <input v-model="password" class="form-input" type="password" placeholder="Ingrese su contraseña" />
          <span v-if="errors.password" class="error">{{ errors.password }}</span>
        </div>
        <div>
          <p>Estoy de acuerdo con Términos y Condiciones</p>
          <input v-model="agree" type="checkbox" class="checkbox" />
        </div>
        <input type="submit" class="form-button" value="Crear cuenta" />
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        agree: false,
        errors: {},
      };
    },
    methods: {
      submitForm() {
        this.errors = {}; // Limpiar errores al enviar el formulario
  
        if (!this.firstName.trim()) {
            this.errors.firstName = "Debe completar el nombre.";
        }
  
        if (!this.lastName.trim()) {
          this.errors.lastName = "Debe completar el apellido.";
        }
  
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        if (!emailPattern.test(this.email)) {
          this.errors.email = "Debe ingresar un email válido.";
        }
  
        if (this.password.length < 6) {
          this.errors.password = "La contraseña debe tener al menos 6 caracteres.";
        }
  
        if (!this.agree) {
          this.errors.agree = "Debe aceptar los Términos y Condiciones.";
        }
  
        if (Object.keys(this.errors).length === 0) {
          // aca podemos realizar el envío del formulario si no hay errores
          console.log("Formulario válido. Enviar datos.");
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .form-register {
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
  
  .form-register h4 {
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
  
  .form-register p {
    height: 40px;
    text-align: center;
    font-size: 18px;
    line-height: 40px;
  }
  
  .form-button {
    width: 100%;
    background: #1f53c5;
    border: none;
    padding: 12px;
    color: white;
    margin: 16px 0;
    font-size: 16px;
    cursor: hand;
  }
  
  span {
    color: red;
    font-weight: bold;
  }
  </style>
  