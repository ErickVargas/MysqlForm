create database form;
use form;
CREATE TABLE `form`.`contactos` (
  `id_contacto` INT NOT NULL AUTO_INCREMENT,
  `nombre` CHAR(20) NULL,
  `telefono` INT NULL,
  `email` VARCHAR(20) NULL,
  PRIMARY KEY (`id_contacto`));

      