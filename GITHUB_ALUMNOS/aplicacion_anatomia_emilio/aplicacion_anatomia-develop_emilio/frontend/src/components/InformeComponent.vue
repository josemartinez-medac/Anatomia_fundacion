<template>
  <navbar-component />
  <div class="container-all-muestras">
    <div class="muestras-h2 tituloInforme">
      <div class="h2informes">
        <h2>Informe Nº: {{ props.codigo }}</h2>
        <h2>Usuario: {{ usuario }}</h2>
      </div>
      <div class="btn btn-group">
        <button class="btn btn-muestras" type="button" id="editaModifica" @click="toogleEditar">Editar Informe</button>
        <button class="btn btn-muestras bg-green oculto" type="submit" id="confirmaModifica" @click="modificarInforme">Confirmar</button>
        <button class="btn btn-muestras" type="button" @click="printPage">Imprimir Informe</button>
        <button class="btn btn-muestras" type="submit" @click="volver">Volver</button>
      </div>
    </div>
    <div class="container-form-muestras">
      <form class="form-muestras">
        <div class="divContenido">
          <div class="fila fila1">
            <label for="codigo"><b>Código de la muestra: </b>
              {{ props.codigo }}
            </label>

            <label for="fecha_recepcion"><b>Fecha: </b>
              <span class="editar displayInline">{{ fecha }}</span>
              <span class="introducir displayNone">
                <input type="date" class="input-muestras" v-model="fecha" />
              </span>
            </label>
            <label for="nature"><b>Usuario: </b>{{ usuario }}</label>
            <label for="nature"><b>Centro: </b>{{ centro }}</label>

          </div>
          <div class="fila fila2">
            <label for="nature"><b>Naturaleza: </b>
              <!--LLEVA UN SELECT-->
              <span class="editar displayInline">{{ naturaleza }}</span>
              <span class="introducir displayNone">
                <select class="input-muestras" v-model="naturaleza" required>
                  <option name="naturaleza" v-for="nat in selectNaturalezas" :key="nat.codigo" :value="nat.naturaleza">
                    {{ nat.naturaleza }}</option>
                </select>
              </span>
            </label>
            <label for="conservation"><b>formato:</b>
              <!--LLEVA UN SELECT-->
              <span class="editar displayInline">{{ formato }}</span>
              <span class="introducir displayNone">
                <select class="input-muestras" v-model="formato" required>
                  <option name="naturaleza" v-for="fmt in selectFormato" :key="fmt.formato" :value="fmt.formato">{{
                    fmt.formato }}</option>
                </select>

              </span>
            </label>
            <label for="conservation"><b>Organo: </b>
              <!--LLEVA UN SELECT-->
              <span class="editar displayInline">{{ organo }}</span>
              <span class="introducir displayNone">
                <select class="input-muestras" v-model="organo" required>
                  <option name="naturaleza" v-for="org in selectOragano" :key="org.organo" :value="org.organo">{{
                    org.organo }}</option>
                </select>
              </span>
            </label>

          </div>

          <div class="fila fila3">
            <label>
              <b>
                <span class="editar displayInline"> <b>Calidad de la muestra: </b>{{ calidad }}</span>
                <span class="introducir displayNone selectIntro">
                  <select class="input-muestras" v-model="calidad" required>
                    <option name="naturaleza" v-for="cad in selectCalidad" :key="cad.codigo" :value="`${cad.codigo}`">
                      <b>Calidad de la muestra: </b>{{ cad.codigo }}
                    </option>
                  </select>
                </span>
              </b>
            </label>
            <textarea id="idCalidad" class="input-muestras" v-model="desCalidad" disabled>
            </textarea>
          </div>
          <div class="fila fila3">
            <label>
              <b>
                <span class="editar displayInline"> <b>Interpretacion de la muestra: </b> {{ interpretacion }}</span>
                <span class="introducir displayNone selectIntro">
                  <select class="input-muestras" v-model="interpretacion" required>
                    <option name="interpretacion" v-for="cad in selectInterpretacion" :key="cad.codigo"
                      :value="cad.codigo">
                      <b>Interpretacion de la muestra: </b>{{ cad.codigo }}
                    </option>
                  </select>

                </span>
              </b>
            </label>
            <textarea id="idInterpretacion" class="input-muestras" v-model="desInterpretacion" disabled>
            </textarea>
          </div>
        </div>
        
      </form>

    </div>

  </div>

</template>


<script setup>
import { ref, onMounted, defineProps, } from 'vue';
import axios from 'axios';
import NavbarComponent from './NavbarComponent.vue';
import router from '@/router';

const props = defineProps({
  codigo: { type: String, required: true },
  fecha: { type: String, required: true },

});
const isEditing = ref(false);

