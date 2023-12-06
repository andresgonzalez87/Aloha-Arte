<template>
    <footer>
      <div class="footer-content">
        <div class="footer-section about">
          <h2>Acerca de nosotros</h2>
          <p>
            Somos ALOHA ARTE, estamos aquí para ayudarte a encontrar la propiedad ideal para ti y tu familia.
          </p>
        </div>
        <div class="footer-section contact">
          <h2>Contacto</h2>
          <p>
            Puedes ponerte en contacto con nosotros a través de los siguientes canales:
          </p>
          <ul>
            <li>Email: contacto@alohaarte.com</li>
            <li>Teléfono: +123 456 789</li>
          </ul>
        </div>
        <div class="footer-section links">
          <h2>Enlaces rápidos</h2>
          <ul>
            <li><router-link to="/">Inicio</router-link></li>
            <li><router-link to="/iniciarsesion">Iniciar sesión</router-link></li>
            <li><router-link to="/registro">Regístrate</router-link></li>
            <li><router-link to="/contacto">Contacto</router-link></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2023 ALOHA ARTE | Todos los derechos reservados</p>
      </div>
    </footer>
  </template>
  
  <style scoped>
  footer {
    background-color: #24303c;
    color: white;
    padding: 20px 0;
  }
  
  .footer-content {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
  }
  
  .footer-section {
    flex: 1;
    margin-bottom: 20px;
  }
  
  .footer-section h2 {
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  
  .footer-section p {
    font-size: 1rem;
  }
  ul {
  list-style: none;
  padding: 0;
  margin: 0;
  
}
  .footer-section ul {
    list-style: none;
    padding: 0;
  }
  
  .footer-section li {
    margin-bottom: 5px;
  }
  ul {
  list-style: none;
}
li {
  color: white; 
}
  .footer-bottom {
    text-align: center;
    margin-top: 20px;
  }
  
  .footer-bottom p {
    font-size: 0.8rem;
  }
  </style>
  
  
  <script>
  export default {
    // agregar lógica
  };
  </script>
  