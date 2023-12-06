<template>
    <br><br><br><br><br>
    <div>
      <div class="contact-info">
        <h2>Contacto</h2>
        <p>
          Estamos aquí para responder a cualquier pregunta.<br/>
          Ponte en contacto con nosotros.
        </p>
      </div>
      <br>
      <div class="contact-form">
        <form @submit.prevent="submitForm">
          <input v-model="name" type="text" id="name" required placeholder="Nombre" />
          <input v-model="email" type="email" id="email" required placeholder="Email" />
          <textarea v-model="message" id="message" required placeholder="Mensaje"></textarea>
          <div>
            <input type="submit" value="Enviar mensaje" />
          </div>
        </form>
      </div>
      <div class="gmap_canvas">
        <iframe
          src="https://maps.google.com/maps?q=university%20of%20san%20francisco&amp;t=&amp;z=13&amp;ie=UTF8&amp;iwloc=&amp;output=embed"
          frameborder="0"
          scrolling="no"
        ></iframe>
        <a href="https://www.eireportingonline.com"></a>
      </div>
    </div>
  </template>
  
  <style scoped>
  .contact-info,
  .contact-form,
  .gmap_canvas {
    background: #678aad;
    font-family: 'calibri', 'Montserrat', 'sans-serif';
    text-align: center;
    margin: auto;
    max-width: 600px;
  }
  
  .contact-info h2,
  .contact-form h2 {
    color: white;
    font-size: 26px;
    margin-bottom: 20px;
  }
  
  .contact-info p {
    color: white;
    font-size: 18px;
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  input,
  textarea {
    padding: 10px;
    margin-bottom: 16px;
    border: 1px solid #1f53c5;
    border-radius: 4px;
    font-size: 16px;
  }
  
  input[type="submit"] {
    background: #1f53c5;
    border: none;
    padding: 12px;
    color: white;
    font-size: 16px;
    cursor: pointer;
  }
  
  .gmap_canvas {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 20px;
  }
  
  .gmap_canvas iframe {
    max-width: 100%;
    width: 50%; 
    height: 200px;
  }
  </style>
  
  <script>
  export default {
    data() {
      return {
        name: "",
        email: "",
        message: "",
      };
    },
    methods: {
      submitForm() {
        // Lógica para enviar el formulario
      },
    },
  };
  </script>
  