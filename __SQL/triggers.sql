-----------------------------------------------------------------------------------------------------
-- FUNCION PARA GENERAR EL CORREO
CREATE OR REPLACE FUNCTION fn_generar_correo(tipo VARCHAR)
RETURNS TRIGGER AS $$
DECLARE
    nuevo_correo VARCHAR(150);
    contador INT;
BEGIN
    nuevo_correo := LOWER(SPLIT_PART(NEW.nombres, ' ', 1) || '.' || SPLIT_PART(NEW.apellidos, ' ', 1));

    SELECT COUNT(*) INTO contador
    FROM Estudiante
    WHERE correo = nuevo_correo||'@unah.hn';

    IF contador > 0 THEN
        nuevo_correo := nuevo_correo || contador;
    END IF;

    NEW.correo := nuevo_correo || '@unah.hn';

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- TRIGGER PARA GENERAR EL CORREO
CREATE TRIGGER tg_generar_correo
BEFORE INSERT ON Estudiante
FOR EACH ROW
EXECUTE FUNCTION fn_generar_correo();
---------------------------------------------------------------------------------------------------------------


-- SECUENCIA DEL NUMERO DE CUENTA
CREATE SEQUENCE sq_numero_cuenta START 1 INCREMENT 1;

-- Crear la función para generar el número de cuenta
CREATE OR REPLACE FUNCTION fg_generar_numero_cuenta()
RETURNS TRIGGER AS $$
DECLARE
    numero_cuenta VARCHAR(11);
    anio VARCHAR(4) := '2024';
BEGIN

    numero_cuenta := anio || LPAD(CAST(NEXTVAL('sq_numero_cuenta') AS TEXT), 6, '0');

    NEW.numero_cuenta := numero_cuenta;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER tg_generar_numero_cuenta
BEFORE INSERT ON Estudiante
FOR EACH ROW
EXECUTE FUNCTION fg_generar_numero_cuenta();

'2018' || '1' || LPAD(CAST(NEXTVAL('numero_cuenta_secuencia') AS TEXT), 6, '0')