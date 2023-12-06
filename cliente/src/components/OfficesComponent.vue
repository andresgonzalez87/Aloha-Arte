<template>
    <div class="title-cards">
      <h2><i>Oficinas en alquiler</i></h2>
    </div>
  
    <div class="container-card">
      <div v-for="(office, index) in offices" :key="index" class="card">
        <figure>
          <img :src="office.image" alt="Oficina">
        </figure>
        <div class="contenido-card">
          <h3>{{ office.title }}</h3>
          <p>{{ office.description }}</p>
          <a href="#">Ver</a>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        offices: [
          {
            title: "Oficina en Palermo",
            description: "Muy buena ubicación y entrada independiente",
            image: "/assets/office1.png",
          },
          {
            title: "Oficina en segundo piso, Microcentro",
            description: "Excelente ubicación y luminosa",
            image: "/assets/office2.png",
          },
          {
            title: "Oficina en Microcentro",
            description: "Cocina y patio propio",
            image: "/assets/office3.png",
          },
          {
            title: "Oficina en primer piso por escalera, Centro",
            description: "Muy luminosa y entrada independiente",
            image: "/assets/office4.png",
          },
          {
            title: "Oficina en barrio facultad de medicina",
            description: "Reciclada a nueva",
            image: "/assets/office5.png",
          },
          {
            title: "Oficina Microcentro",
            description: "Excelente ubicación y entrada independiente",
            image: "/assets/office6.png",
          },
          {
            title: "Oficina en Puerto Madero",
            description: "Excelente ubicación a metros del río",
            image: "/assets/office7.png",
          },
          {
            title: "Oficina en Puerto Madero",
            description: "A metros de Plaza de Mayo",
            image: "/assets/office8.png",
          },
        ],
      };
    },
    // agregar métodos y lógica 
  };
  </script>
  
  <style scoped>
  h2 {
    color: #fff;
    font-family: 'sans-serif';
  }
  
  .container-card {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-gap: 15px;
    max-width: 1100px;
    margin: auto;
  }
  
  .title-cards {
    width: 100%;
    max-width: 1080px;
    margin: auto;
    padding: 20px;
    margin-top: 150px;
    text-align: center;
    color: #7a7a7a;
  }
  
  .card {
    width: 100%;
    margin: 20px;
    border-radius: 6px;
    overflow: hidden;
    background: #fff;
    box-shadow: 0px 1px 10px rgba(0, 0, 0, 0.2);
    transition: all 400ms ease-out;
    cursor: default;
  }
  
  .card:hover {
    box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.4);
    transform: translateY(-3%);
  }
  
  .card img {
    width: 100%;
    height: 210px;
  }
  
  .card .contenido-card {
    padding: 15px;
    text-align: center;
  }
  
  .card .contenido-card h3 {
    margin-bottom: 15px;
    color: #7a7a7a;
  }
  
  .card .contenido-card p {
    line-height: 1.8;
    color: #6a6a6a;
    font-size: 14px;
    margin-bottom: 5px;
  }
  
  .card .contenido-card a {
    display: inline-block;
    padding: 10px;
    margin-top: 10px;
    text-decoration: none;
    color: #2fb4cc;
    border: 1px solid #2fb4cc;
    border-radius: 4px;
    transition: all 400ms ease;
    margin-bottom: 5px;
  }
  </style>
  