<template>
  <br>
    <div>
      <section class="top-banner">
        <div class="container">
          <h1 class="heading">Verificá cómo está el clima antes de viajar</h1>
          <form @submit.prevent="searchCity">
            <input v-model="city" type="text" placeholder="Buscar ciudad">
            <button type="submit">Enviar</button>
            <span class="msg"></span>
          </form>
        </div>
      </section>
      <section class="ajax-section">
        <div class="container">
          <ul class="cities">
            <li v-for="(cityData, index) in cities" :key="index" class="city">
              <h2 class="city-name" :data-name="`${cityData.name},${cityData.sys.country}`">
                <span>{{ cityData.name }}</span>
                <sup>{{ cityData.sys.country }}</sup>
              </h2>
              <div class="city-temp">{{ Math.round(cityData.main.temp) }}<sup>°C</sup></div>
              <figure>
                <img class="city-icon" :src="getWeatherIconUrl(cityData.weather[0].icon)" :alt="cityData.weather[0].main">
                <figcaption>{{ cityData.weather[0].description }}</figcaption>
              </figure>
            </li>
          </ul>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        city: "",
        cities: [],
        apiKey: "c2c74aeb2f8a362613fe0039d4faed8e",
      };
    },
    methods: {
      searchCity() {
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${this.city}&appid=${this.apiKey}&units=metric`;
  
        fetch(url)
          .then(response => response.json())
          .then(data => {
            this.cities.push(data);
          })
          .catch(() => {
            // Handle error
            console.error("Error fetching weather data");
          });
  
        // Clear input
        this.city = "";
      },
      getWeatherIconUrl(iconCode) {
        return `https://openweathermap.org/img/wn/${iconCode}@2x.png`;
      },
    },
  };
  </script>
  
  <style scoped>
  .top-banner {
    width: 400px;
    background: #24303c;
    padding: 30px;
    margin: auto;
    margin-top: 100px;
    margin-bottom: 50px;
    border-radius: 4px;
    font-family: 'calibri';
    color: white;
    box-shadow: 7px 13px 37px #000;
}
h1 {
    font-size: 22px;
    margin-bottom: 20px;
    text-align: center;
}
.container input {
    width: 100%;
    background: #24303c;
    padding: 10px;
    border-radius: 4px;
    border: 1px solid #1f53c5;
    font-family: 'calibri';
    font-size: 18px;
    color: white;
}
button {
    width: 100%;
    background: #1f53c5;
    border: none;
    padding: 12px;
    color: white;
    margin: 16px 0;
    font-size: 16px;
    cursor: pointer;
}
.ajax-section .cities {
    display: grid;
    grid-gap: 30px 20px;
    grid-template-columns: repeat(4, 1fr);
    justify-content: center;
    justify-items: center;
}
@media only screen 
  and (min-width: 768px) 
  and (max-width: 1024px) {
      .ajax-section .cities{
          grid-template-columns: 1fr 1fr;
      }
  }   
  @media (max-width: 767px) {
    .ajax-section .cities{
        grid-template-columns: 1fr;
    }
}
  </style>
  