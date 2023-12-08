<template>
  <div class="content">
    <header class="fixed-navbar">
      <div class="logo">
        <router-link to="/" class="navbar-logo">
          <img src="/assets/logo-sin-fondo.png" alt="Logo">
        </router-link>
      </div>

      <div class="bars" @click="toggleNavbar">
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
      </div>

      <nav class="nav-bar" :class="{ active: isNavbarActive }">
        <ul>
          <li>
            <router-link to="/" class="nav-link" exact>
              Home
            </router-link>
          </li>
          <li>
            <router-link to="/iniciarsesion" class="nav-link">
              Iniciar sesión
            </router-link>
          </li>
          <li>
            <router-link to="/registro" class="nav-link">
              Regístrate
            </router-link>
          </li>
          <li>
            <router-link to="/nosotros" class="nav-link">
              Sobre nosotros
            </router-link>
          </li>
          <li>
            <router-link to="/clima" class="nav-link">
              Clima
            </router-link>
          </li>
          <li>
            <router-link to="/contacto" class="nav-link">
              Contacto
            </router-link>
          </li>
          <li>
            <router-link to="/administracion" class="nav-link">
              Administración
            </router-link>
          </li>
        </ul>
      </nav>
    </header>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isNavbarActive: false,
    };
  },
  methods: {
    toggleNavbar() {
      this.isNavbarActive = !this.isNavbarActive;
    },
  },
};
</script>

<style scoped>
header {
  width: 100%;
  height: 80px;
  background-color: #242526;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 100px;
  position: fixed;
}
.fixed-navbar {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000; 
}

.navbar-logo {
  display: inline-block;
  vertical-align: middle;
  width: 70px;
}

.navbar-logo img {
  display: block;
  width: 120%;
  height: auto;
  background-color: #242526;
}

.bars {
  display: none;
}

.nav-bar ul {
  display: flex;
}

.nav-bar ul li .nav-link {
  display: block;
  color: #ffffff;
  font-size: 18px;
  padding: 10px 25px;
  border-radius: 15px;
  transition: 0.2s;
  margin: 0 5px;
  cursor: pointer;
}

.nav-bar ul li .nav-link:hover {
  background-color: #363738;
}

@media (max-width: 1024px) {
  header {
    padding: 0px 30px;
  }
  .bars {
    display: block;
    cursor: pointer;
  }
  .bars .line {
    width: 30px;
    height: 3px;
    background-color: #ffffff;
    margin: 6px 0px;
  }
  .nav-bar {
    height: 0px;
    position: absolute;
    top: 80px;
    left: 0px;
    right: 0;
    width: 100vw;
    transition: 0.5s;
    background-color: #242526;
    overflow: hidden;
  }
  .nav-bar.active {
    height: 450px;
  }
  .nav-bar ul {
    display: block;
    width: fit-content;
    margin: 80px auto 0 auto;
    text-align: center;
    transition: 0.5s;
    opacity: 0;
  }
  .nav-bar.active ul {
    opacity: 1;
  }
  .nav-bar ul li .nav-link {
    margin-bottom: 20px;
  }
}
</style>
