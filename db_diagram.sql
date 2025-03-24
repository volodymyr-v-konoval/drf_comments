CREATE TABLE `follows` (
  `following_user_id` integer,
  `followed_user_id` integer,
  `created_at` timestamp
);

CREATE TABLE `users` (
  `id` integer PRIMARY KEY,
  `username` varchar(255),
  `role` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `posts` (
  `id` integer PRIMARY KEY,
  `title` varchar(255),
  `body` text COMMENT 'Content of the post',
  `user_id` integer NOT NULL,
  `status` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `auth_group` (
  `id` integer PRIMARY KEY NOT NULL,
  `name` character varying(150) UNIQUE NOT NULL
);

CREATE TABLE `auth_group_permissions` (
  `id` bigint PRIMARY KEY NOT NULL,
  `group_id` integer NOT NULL,
  `permission_id` integer NOT NULL
);

CREATE TABLE `auth_permission` (
  `id` integer PRIMARY KEY NOT NULL,
  `name` character varying(255) NOT NULL,
  `content_type_id` integer NOT NULL,
  `codename` character varying(100) NOT NULL
);

CREATE TABLE `auth_user` (
  `id` integer PRIMARY KEY NOT NULL,
  `password` character varying(128) NOT NULL,
  `last_login` timestamp,
  `is_superuser` boolean NOT NULL,
  `username` character varying(150) UNIQUE NOT NULL,
  `first_name` character varying(150) NOT NULL,
  `last_name` character varying(150) NOT NULL,
  `email` character varying(254) NOT NULL,
  `is_staff` boolean NOT NULL,
  `is_active` boolean NOT NULL,
  `date_joined` timestamp NOT NULL
);

CREATE TABLE `auth_user_groups` (
  `id` bigint PRIMARY KEY NOT NULL,
  `user_id` integer NOT NULL,
  `group_id` integer NOT NULL
);

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint PRIMARY KEY NOT NULL,
  `user_id` integer NOT NULL,
  `permission_id` integer NOT NULL
);

CREATE TABLE `authtoken_token` (
  `key` character varying(40) PRIMARY KEY NOT NULL,
  `created` timestamp NOT NULL,
  `user_id` integer UNIQUE NOT NULL
);

CREATE TABLE `blog_comment` (
  `id` bigint PRIMARY KEY NOT NULL,
  `email` character varying(254) NOT NULL,
  `homepage` character varying(200) NOT NULL,
  `text` character varying(2500) NOT NULL,
  `created` timestamp NOT NULL,
  `updated` timestamp NOT NULL,
  `parent_id` bigint,
  `username_id` integer NOT NULL
);

CREATE TABLE `captcha_captchastore` (
  `id` integer PRIMARY KEY NOT NULL,
  `challenge` character varying(32) NOT NULL,
  `response` character varying(32) NOT NULL,
  `hashkey` character varying(40) UNIQUE NOT NULL,
  `expiration` timestamp NOT NULL
);

CREATE TABLE `django_admin_log` (
  `id` integer PRIMARY KEY NOT NULL,
  `action_time` timestamp NOT NULL,
  `object_id` text,
  `object_repr` character varying(200) NOT NULL,
  `action_flag` smallint NOT NULL,
  `change_message` text NOT NULL,
  `content_type_id` integer,
  `user_id` integer NOT NULL
);

CREATE TABLE `django_content_type` (
  `id` integer PRIMARY KEY NOT NULL,
  `app_label` character varying(100) NOT NULL,
  `model` character varying(100) NOT NULL
);

CREATE TABLE `django_migrations` (
  `id` bigint PRIMARY KEY NOT NULL,
  `app` character varying(255) NOT NULL,
  `name` character varying(255) NOT NULL,
  `applied` timestamp NOT NULL
);

CREATE TABLE `django_session` (
  `session_key` character varying(40) PRIMARY KEY NOT NULL,
  `session_data` text NOT NULL,
  `expire_date` timestamp NOT NULL
);

CREATE INDEX `auth_group_name_a6ea08ec_like` ON `auth_group` (`name`) USING BTREE;

CREATE UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` ON `auth_group_permissions` (`group_id`, `permission_id`);

CREATE INDEX `auth_group_permissions_group_id_b120cbf9` ON `auth_group_permissions` (`group_id`) USING BTREE;

CREATE INDEX `auth_group_permissions_permission_id_84c5c92e` ON `auth_group_permissions` (`permission_id`) USING BTREE;

CREATE UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` ON `auth_permission` (`content_type_id`, `codename`);

CREATE INDEX `auth_permission_content_type_id_2f476e4b` ON `auth_permission` (`content_type_id`) USING BTREE;

CREATE INDEX `auth_user_username_6821ab7c_like` ON `auth_user` (`username`) USING BTREE;

CREATE UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq` ON `auth_user_groups` (`user_id`, `group_id`);

CREATE INDEX `auth_user_groups_group_id_97559544` ON `auth_user_groups` (`group_id`) USING BTREE;

CREATE INDEX `auth_user_groups_user_id_6a12ed8b` ON `auth_user_groups` (`user_id`) USING BTREE;

CREATE UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` ON `auth_user_user_permissions` (`user_id`, `permission_id`);

CREATE INDEX `auth_user_user_permissions_permission_id_1fbb5f2c` ON `auth_user_user_permissions` (`permission_id`) USING BTREE;

CREATE INDEX `auth_user_user_permissions_user_id_a95ead1b` ON `auth_user_user_permissions` (`user_id`) USING BTREE;

CREATE INDEX `authtoken_token_key_10f0b77e_like` ON `authtoken_token` (`key`) USING BTREE;

CREATE INDEX `blog_commen_created_79f39f_idx` ON `blog_comment` (`created`) USING BTREE;

CREATE INDEX `blog_comment_parent_id_f2a027bb` ON `blog_comment` (`parent_id`) USING BTREE;

CREATE INDEX `blog_comment_username_id_38b7d8c7` ON `blog_comment` (`username_id`) USING BTREE;

CREATE INDEX `captcha_captchastore_hashkey_cbe8d15a_like` ON `captcha_captchastore` (`hashkey`) USING BTREE;

CREATE INDEX `django_admin_log_content_type_id_c4bce8eb` ON `django_admin_log` (`content_type_id`) USING BTREE;

CREATE INDEX `django_admin_log_user_id_c564eba6` ON `django_admin_log` (`user_id`) USING BTREE;

CREATE UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` ON `django_content_type` (`app_label`, `model`);

CREATE INDEX `django_session_expire_date_a5c62663` ON `django_session` (`expire_date`) USING BTREE;

CREATE INDEX `django_session_session_key_c0390e0f_like` ON `django_session` (`session_key`) USING BTREE;

ALTER TABLE `posts` ADD CONSTRAINT `user_posts` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `follows` ADD FOREIGN KEY (`following_user_id`) REFERENCES `users` (`id`);

ALTER TABLE `follows` ADD FOREIGN KEY (`followed_user_id`) REFERENCES `users` (`id`);

ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

ALTER TABLE `auth_permission` ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

ALTER TABLE `auth_user_groups` ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

ALTER TABLE `auth_user_groups` ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `authtoken_token` ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `blog_comment` ADD CONSTRAINT `blog_comment_parent_id_f2a027bb_fk_blog_comment_id` FOREIGN KEY (`parent_id`) REFERENCES `blog_comment` (`id`);

ALTER TABLE `blog_comment` ADD CONSTRAINT `blog_comment_username_id_38b7d8c7_fk_auth_user_id` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `django_admin_log` ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

ALTER TABLE `django_admin_log` ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
