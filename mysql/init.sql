CREATE TABLE `organisational_unit` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `parent_id` smallint(5) unsigned DEFAULT NULL,
  `code` varchar(10) NOT NULL,
  `abbreviation` varchar(20) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `payment_methods` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_name` (`name`),
  UNIQUE KEY `unique_code` (`code`),
  CONSTRAINT `FK_organisational_unit_parent_id` FOREIGN KEY (`parent_id`) REFERENCES `organisational_unit` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `organisational_unit` (`id`, `parent_id`, `code`, `abbreviation`, `name`) VALUES
    (1, NULL, 'D21', 'DHC', 'DH Core'),
    (2, NULL, 'D22', 'HRA', 'Health Research Authority'),
    (3, NULL, 'D23', 'HFE', 'Human Fertilisation & Embryology'),
    (4, NULL, 'D24', 'MHPRA', 'Medicines and Healthcare Products Regulatory Agency');

CREATE TABLE `profession` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `parent_id` smallint(5) unsigned DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_profession_profession` (`parent_id`),
  CONSTRAINT `FK_profession_profession` FOREIGN KEY (`parent_id`) REFERENCES `profession` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `profession` (`parent_id`,`name`) VALUES
(NULL,"Analysis"),
(NULL,"Commercial"),
(NULL,"Communications"),
(NULL,"Corporate finance"),
(NULL,"Digital"),
(NULL,"Finance"),
(NULL,"Fraud, error, debt and grants"),
(NULL,"Human resources"),
(NULL,"Internal audit"),
(NULL,"Legal");

CREATE TABLE IF NOT EXISTS `grade` (
  `id` smallint(5) NOT NULL AUTO_INCREMENT,
  `organisation_id` smallint(5) DEFAULT NULL,
  `code` char(20) NOT NULL UNIQUE,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO grade (code, name, organisation_id) VALUES
	('AA', 'Administrative assistant', null),
	('AO', 'Administrative officer', null),
    ('EO', 'Executive officer', null),
    ('G6', 'Grade 6', null),
    ('G7', 'Grade 7', null),
    ('HEO','Higher executive officer', null),
    ('SEO','Senior executive officer', null),
    ('PB1', 'SCS: deputy director', null),
    ('PB2', 'SCS: director', null),
    ('PB3', 'SCS: director General', null),
	('PS',  'SCS: permanent Secretary', null);