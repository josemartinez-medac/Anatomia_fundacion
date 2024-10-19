import { createRouter, createWebHistory } from 'vue-router';
const routes = [
  //{ path: '/', redirect: '/login' },
  //{ path: '/login', component: LoginForm },
  { path: '/registro', component: () => import('@/views/SignUpView.vue') },
  {
    path: '/organos',
    name: 'organos',
    component: () => import('@/views/OrganoView.vue')
  },
  {
    path: '/naturalezas',
    name: 'naturalezas',
    component: () => import('@/views/NaturalezaView.vue')
  },
  {
    path: '/sedes',
    name: 'sedes',
    component: () => import('@/views/SedeView.vue')
  },
  {
    path: '/formatos',
    name: 'formatos',
    component: () => import('@/views/FormatoView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LoginView.vue')
  },
  {
    path: '/muestrasmenu',
    name: 'muestrasmenu',
    component: () => import('@/views/MenuMuestraView.vue')
  },
  {
    path: '/muestras',
    name: 'muestras',
    component: () => import('@/views/MuestraView.vue')
  },
  {
    path: '/informe/:codigo',
    name: 'informe',
    component: () => import('@/components/InformeComponent.vue'),
    props: true
  },
  {
    path: '/muestras2/:codigo/:naturaleza/:fecha_recepcion/:formato/:organo/:sede/:imgUrls',
    name: 'ViewMuestras2',
    component: () => import('@/views/Muestra2View.vue'),
    props: true
  },
  {
    path: '/revisar/:codigo/:naturaleza/:fecha_recepcion/:formato/:organo/:sede/:imgUrls/:calidad/:desccalidad/:interpretacion/:desc',
    name: 'ViewRevisar',
    component: () => import('@/views/RevisionView.vue'),
    props: true
  },
  {
    path: '/home',
    name: 'inicio',
    component: () => import('@/views/HomeView.vue')
  },
  {
    path: '/consultas',
    name: 'consultas',
    component: () => import('@/views/ConsultaView.vue')
  },
  /*{
    path:'/muestra/nueva',
    name: 'muestra-nueva',
    component: ()=>import('@/views/MuestraNuevaView.vue')
  },*/
  //{ path: '/restore-password', component: RestorePassword },
  //{ path: '/new-password', component: NewPassword },
  //{ path: '/technical-support', component: TecnicalSuport },
  //{ path: '/muestras', component: Muestras },
  /*{
    path: '/viewrevisar/:code/:nature/:dateColected/:conservation/:biopsy/:sede/:quality/:descQuality/:interpretation/:desc', 
    name: 'ViewRevisar',
    component: ViewRevisar,
    props: true
  },*/

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;










/*

//import axios from 'axios';
export default {
  props2: ['codigo', 'naturaleza', 'fecha_recepcion', 'formato', 'organo', 'sede', 'imgUrls'],
  data() {
    return {
      calidad2: '',
      desccalidad2: '',
      calidades2: [],
      interpretacion2: '',
      desc: '',
      interpretaciones: [],
    };
  },
  created() {
    this.fetchCalidades();
    this.fetchInterpretaciones();
  },
  methods: {
    fetchCalidades() {
      axios.get('http://localhost:8000/api/calidades/')
        .then(response => {
          this.calidades = response.data;
        })
        .catch(error => {
          console.error("Error fetching calidades:", error);
        });
    },
    fetchInterpretaciones() {
      axios.get('http://localhost:8000/api/interpretaciones/')
        .then(response => {
          this.interpretaciones = response.data;
        })
        .catch(error => {
          console.error("Error fetching interpretaciones:", error);
        });
    },
    submitForm() {


      this.$router.push({
        import { useRoute } from 'vue-router';
        const router = useRoute();
        const codigoPrincipal = () => {
          props: ['codigo']
          this.$router.push({
            name: 'ViewRevisar',
            params: {
              codigo2: this.codigo2,
              naturaleza2: this.naturaleza2,
              fecha_recepcion2: this.fecha_recepcion2,
              formato2: this.formato2,
              organo2: this.organo2,
              sede2: this.sede2,
              imgUrls2: this.imgUrls2,
              calidad2: this.calidad2,
              desccalidad2: this.desccalidad2,
              interpretacion2: this.interpretacion2,
              desc2: this.desc2
            }
          });
        },
        any() {
          this.calidades2.push({
            calidad2: this.calidad2,
            desccalidad2: this.desccalidad2
          });
          this.desccalidad2 = '';
        },
        other() {
          this.interpretaciones2.push({
            interpretacion2: this.interpretacion2,
            desc2: this.desc2
          });

          this.desc2 = '';

        },
      },
        watch: {
        calidad(newVal) {
          const selected = this.calidades2.find(item => item.codigo === newVal);
          this.desccalidad2 = selected ? selected.descripcion : '';
        },
        interpretacion(newVal) {
          const selected = this.interpretaciones2.find(item => item.codigo === newVal);
          this.desc2 = selected ? selected.descripcion : '';
        }
      },
        name: 'ViewMuestras2'
};

    codigo2: this.codigo2
  }
})
  }

</script >
*/