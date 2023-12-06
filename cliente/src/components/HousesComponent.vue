<template>
    <div class="title-cards">
      <h2><i>Casas en alquiler</i></h2>
    </div>
    <div class="container-card">
      <div v-for="(house, index) in houses" :key="index" class="card">
        <figure>
          <img :src="house.image">
        </figure>
        <div class="contenido-card">
          <h3>{{ house.name }}</h3>
          <p>{{ house.description }}</p>
          <a href="#">Ver</a>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        houses: [
          {
            name: "Casa en barrio privado",
            description: "360m2 5 ambientes 3 dormitorios 2 baños",
            image: "/assets/house1.png"
          },
          {
            name: "Casa en barrio privado",
            description: "300m2 4 ambientes 3 dormitorios 2 baños",
            image: "/assets/house2.png"
          },
          {
            name: "Casa en barrio privado",
            description: "250m2 4 ambientes 3 dormitorios 2 baños",
            image: "/assets/house3.png"
          },
          {
            name: "Casa en Sierra de los padres",
            description: "400m2 5 ambientes 4 dormitorios 2 baños",
            image: "/assets/house4.png"
          },
          {
            name: "Casa en Castelar",
            description: "350m2 5 ambientes 4 dormitorios 2 baños",
            image: "/assets/house5.png"
          },
          {
            name: "Casa en Nuñez",
            description: "200m2 4 ambientes 3 dormitorios 2 baños",
            image: "/assets/house6.png"
          },
          {
            name: "Casa en Belgrano",
            description: "190m2 3 ambientes 2 dormitorios 1 baños",
            image: "/assets/house7.png"
          },
          {
            name: "Casa en Flores",
            description: "250m2 4 ambientes 3 dormitorios 2 baños",
            image: "/assets/house8.png"
          }
        ]
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
  
  .container-card{
      width: 100%;
      display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-gap: 15px;
      max-width: 1100px;
      margin: auto;
  }
  
  .title-cards{
      width: 100%;
      max-width: 1080px;
      margin: auto;
      padding: 20px;
      margin-top: 150px;
      text-align: center;
      color: #7a7a7a;
  }
  
  .card{
      width: 100%;
      margin: 20px;
      border-radius: 6px;
      overflow: hidden;
      background:#fff;
      box-shadow: 0px 1px 10px rgba(0,0,0,0.2);
      transition: all 400ms ease-out;
      cursor: default;
  }
  
  .card:hover{
      box-shadow: 5px 5px 20px rgba(0,0,0,0.4);
      transform: translateY(-3%);
  }
  
  .card img{
      width: 100%;
      height: 210px;
  }
  
  .card .contenido-card{
      padding: 15px;
      text-align: center;
  }
  
  .card .contenido-card h3{
      margin-bottom: 15px;
      color: #7a7a7a;
  }
  
  .card .contenido-card p{
      line-height: 1.8;
      color: #6a6a6a;
      font-size: 14px;
      margin-bottom: 5px;
  }
  
  .card .contenido-card a{
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
  