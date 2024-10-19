from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_201_CREATED ,HTTP_404_NOT_FOUND#HTTP_204_NO_CONTENT
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Tipo, Sede, Naturaleza, Formato, Estado, Organo, CodificacionInterpretacion,  Aumento, Imagen, Usuario,Calidad,Interpretacion,Rol,Muestra#,Test
from .serializers import TipoSerializer, SedeSerializer, NaturalezaSerializer, FormatoSerializer, EstadoSerializer, OrganoSerializer, CodificacionInterpretacionSerializer, AumentoSerializer, ImagenSerializer, AuthUsuarioSerializer, CodificacionInterpretacionFliter, ImagenFilter,CalidadSerializer,InterpretacionSerializer,RolSerializer,MuestraSerializer,MuestraFilter#,TestSerializer
class TipoViewSet (ModelViewSet):
    queryset=Tipo.objects.all()
    serializer_class=TipoSerializer
    #permission_classes=[IsAuthenticated]
class SedeViewSet (ModelViewSet):
    queryset=Sede.objects.all()
    serializer_class=SedeSerializer
    #permission_classes=[IsAuthenticated]
class NaturalezaViewSet (ModelViewSet):
    queryset=Naturaleza.objects.all()
    serializer_class=NaturalezaSerializer
    #permission_classes=[IsAuthenticated]
class FormatoViewSet (ModelViewSet):
    queryset=Formato.objects.all()
    serializer_class=FormatoSerializer
    #permission_classes=[IsAuthenticated]
class EstadoViewSet (ModelViewSet):
    queryset=Estado.objects.all()
    serializer_class=EstadoSerializer
    #permission_classes=[IsAuthenticated]
class OrganoViewSet (ModelViewSet):
    queryset=Organo.objects.all()
    serializer_class=OrganoSerializer
    #permission_classes=[IsAuthenticated]
class CodificacionInterpretacionViewsSet (ModelViewSet):
    queryset=CodificacionInterpretacion.objects.all()
    serializer_class=CodificacionInterpretacionSerializer
    filterset_class=CodificacionInterpretacionFliter
    #permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
class MuestraViewSet (ModelViewSet):
    queryset=Muestra.objects.all()
    serializer_class=MuestraSerializer
    filterset_class=MuestraFilter #o 
    #permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
