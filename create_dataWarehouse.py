DDL_QUERY = '''

create table if not exists dim_producto(

sk_id_producto serial primary key,
nombre_articulo varchar(100),
precio_venta decimal(11,2),
stock integer,
estado boolean,
descipcion_articulo varchar(255), 
nombre_categoria varchar(50),
descripcion_categoria varchar(255),

);

create table if not exists dim_persona(

sk_id_persona serial primary key,
idpersona integer,
idusuario integer,
idrol integer,
tipo_persona varchar(20),
nombre varchar(100),
tipo_documento varchar(20), 
num_documento varchar(20), 
direccion varchar(70), 
telefono varchar(20),
email varchar(50),
rol varchar(30),
clave bytea,
esato_usuario boolean,
estado_rol boolean,
);


create table if not exists  dim_ingreso(

sk_id_ingreso serial primary key, 
idproveedor integer, 
idusuario integer,
idarticulo integer,
datekey integer,
impuesto decimal(4,2), 
total decimal(11,2), 
estado boolean, 
cantidad integer,
precio decimal(11,2),
idcomprobante integer


);


create table dim_tiempo(
date_key INT primary key  NOT NULL,
full_date DATE,
day_of_week TINYINT,
day_num_in_month TINYINT,
day_num_overall SMALLINT,
day_name VARCHAR(9),
day_abbrev CHAR(3),
weekday_flag VARCHAR(7),
week_num_in_year TINYINT,
week_num_overall SMALLINT,
week_begin_date DATE,
week_begin_date_key INT,
month TINYINT,
month_num_overall SMALLINT,
month_name VARCHAR(9),
month_abbrev CHAR(3),
quarter TINYINT,
year SMALLINT,
yearmo INT,
fiscal_month TINYINT,
fiscal_quarter TINYINT,
fiscal_year SMALLINT,
last_day_in_month_flag CHAR(13),
same_day_year_ago_date DATE,

);


create table if not exists  dim_comrpbante(

idcomprobante serial primary key,
tipo_comrpobante varchar(20),
serie_comprobante varchar(7),
num_comrpobante varchar(10),

);


create table if not exists  fact_ventas(
idventa integer, 
idcliente integer, -- idpersona
idcomprobante integer,
datekey integer, 
impuesto decimal(4,2),
total decimal(11,2),
estado varchar(20), -- ojo ¿por que varchar? 
idarticulo integer,
cantidad integer, 
precio decimal(11,2), 
descuento decimal(11,2)

);
'''