<template>
    <section class="info">

        <p class="animation-1"> <b>Bienvenido a Inmobiliaria ALOHA-ARTE </b>Donde los sueños de encontrar el hogar perfecto
            se hacen realidad. <br>Con años de experiencia y un equipo dedicado, estamos aquí para ayudarte a encontrar la
            propiedad ideal para ti y tu familia.</p>
        <br><br>

        <div class="animation-2">
            <p><strong>Nuestros Servicios:</strong></p>
            <ul>
                <li>Alquiler de Propiedades: Ya sea que estés buscando tu primera casa, un lugar más grande para tu
                    creciente familia, estamos aquí para guiarte en cada paso del proceso de alquiler.</li>
                <li>Alquiler de oficinas/coworking: Para aquellos que buscan alquilar una oficina o un espacio para
                    trabajar, ofrecemos una amplia gama de opciones que se adaptan a diferentes necesidades y presupuestos.
                </li>
                <li>Gestión de Propiedades: Para propietarios, ofrecemos servicios de gestión de propiedades integrales,
                    asegurando que tus propiedades se mantengan en excelente estado y que los inquilinos estén satisfechos.
                </li>
            </ul>
        </div>
        <br><br>

        <div class="animation-3">
            <p><strong>Por qué elegirnos?</strong></p>
            <ul>
                <li>Profesionalismo: Nuestro equipo de agentes inmobiliarios está altamente capacitado y tiene un profundo
                    conocimiento del mercado local. Estamos comprometidos a brindarte un servicio profesional y
                    personalizado.</li>
                <li>Integridad: Valoramos la transparencia y la honestidad en todas nuestras transacciones. Puedes confiar
                    en nosotros para proporcionarte información precisa y fiable en todo momento.</li>
                <li>Enfoque Personalizado: Entendemos que cada cliente tiene necesidades y deseos únicos. Nos dedicamos a
                    entender tus requisitos y a encontrar la propiedad que se adapte perfectamente a tus expectativas.</li>
            </ul>
        </div>

    </section>
</template>
  
<script>
export default {
    data() {
        return {
            animation: 1,
        };
    },
};
</script>
  
<style scoped>
.nosotros {
    background: #678aad;
    font-family: 'calibri', 'Montserrat', 'sans-serif';
    height: 100%;
}
.info {
    margin: 200px 200px;
    color: white;
    text-align: center;
    font-size: 20px;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.animation-1 {
    animation: fadeIn 3s ease-in-out;
}

.animation-2 {
    animation: fadeIn 9s ease-in-out;
}

.animation-3 {
    animation: fadeIn 15s ease-in-out;
}

@media only screen and (min-width: 768px) and (max-width: 1024px) {
    .info {
        margin: 100px 100px;
    }
}

@media (max-width: 767px) {
    .info {
        margin: 100px 50px;
    }
}</style>
  