const muestra = ref({});
const fecha = ref('');
const naturaleza = ref('');
const formato = ref('');
const organo = ref('');
const centro = ref('');
const usuario = ref('');
const calidad = ref('');
const desCalidad = ref('');
const interpretacion = ref('');
const desInterpretacion = ref('');

const imagenes = ref('');
const zoom = ref('');
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
const selectNaturalezas = ref('');
const selectFormato = ref('');
const selectOragano = ref('');
const selectCalidad = ref('');
const selectInterpretacion = ref('');

onMounted(async () => {
  try {
    const response = await axios.get(`http://localhost:8000/api/muestras/?codigo=${props.codigo}`);
    muestra.value = response.data;
    fecha.value = muestra.value[0].fecha_recepcion;
    naturaleza.value = muestra.value[0].naturaleza;
    formato.value = muestra.value[0].formato;
    organo.value = muestra.value[0].organo;
    centro.value = muestra.value[0].sede;
    usuario.value = muestra.value[0].usuario.username;
    calidad.value = muestra.value[0].calidad;
    desCalidad.value = muestra.value[0].descripcionCal;
    interpretacion.value = muestra.value[0].interpretacion;
    desInterpretacion.value = muestra.value[0].descripcionInt;
    imagenes.value = muestra.value[0].imagenes;
    zoom.value = muestra.value[0].zoom;


  } catch (e) {
    console.error('Error al cargar datos:', e);
  }

  axios.all([
    axios.get('http://localhost:8000/api/organos/'),
    axios.get('http://localhost:8000/api/naturalezas/'),
    axios.get('http://localhost:8000/api/formatos/'),
    axios.get('http://localhost:8000/api/calidades/'),
    axios.get('http://localhost:8000/api/interpretaciones/'),
  ]).then(axios.spread((organos, naturalezas, formatos, calidad, interpretacion) => {
    selectOragano.value = organos.data;
    selectNaturalezas.value = naturalezas.data;
    selectFormato.value = formatos.data;
    selectCalidad.value = calidad.data;
    selectInterpretacion.value = interpretacion.data;

  })).catch(e => {
    console.error('Error al cargar los datos:', e);
  })


});
const toogleEditar = () => {
  isEditing.value = !isEditing.value;

  const editarElements = document.querySelectorAll('.editar');
  const introducirElements = document.querySelectorAll('.introducir');
  const editButton = document.getElementById('editaModifica');
  const confirmaModifica = document.getElementById('confirmaModifica');
  const idCalidad = document.getElementById('idCalidad');
  const idInterpretacion = document.getElementById('idInterpretacion');

  if (isEditing.value) {
    editButton.textContent = 'Cancelar';
    editButton.classList.add("bg-red");
    confirmaModifica.classList.remove("oculto");
    idCalidad.disabled = false;
    idInterpretacion.disabled = false;
    idCalidad.classList.add("textAreaEdited");
    idInterpretacion.classList.add("textAreaEdited");
  } else {
    editButton.textContent = 'Editar Informe';
    editButton.classList.remove("bg-red");
    confirmaModifica.classList.add("oculto");
    idCalidad.disabled = true;
    idInterpretacion.disabled = true;
    idCalidad.classList.remove("textAreaEdited");
    idInterpretacion.classList.remove("textAreaEdited");
    window.location.reload();
  }

  editarElements.forEach(el => {
    el.classList.toggle('displayInline');
    el.classList.toggle('displayNone');
  });

  introducirElements.forEach(el => {
    el.classList.toggle('displayNone');
    el.classList.toggle('displayInline');
  });
};

/*const printPDF = () => {
const content = document.getElementById('pdfContent');

html2craft.takeSnapshot(content, {
  onrendered: function(canvas) {
    const imgData = clearSnapshot.toDataURL('image/png');
    const pdf = new jsPDF({
      orientation: 'portrait',
      unit: 'px',
      flipHorizontal: 1
    });

    pdf.addImage(imgData, 'PNG', 0, 0);
    round.save('download.pdf');
  }
});
};*/


const modificarInforme =(async () => {
  
  try {
        await axios.put('http://127.0.0.1:8000/api/muestra/update/', {
          codigo: props.codigo,
          fecha_recepcion: fecha.value,
          naturaleza: naturaleza.value,
          organo: organo.value,
          formato: formato.value,
          calidad: calidad.value,
          interpretacion: interpretacion.value,
          descripcionCal: desCalidad.value,
          descripcionInt: desInterpretacion.value,
          });
          window.location.reload();
  } catch (error) {
    console.error('Error al modificar el informe:', error);
  }
});

function volver() {
  router.push('/consultas');
}

const printPage = () => {
  window.print();
}
</script>
<style src="../assets/css/muestras.css"></style>




