
SQL_QUERY_DELETE_RESET= '''
DELETE FROM detalle_ingreso;
commit;
DELETE FROM detalle_venta ;
commit;
DELETE FROM ingreso;
commit;
DELETE FROM persona ;
commit;
DELETE FROM usuario;
commit;
DELETE FROM venta;
commit;
DELETE FROM articulo;
commit;
DELETE FROM categoria;
commit;
DELETE FROM rol;
commit;

ALTER SEQUENCE categoria_idcategoria_seq RESTART WITH 1;
ALTER SEQUENCE articulo_articulo_seq RESTART WITH 1;
ALTER SEQUENCE detalle_ingreso_iddetalle_ingreso_seq RESTART WITH 1;
ALTER SEQUENCE persona_idpersona_seq RESTART WITH 1;
ALTER SEQUENCE ingreso_idingreso_seq RESTART WITH 1;
ALTER SEQUENCE persona_idpersona_seq RESTART WITH 1;
ALTER SEQUENCE rol_idrol_seq RESTART WITH 1;
ALTER SEQUENCE venta_idventa_seq RESTART WITH 1;
ALTER SEQUENCE usuario_idcategoria_seq RESTART WITH 1;
'''