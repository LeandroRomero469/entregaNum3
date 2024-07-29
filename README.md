# nueva_entrega3

## Primero usar git clone https://github.com/LeandroRomero469/entregaNum3


# Despues usar pip install -r requirements.txt, para instalar las versiones usadas en este proyecto.

## Tenemos que entrar dentro de entreganum3 para usar el manage.py

## Uso

### Modelos

#### Proyecto
**Este modelo permite gestionar proyectos.**

- **Campos**:
 # - `titulo`: Título del proyecto.
 # - `descripcion`: Descripción detallada del proyecto.
 # - `fecha_inicio`: Fecha de inicio del proyecto.
 # - `fecha_fin`: Fecha de finalización del proyecto (opcional).

 #### Habilidad
**Este modelo permite gestionar habilidades.**

- **Campos**:
# - `nombre`: Nombre de la habilidad.
#  - `nivel`: Nivel de la habilidad (e.g., 'Principiante', 'Intermedio', 'Avanzado').

#### Educacion
**Este modelo permite gestionar la educación.**

- **Campos**:
#  - `institucion`: Nombre de la institución educativa.
#  - `titulo`: Título obtenido.
#  - `fecha_inicio`: Fecha de inicio de los estudios.
#  - `fecha_fin`: Fecha de finalización de los estudios (opcional).
#  - `descripcion`: Descripción adicional de los estudios (opcional).

#### Experiencia
### Este modelo permite gestionar la experiencia laboral.

- **Campos**:
#  - `empresa`: Nombre de la empresa.
#  - `puesto`: Puesto desempeñado.
#  - `fecha_inicio`: Fecha de inicio en el puesto.
#  - `fecha_fin`: Fecha de finalización en el puesto (opcional).
#  - `descripcion`: Descripción de las responsabilidades y logros.