DDL_QUERY = '''
-- Crear tabla "categoria"
CREATE TABLE IF NOT EXISTS categoria (
  idcategoria SERIAL PRIMARY KEY,
  nombre VARCHAR(50),
  descripcion VARCHAR(255),
  estado BOOLEAN
);

-- Crear tabla "articulo"
CREATE TABLE IF NOT EXISTS articulo (
  idarticulo SERIAL PRIMARY KEY,
  idcategoria INTEGER REFERENCES categoria(idcategoria),
  codigo VARCHAR(50),
  nombre VARCHAR(100),
  precio_venta DECIMAL(11,2),
  stock INTEGER,
  descripcion VARCHAR(255),
  imagen VARCHAR(20),
  estado BOOLEAN
);

-- Crear tabla "persona"
CREATE TABLE IF NOT EXISTS persona (
  idpersona SERIAL PRIMARY KEY,
  tipo_persona VARCHAR(20),
  nombre VARCHAR(100),
  tipo_documento VARCHAR(20),
  num_documento VARCHAR(20),
  direccion VARCHAR(70),
  telefono VARCHAR(20),
  email VARCHAR(50)
);

-- Crear tabla "rol"
CREATE TABLE IF NOT EXISTS rol (
  idrol SERIAL PRIMARY KEY,
  nombre VARCHAR(30),
  descripcion VARCHAR(255),
  estado BOOLEAN
);

-- Crear tabla "usuario"
CREATE TABLE IF NOT EXISTS usuario (
  idusuario SERIAL PRIMARY KEY,
  idrol INTEGER REFERENCES rol(idrol),
  nombre VARCHAR(100),
  tipo_documento VARCHAR(20),
  num_documento VARCHAR(20),
  direccion VARCHAR(70),
  telefono VARCHAR(20),
  email VARCHAR(50),
  clave BYTEA,
  estado BOOLEAN
);

-- Crear tabla "venta"
CREATE TABLE IF NOT EXISTS venta (
  idventa SERIAL PRIMARY KEY,
  idcliente INTEGER REFERENCES persona(idpersona),
  idusuario INTEGER REFERENCES usuario(idusuario),
  tipo_comprobante VARCHAR(20),
  serie_comprobante VARCHAR(7),
  num_comprobante VARCHAR(10),
  fecha TIMESTAMP,
  impuesto DECIMAL(4,2),
  total DECIMAL(11,2),
  estado VARCHAR(20)
);

-- Crear tabla "detalle_venta"
CREATE TABLE IF NOT EXISTS detalle_venta (
  iddetalle_venta SERIAL PRIMARY KEY,
  idventa INTEGER REFERENCES venta(idventa),
  idarticulo INTEGER REFERENCES articulo(idarticulo),
  cantidad INTEGER,
  precio DECIMAL(11,2),
  descuento DECIMAL(11,2)
);

-- Crear tabla "ingreso"
CREATE TABLE IF NOT EXISTS ingreso (
  idingreso SERIAL PRIMARY KEY,
  idproveedor INTEGER REFERENCES persona(idpersona),
  idusuario INTEGER REFERENCES usuario(idusuario),
  tipo_comprobante VARCHAR(20),
  serie_comprobante VARCHAR(7),
  num_comprobante VARCHAR(10),
  fecha TIMESTAMP,
  impuesto DECIMAL(4,2),
  total DECIMAL(11,2),
  estado VARCHAR(20)
);

-- Crear tabla "detalle_ingreso"
CREATE TABLE IF NOT EXISTS detalle_ingreso (
  iddetalle_ingreso SERIAL PRIMARY KEY,
  idingreso INTEGER REFERENCES ingreso(idingreso),
  idarticulo INTEGER REFERENCES articulo(idarticulo),
  cantidad INTEGER,
  precio DECIMAL(11,2)
);

'''