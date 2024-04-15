> [!IMPORTANT]
> Este proyecto necesita los archivos de configuración `transactional_config.cfg` y `etl_config.cfg` para funcionar. Sin embargo, no fueron incluidos en este repositorio por motivos de seguridad. Favor de contactar a cualquier integrante del grupo para que pueda proporcionar los archivos de configuración mencionados. 

# Integrantes

- 24003821 - Diego Bran
- 14001764 - Jose Calderón
- 14003689 - Yosef Maldonado

# Video

[Proyecto Final Python](https://drive.google.com/file/d/1wF_Zwee4-taDZ14SCA_Rns4G6uvATMA6/view?usp=sharing)

# Documentación de Notebooks para Data Warehouse de Modelo de Tienda

## Descripción General

Estos notebooks forman parte del proceso de diseño e implementación de un Data Warehouse para una tienda, utilizando un modelo relacional. `etl.ipynb` se encarga de los procesos ETL (Extract, Transform, Load), mientras que `transactional.ipynb` gestiona operaciones transaccionales.

## etl.ipynb

### Propósito

Este notebook implementa el proceso ETL para extraer datos desde diversas fuentes, transformarlos conforme a las necesidades del negocio y cargarlos en el Data Warehouse.

### Librerías Principales

- **boto3**: Interacción con AWS.
- **pandas y numpy**: Manipulación de datos.
- **psycopg2**: Conexión con bases de datos PostgreSQL.
- **Faker**: Generación de datos ficticios.

### Funciones Clave

- Configuración de AWS y PostgreSQL.
- Transformación de datos y generación de claves únicas.
- Visualización de datos para verificaciones.

## transactional.ipynb

### Propósito

Gestiona la inserción y manipulación de datos transaccionales en el Data Warehouse, asegurando que los datos sean actuales y relevantes.

### Librerías Principales

- Comparte librerías con `etl.ipynb` para una coherencia en el manejo de datos.

### Funciones Clave

- Inserción y actualización de datos transaccionales.
- Generación de datos transaccionales ficticios para pruebas.

## Configuración y Uso

Ambos notebooks utilizan configuraciones externas (`etl_config.cfg` y `transactional_config.cfg`) para manejar conexiones y parámetros. Es esencial revisar y ajustar estas configuraciones según el entorno de producción.

## Conclusiones

Estos notebooks son esenciales para la operación y mantenimiento del Data Warehouse de la tienda, permitiendo un manejo eficiente y estructurado de los datos tanto en el nivel ETL como transaccional.
