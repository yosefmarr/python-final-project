
SQL_QUERY_DELETE_RESET= '''
DELETE FROM detalle_ingreso;
DELETE FROM detalle_venta ;
DELETE FROM ingreso;
DELETE FROM venta;
DELETE FROM usuario;
DELETE FROM persona;
DELETE FROM articulo;
DELETE FROM categoria;
DELETE FROM rol;

ALTER SEQUENCE categoria_idcategoria_seq RESTART WITH 1;
ALTER SEQUENCE articulo_idarticulo_seq RESTART WITH 1;
ALTER SEQUENCE detalle_ingreso_iddetalle_ingreso_seq RESTART WITH 1;
ALTER SEQUENCE persona_idpersona_seq RESTART WITH 1;
ALTER SEQUENCE ingreso_idingreso_seq RESTART WITH 1;
ALTER SEQUENCE persona_idpersona_seq RESTART WITH 1;
ALTER SEQUENCE rol_idrol_seq RESTART WITH 1;
ALTER SEQUENCE venta_idventa_seq RESTART WITH 1;
ALTER SEQUENCE categoria_idcategoria_seq RESTART WITH 1;
'''