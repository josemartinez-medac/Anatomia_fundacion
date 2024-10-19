<template>
  <div class="container-all-muestras" style="margin-top: 120px;">
    <div class="muestras-h2">
      <h2>Buscar muestra por:</h2>
    </div>

    <div class="container-form-muestras">
      <form class="form-muestras" @submit.prevent="searchMuestras">
        <div style="display: flex; justify-content: space-between;">
          <div>
            <div>
              <label for="codigo">Código de la muestra</label>
              <input type="text" class="input-muestras" name="code" v-model="codigo" id="codigo" />
            </div>
            <div>
              <label for="fecha_recepcion">Fecha Recepción</label>
              <input class="input-muestras" type="date" v-model="fecha_recepcion" name="dateColected"
                id="fecha_recepcion" />
            </div>
          </div>
          <div>
            <div>
              <label for="naturaleza">Naturaleza de la muestra</label>
              <select class="input-muestras" v-model="naturaleza" id="naturaleza">
                <option v-for="nat in naturalezas" :key="nat.naturaleza" :value="nat.naturaleza">{{ nat.naturaleza }}
                </option>
              </select>
            </div>
            <div>
              <label for="formato">Conservación de muestra</label>
              <select class="input-muestras" v-model="formato" id="formato">
                <option v-for="fmt in formatos" :key="fmt.formato" :value="fmt.formato">{{ fmt.formato }}</option>
              </select>
            </div>
          </div>
          <div>
            <div>
              <label for="organo">Opciones biopsia</label>
              <select class="input-muestras" v-model="organo" id="organo">
                <option v-for="org in organos" :key="org.organo" :value="org.organo">{{ org.organo }}</option>
              </select>
            </div>
            <div>
              <label for="sede">Centro de procedencia</label>
              <select class="input-muestras" v-model="sede" id="sede">
                <option v-for="s in sedes" :key="s.sede" :value="s.sede">{{ s.sede }}</option>
              </select>
            </div>
          </div>
        </div>

        <button class="btn-muestras" type="submit">Buscar</button>
        <div v-if="hasSearched">
          <div v-if="filteredmuestras.length > 0">
            <h3>
              Resultados.
            </h3>
            <ul v-for="m in filteredmuestras" :key="m.codigo">
              <li>
                <router-link
                  :to="`/informe/${m.codigo}`">
                  <span>Informe {{ m.codigo }} del usuario {{ m.usuario.username }}</span>
                  
                </router-link>
              </li>
            </ul>
          </div>
          <h3 v-else>
            No se encontraron resultados.
          </h3>
        </div>
      </form>
    </div>



  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const codigo = ref('');
const naturaleza = ref('');
const organos = ref([]);
const naturalezas = ref([]);
const formatos = ref([]);
const sedes = ref([]);
const formato = ref('');
const fecha_recepcion = ref('');
const organo = ref('');
const sede = ref('');
const usuarios = ref([]);
const usuario = ref('');
const calidades = ref([]);
const calidad = ref('');
const interpretaciones = ref([]);
const interpretacion = ref('');
const muestras = ref([]);
const filteredmuestras = ref([]);
const hasSearched = ref(false);

onMounted(() => {
  axios.all([
    axios.get('http://localhost:8000/api/muestras/'),
    axios.get('http://localhost:8000/api/organos/'),
    axios.get('http://localhost:8000/api/naturalezas/'),
    axios.get('http://localhost:8000/api/formatos/'),
    axios.get('http://localhost:8000/api/sedes/'),
    axios.get('http://localhost:8000/api/usuarios/'),
    axios.get('http://localhost:8000/api/calidades/'),
    axios.get('http://localhost:8000/api/interpretaciones/'),
  ]).then(axios.spread((muestrasResp, organosResp, naturalezasResp, formatosResp, sedesResp, usuariosResp, calidadesResp, interpretacionesResp) => {
    muestras.value = muestrasResp.data;
    organos.value = organosResp.data;
    naturalezas.value = naturalezasResp.data;
    formatos.value = formatosResp.data;
    sedes.value = sedesResp.data;
    usuarios.value = usuariosResp.data;
    calidades.value = calidadesResp.data;
    interpretaciones.value = interpretacionesResp.data;
  })).catch(e => {
    console.error('Error al cargar los datos:', e);

  })
});

const searchMuestras = () => {
  hasSearched.value = true;
  filteredmuestras.value = muestras.value.filter(muestra => {
    return (!codigo.value || muestra.codigo.toString() === codigo.value.toString()) &&
      (!naturaleza.value || muestra.naturaleza === naturaleza.value) &&
      (!formato.value || muestra.formato === formato.value) &&
      (!fecha_recepcion.value || muestra.fecha_recepcion === fecha_recepcion.value) &&
      (!organo.value || muestra.organo === organo.value) &&
      (!sede.value || muestra.sede === sede.value) &&
      (!usuario.value || muestra.usuario === usuario.value) &&
      (!calidad.value || muestra.calidad === calidad.value) &&
      (!interpretacion.value || muestra.interpretacion === interpretacion.value)
  });
};
</script>

<style src="../assets/css/muestras.css"></style>
