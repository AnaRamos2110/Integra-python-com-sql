CREATE TABLE `loja`.`clientes` (
  `id_clientes` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `cidade` VARCHAR(45) NULL,
  `estado` VARCHAR(45) NULL,
  PRIMARY KEY (`id_clientes`));


CREATE TABLE `loja`.`funcionarios` (
  `id_funcionarios` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `idade` INT(3) NULL,
  `setor` VARCHAR(45) NULL,
  PRIMARY KEY (`id_funcionarios`));


CREATE TABLE `loja`.`produtos` (
  `id_produtos` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(45) NULL,
  `valor` FLOAT NULL,
  PRIMARY KEY (`id_produtos`));

CREATE TABLE `loja`.`usuarios` (
  `id_usuarios` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `senha` VARCHAR(25) NULL,
  PRIMARY KEY (`id_usuarios`));

CREATE TABLE `loja`.`vendas` (
    `id_vendas` INT AUTO_INCREMENT PRIMARY KEY,
    `id_clientes` INT NOT NULL,
    `id_funcionarios` INT NOT NULL,
    `id_produtos` INT NOT NULL,
    `quantidade` INT NOT NULL,
    `valor_unitario` DECIMAL(10,2) NOT NULL,
    `valor_total` DECIMAL(10,2) GENERATED ALWAYS AS (quantidade * valor_unitario) STORED,
    `data_venda` DATETIME DEFAULT CURRENT_TIMESTAMP);

