-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-12-2025 a las 17:35:36
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `chuckydb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add curso', 7, 'add_curso'),
(26, 'Can change curso', 7, 'change_curso'),
(27, 'Can delete curso', 7, 'delete_curso'),
(28, 'Can view curso', 7, 'view_curso'),
(29, 'Can add alumno', 8, 'add_alumno'),
(30, 'Can change alumno', 8, 'change_alumno'),
(31, 'Can delete alumno', 8, 'delete_alumno'),
(32, 'Can view alumno', 8, 'view_alumno');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-11-30 03:47:13.510494', '1', 'admin - admin@ad.cl', 2, '[{\"changed\": {\"fields\": [\"Rol\"]}}]', 6, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(8, 'gestorCursos', 'alumno'),
(7, 'gestorCursos', 'curso'),
(6, 'gestorUser', 'user'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-11-30 03:18:24.563698'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-11-30 03:18:24.634700'),
(3, 'auth', '0001_initial', '2025-11-30 03:18:24.880328'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-11-30 03:18:24.932666'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-11-30 03:18:24.938823'),
(6, 'auth', '0004_alter_user_username_opts', '2025-11-30 03:18:24.945764'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-11-30 03:18:24.951749'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-11-30 03:18:24.954196'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-11-30 03:18:24.962877'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-11-30 03:18:24.970866'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-11-30 03:18:24.978503'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-11-30 03:18:24.992511'),
(13, 'auth', '0011_update_proxy_permissions', '2025-11-30 03:18:25.001914'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-11-30 03:18:25.009916'),
(15, 'gestorUser', '0001_initial', '2025-11-30 03:18:25.287769'),
(16, 'admin', '0001_initial', '2025-11-30 03:18:25.405967'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-11-30 03:18:25.415128'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-11-30 03:18:25.425959'),
(19, 'gestorCursos', '0001_initial', '2025-11-30 03:18:25.616037'),
(20, 'gestorCursos', '0002_alumno_creador_alumno_curso_creador_curso_and_more', '2025-11-30 03:18:25.784163'),
(21, 'gestorCursos', '0003_alter_alumno_options', '2025-11-30 03:18:25.795178'),
(22, 'gestorUser', '0002_alter_user_rol', '2025-11-30 03:18:25.807454'),
(23, 'sessions', '0001_initial', '2025-11-30 03:18:25.864566');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('o6i4h2pk6q56ld0w2jx486gnlo41q3a4', '.eJxVjEEOwiAQAP_C2ZAV2AoevfcNBNhFqgaS0p6MfzckPeh1ZjJv4cO-Fb93Xv1C4iqUOP2yGNKT6xD0CPXeZGp1W5coRyIP2-XciF-3o_0blNDL2CJGsiqzypAt8oVd5jOBQhchkU08gTJIDiGqKRudIpHWGLI1SWsQny_1nzgx:1vQ5VG:rumwYO_HTsBRNuxHCKTgbVsJQH6-bZk7BY9I0SlT1Ho', '2025-12-15 15:07:50.455513'),
('qph2pbdv7esa22tf0hyp3gp1d0afg002', '.eJxVjEEOwiAQRe_C2pAOUGBcuvcMZBhAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hSuIsQJx-t0j8yG0H6U7tNkue27pMUe6KPGiX1znl5-Vw_w4q9fqtMWpPbow-s3WYuBREq0wkZdGCyuDcoIExudF4KjZpUzQYxTAQaCri_QHcsDd-:1vQ6KR:egMfaF1-vCKgzQESZia34hU4aNH5WPq1ItkoVQvPZ9U', '2025-12-15 16:00:43.245064');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestorcursos_alumno`
--

