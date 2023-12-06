<template>
  <div class="title-cards">
    <h2><i>Departamentos en alquiler</i></h2>
  </div>
  <div class="container-card">
    <div v-for="(department, index) in departments" :key="index" class="card">
      <figure>
        <img :src="department.image">
      </figure>
      <div class="contenido-card">
        <h3>{{ department.name }}</h3>
        <p>{{ department.description }}</p>
        <a href="#">Ver</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      departments: [
        {
          name: "Departamento en Caballito, CABA",
          description: "4 ambientes 2 baños",
          image: "/assets/depto1.jpg"
        },
        {
          name: "Departamento en Belgrano, CABA",
          description: "2 ambientes 2 baños",
          image: "/assets/depto2.jpg"
        },
        {
          name: "Departamento en Belgrano, CABA",
          description: "2 ambientes 1 baños",
          image: "/assets/depto3.jpg"
        },
        {
          name: "Departamento en Belgrano, CABA",
          description: "3 ambientes 2 baños",
          image: "/assets/depto4.jpg"
        },
        {
          name: "Loft en Belgrano, CABA",
          description: "1 ambiente dividido 1 baños",
          image: "/assets/depto5.jpg"
        },
        {
          name: "Departamento en Recoleta, CABA",
          description: "3 ambientes 2 baños",
          image: "/assets/depto6.jpg"
        },
        {
          name: "Departamento en Nuñez",
          description: "4 ambientes 3 baños",
          image: "/assets/depto7.jpg"
        }
      ]
    };
  },
  // agregar métodos y lógica específica del componente
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