class CreateMuestraView(APIView):
    def post(self, request):
        data = request.data.copy()
        print(data)
        fecha_recepcion = data.get('fecha_recepcion')
        naturaleza_code = data.get('naturaleza')
        formato_f = data.get('formato')
        organo_o = data.get('organo')
        sede_code = data.get('sede')
        username_u = data.get('username')
        calidad_c = data.get('calidad')
        interpretacion_i = data.get('interpretacion')
        descripcioncal=data.get('descripcionCal')
        descripcionInt=data.get('descripcionInt')
        print([username_u, formato_f])
        #dgñafhypq
        try:
            naturaleza = get_object_or_404(Naturaleza, naturaleza=naturaleza_code)
            formato = get_object_or_404(Formato, formato=formato_f)
            organo = get_object_or_404(Organo, organo=organo_o)
            sede = get_object_or_404(Sede, sede=sede_code)
            user = get_object_or_404(User, username=username_u)
            usuario = get_object_or_404(Usuario, username=user)
            #usuario = get_object_or_404(Usuario, username=user)#lg
            calidad = get_object_or_404(Calidad, codigo=calidad_c)

            muestra = Muestra.objects.create(
                codigo=data.get('codigo'),
                fecha_recepcion=fecha_recepcion,
                naturaleza=naturaleza,
                formato=formato,
                organo=organo,
                sede=sede,
                usuario=usuario,
                calidad=calidad,
                interpretacion=interpretacion_i,
                descripcionCal=descripcioncal,
                descripcionInt=descripcionInt
            )
            return Response({"message": "La muestra ha sido creada"}, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
"""class CreateMuestraView (APIView):
    queryset=Muestra.objects.all()
    serializer_class=MuestraSerializer
    #permission_classes=[IsAuthenticated]
    def post (self,request):
        data = request.data.copy()
        #imagenes = request.FILES.getlist('imagenes')
        #zooms = request.data.getlist('zooms')
        fecha_recepcion=request.data.get('fecha_recepcion')
        naturaleza_code=request.data.get('naturaleza')
        formato_f=request.data.get('formato')
        organo_o=request.data.get('organo')
        sede_code=request.data.get('sede')
        #estado_e=request.data.get('estado')
        username_u=request.data.get('username')
        calidad_c=request.data.get('calidad')
        interpretacion_i=request.data.get('interpretacion')
        try:
            naturaleza=get_object_or_404(Naturaleza, naturaleza=naturaleza_code)
            formato=get_object_or_404(Formato, formato=formato_f)
            organo=get_object_or_404(Organo, organo=organo_o)
            sede=get_object_or_404(Sede, sede=sede_code)
            #estado=get_object_or_404(Estado, estado=estado_e)
            username=get_object_or_404(User, username=username_u)
            calidad=get_object_or_404(Calidad, calidad=calidad_c)
            #interpretacion=get_object_or_404(Interpretacion,calidad=interpretacion_i)
            #usuario = get_object_or_404(Usuario, username=username)
            muestra=Muestra.objects.create(
                codigo=data.get('codigo'),
                fecha_recepcion=fecha_recepcion,
                naturaleza=naturaleza, 
                formato=formato, 
                organo=organo,
                sede=sede,
                #estado=estado,
                username=username,
                calidad=calidad,
                interpretacion=interpretacion_i)
            for i, imagen in enumerate(imagenes):
                zoom = zooms[i] if i < len(zooms) else 'x4'  # Default zoom if not provided
                Imagen.objects.create(muestra=muestra, imagen=imagen, zoom=zoom)
            return Response({"message":"La muestra ha sido creada"},status=HTTP_201_CREATED)
        except Exception as e:
            return Response({"error":str(e)},status=500)"""

"""
Añadido Clase que modifica
"""
class UpdateMuestraView(APIView):
    def put(self, request):
        try:
            # Obtener el código del informe de los datos de la solicitud
            codigo_informe = request.data.get('codigo')
            if not codigo_informe:
                return Response({"error": "Se requiere el código del informe"}, status=HTTP_400_BAD_REQUEST)

            # Buscar la muestra por el código
            muestra = get_object_or_404(Muestra, codigo=codigo_informe)
            
            # Actualizar solo los campos proporcionados en la solicitud
            for field, value in request.data.items():
                if field == 'codigo':
                    continue  # No permitimos cambiar el código
                elif field == 'naturaleza':
                    muestra.naturaleza = get_object_or_404(Naturaleza, naturaleza=value)
                elif field == 'formato':
                    muestra.formato = get_object_or_404(Formato, formato=value)
                elif field == 'organo':
                    muestra.organo = get_object_or_404(Organo, organo=value)
                elif field == 'sede':
                    continue  # No permitimos cambiar la sede
                elif field == 'username':
                    continue  # No permitimos cambiar el username
                elif field == 'calidad':
                    muestra.calidad = get_object_or_404(Calidad, codigo=value)
                elif hasattr(muestra, field):
                    setattr(muestra, field, value)

            muestra.save()
            
            # Preparar respuesta
            response_data = {
                "message": "El informe ha sido actualizado",
                "informe": {
                    "codigo": muestra.codigo,
                    "fecha_recepcion": muestra.fecha_recepcion,
                    "naturaleza": muestra.naturaleza.naturaleza if muestra.naturaleza else None,
                    "formato": muestra.formato.formato if muestra.formato else None,
                    "organo": muestra.organo.organo if muestra.organo else None,
                    "sede": muestra.sede.sede if muestra.sede else None,
                    "usuario": muestra.usuario.username.username if muestra.usuario else None,
                    "calidad": muestra.calidad.codigo if muestra.calidad else None,
                    "interpretacion": muestra.interpretacion,
                    "descripcionCal": muestra.descripcionCal,
                    "descripcionInt": muestra.descripcionInt
                }
            }
            
            return Response(response_data, status=HTTP_200_OK)

        except Muestra.DoesNotExist:
            return Response({"error": "Informe no encontrado"}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

"""
clase final
"""
class AumentoViewSet (ModelViewSet):
    queryset=Aumento.objects.all()
    serializer_class=AumentoSerializer
    #permission_classes=[IsAuthenticated]
class ImagenViewSet (ModelViewSet):
    queryset=Imagen.objects.all()
    serializer_class=ImagenSerializer
    filterset_class=ImagenFilter
    #permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
class AuthUserViewSet (ModelViewSet):
    queryset=Usuario.objects.all()
    serializer_class=AuthUsuarioSerializer
    #permission_classes=[IsAuthenticated]
class RegisterView(APIView):
    queryset=Usuario.objects.all()
    serializer=AuthUsuarioSerializer
    permissions_classes=[AllowAny]
    def post(self, request):
        email = request.data.get('email')
        username=email.split('@')[0]
        password = request.data.get('password')
        sede_s = request.data.get('sede')
        if not email.endswith('@medac.es') and not email.endswith('@alu.medac.es') \
            and not email.endswith('@doc.medac.es') and not password:
            return Response({"error": "Username and password are required"}, status=HTTP_400_BAD_REQUEST)
        if Usuario.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=HTTP_400_BAD_REQUEST)
        sede = get_object_or_404(Sede, sede=sede_s)
        if email.endswith('@alu.medac.es'): rol='Estudiante'
        elif email.endswith('@doc.medac.es') or email.endswith('@medac.es'): rol='Profesor/a'
        rol_guapo=get_object_or_404(Rol, rol=rol)
        user = User.objects.create_user(username=username, email=email, password= password)
        usuario = Usuario.objects.create(username=user, sede=sede, rol=rol_guapo)
        return Response({"message": "User created successfully"}, status=HTTP_201_CREATED)
"""class MuestraDeleteView(APIView):
    #permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            tipo_obj = Muestra.objects.get(id=pk)
        except Muestra.DoesNotExist:
            return Response({"error": "Tipo not found"}, status=HTTP_404_NOT_FOUND)
        tipo_obj.delete()
        return Response(status=HTTP_204_NO_CONTENT)"""
class CalidadViewSet(ModelViewSet):
    queryset=Calidad.objects.all()
    serializer_class=CalidadSerializer
class InterpretacionViewSet(ModelViewSet):
    queryset=Interpretacion.objects.all()
    serializer_class=InterpretacionSerializer

class RolViewSet (ModelViewSet):
    queryset=Rol.objects.all()
    serializer_class=RolSerializer
    #permission_classes=[IsAuthenticated]
"""class TestViewSet (ModelViewSet):
    queryset=Test.objects.all()
    serializer_class=TestSerializer"""