CREATE TABLE `gestorcursos_alumno` (
  `id` bigint(20) NOT NULL,
  `rut` varchar(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `creador_alumno_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `gestorcursos_alumno`
--

INSERT INTO `gestorcursos_alumno` (`id`, `rut`, `nombre`, `apellido`, `fecha_nacimiento`, `creador_alumno_id`) VALUES
(1, '12842932-4', 'José', 'Valdés', '2000-09-04', 1),
(2, '12312453-6', 'Cristian', 'Cortés', '2000-06-08', 1),
(3, '23534123-5', 'Julio', 'Gonzalez', '2006-05-10', 2),
(4, '12346743-k', 'andres', 'rojas', '2006-05-09', 4),
(5, '12634723-k', 'Pancho', 'Valenzuela', '1997-01-18', 4),
(6, '24636356-k', 'Pablo', 'Valenzuela', '1988-07-07', 4),
(7, '12456635-6', 'kratos', 'John', '1993-06-11', 2),
(8, '34647124-5', 'Javier', 'Rios', '2025-12-13', 4),
(9, '12452356-5', 'Daniel', 'Ortiz', '2025-12-12', 4),
(10, '12748347-4', 'Valentina', 'Gomez', '2025-11-05', 2),
(11, '12435747-3', 'Adrian', 'Segura', '2025-12-13', 2),
(12, '12547346-3', 'Felipe', 'Cruces', '2025-12-20', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestorcursos_alumno_cursos_tomado`
--

CREATE TABLE `gestorcursos_alumno_cursos_tomado` (
  `id` bigint(20) NOT NULL,
  `alumno_id` bigint(20) NOT NULL,
  `curso_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `gestorcursos_alumno_cursos_tomado`
--

INSERT INTO `gestorcursos_alumno_cursos_tomado` (`id`, `alumno_id`, `curso_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1),
(4, 2, 2),
(6, 2, 3),
(5, 3, 1),
(7, 4, 1),
(8, 4, 5),
(9, 4, 6),
(10, 5, 1),
(11, 5, 2),
(12, 5, 3),
(13, 5, 4),
(14, 5, 5),
(15, 5, 6),
(16, 6, 1),
(17, 6, 5),
(18, 6, 6),
(19, 7, 1),
(20, 7, 2),
(21, 7, 3),
(22, 7, 4),
(23, 7, 5),
(24, 7, 6),
(25, 8, 6),
(26, 9, 5),
(27, 10, 6),
(28, 11, 1),
(29, 12, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestorcursos_curso`
--

CREATE TABLE `gestorcursos_curso` (
  `id` bigint(20) NOT NULL,
  `codigo` varchar(60) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `creador_curso_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `gestorcursos_curso`
--

INSERT INTO `gestorcursos_curso` (`id`, `codigo`, `nombre`, `descripcion`, `creador_curso_id`) VALUES
(1, 'JV-DX-T4356', 'Programación orientada a objeto', 'Programación orientado a objeto en python y consumo de API', 1),
(2, 'KS-TD-T2314', 'Front End', 'Diseño de Front End con herramientas como Bootstrap y otros', 1),
(3, 'FG-ER-T945', 'Matematicas', 'Despejar X de la ecuación y creación de formulas', 3),
(4, 'JD-GD-T342', 'Innovación y emprendimiento I', 'Presentación de un proyecto amigable con el medio ambiente.', 3),
(5, 'FK-WR-T3952', 'Ingles', 'Presentación de los principales tiempos verbales en ingles', 3),
(6, 'DF-GE-T4952', 'Back End', 'Presentación del framework Django en combinación con XAMPP y herramientas como Bootstrap y paneles administrativos', 3),
(7, 'AT-UJ-T3245', 'Desarrollo de videojuegos', 'Durante este curso se enseñara el desarrollo de videojuegos utilizando la herramienta de Unity', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestoruser_user`
--

CREATE TABLE `gestoruser_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `rol` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `gestoruser_user`
--

INSERT INTO `gestoruser_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `rol`) VALUES
(1, 'pbkdf2_sha256$720000$n47AO38pe2DvLHublTOl7z$AcR0IZODLwNVGstiIFnvIGqKjVat5VoZLZyQuWHFmEU=', '2025-12-01 16:00:43.240829', 1, 'admin', '', '', 'admin@ad.cl', 1, 1, '2025-11-30 03:20:44.000000', 'Administrador'),
(2, 'pbkdf2_sha256$720000$Cwn95qvTqFriPJl8w20x92$XHbGAGEJtbYQwIyXbe3cAV8Lyj3UpFOShPmQOv3G/H0=', '2025-12-01 15:07:50.453260', 0, 'docente', '', '', 'docente@doc.cl', 0, 1, '2025-11-30 04:25:15.641235', 'Docente'),
(3, 'pbkdf2_sha256$720000$3wYEZdbEbBOo3zymNDu69U$5/iSZ5wz8uyVQYHvoMI1dnDIRR1k+n1OH2v4/j1gUEk=', '2025-11-30 05:33:17.139589', 1, 'pepe', '', '', 'pepe@pe.cl', 1, 1, '2025-11-30 04:31:37.716999', 'Administrador'),
(4, 'pbkdf2_sha256$720000$APdTpj0gXoBlXjC3BBJHFH$HhYC+Zvy1Lgtk0bjYe+JOOd/KPmHZNt0ts8NQFSgfQc=', '2025-12-01 15:02:39.354578', 0, 'Cristofher', '', '', 'crstofher@cri.cl', 0, 1, '2025-11-30 04:40:47.883236', 'Docente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestoruser_user_groups`
--

CREATE TABLE `gestoruser_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestoruser_user_user_permissions`
--

CREATE TABLE `gestoruser_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_gestorUser_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `gestorcursos_alumno`
--
ALTER TABLE `gestorcursos_alumno`
  ADD PRIMARY KEY (`id`),
  ADD KEY `gestorCursos_alumno_creador_alumno_id_fa71847c_fk_gestorUse` (`creador_alumno_id`);

--
-- Indices de la tabla `gestorcursos_alumno_cursos_tomado`
--
ALTER TABLE `gestorcursos_alumno_cursos_tomado`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `gestorCursos_alumno_curs_alumno_id_curso_id_91d92801_uniq` (`alumno_id`,`curso_id`),
  ADD KEY `gestorCursos_alumno__curso_id_6d86822a_fk_gestorCur` (`curso_id`);

--
-- Indices de la tabla `gestorcursos_curso`
--
ALTER TABLE `gestorcursos_curso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `gestorCursos_curso_creador_curso_id_88c9d59e_fk_gestorUse` (`creador_curso_id`);

--
-- Indices de la tabla `gestoruser_user`
--
ALTER TABLE `gestoruser_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `gestoruser_user_groups`
--
ALTER TABLE `gestoruser_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `gestorUser_user_groups_user_id_group_id_eff9fe8b_uniq` (`user_id`,`group_id`),
  ADD KEY `gestorUser_user_groups_group_id_d220a25d_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `gestoruser_user_user_permissions`
--
ALTER TABLE `gestoruser_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `gestorUser_user_user_per_user_id_permission_id_ab8fd325_uniq` (`user_id`,`permission_id`),
  ADD KEY `gestorUser_user_user_permission_id_03839fe0_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `gestorcursos_alumno`
--
ALTER TABLE `gestorcursos_alumno`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `gestorcursos_alumno_cursos_tomado`
--
ALTER TABLE `gestorcursos_alumno_cursos_tomado`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `gestorcursos_curso`
--
ALTER TABLE `gestorcursos_curso`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `gestoruser_user`
--
ALTER TABLE `gestoruser_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `gestoruser_user_groups`
--
ALTER TABLE `gestoruser_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `gestoruser_user_user_permissions`
--
ALTER TABLE `gestoruser_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_gestorUser_user_id` FOREIGN KEY (`user_id`) REFERENCES `gestoruser_user` (`id`);

--
-- Filtros para la tabla `gestorcursos_alumno`
--
ALTER TABLE `gestorcursos_alumno`
  ADD CONSTRAINT `gestorCursos_alumno_creador_alumno_id_fa71847c_fk_gestorUse` FOREIGN KEY (`creador_alumno_id`) REFERENCES `gestoruser_user` (`id`);

--
-- Filtros para la tabla `gestorcursos_alumno_cursos_tomado`
--
ALTER TABLE `gestorcursos_alumno_cursos_tomado`
  ADD CONSTRAINT `gestorCursos_alumno__alumno_id_07329b43_fk_gestorCur` FOREIGN KEY (`alumno_id`) REFERENCES `gestorcursos_alumno` (`id`),
  ADD CONSTRAINT `gestorCursos_alumno__curso_id_6d86822a_fk_gestorCur` FOREIGN KEY (`curso_id`) REFERENCES `gestorcursos_curso` (`id`);

--
-- Filtros para la tabla `gestorcursos_curso`
--
ALTER TABLE `gestorcursos_curso`
  ADD CONSTRAINT `gestorCursos_curso_creador_curso_id_88c9d59e_fk_gestorUse` FOREIGN KEY (`creador_curso_id`) REFERENCES `gestoruser_user` (`id`);

--
-- Filtros para la tabla `gestoruser_user_groups`
--
ALTER TABLE `gestoruser_user_groups`
  ADD CONSTRAINT `gestorUser_user_groups_group_id_d220a25d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `gestorUser_user_groups_user_id_fe6ab37c_fk_gestorUser_user_id` FOREIGN KEY (`user_id`) REFERENCES `gestoruser_user` (`id`);

--
-- Filtros para la tabla `gestoruser_user_user_permissions`
--
ALTER TABLE `gestoruser_user_user_permissions`
  ADD CONSTRAINT `gestorUser_user_user_permission_id_03839fe0_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `gestorUser_user_user_user_id_5d54e3bd_fk_gestorUse` FOREIGN KEY (`user_id`) REFERENCES `gestoruser_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
