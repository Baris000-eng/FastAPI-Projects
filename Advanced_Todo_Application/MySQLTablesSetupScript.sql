DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(200) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `initial_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `hashed_pwd` varchar(200) DEFAULT NULL,
  `is_active` int(1) DEFAULT NULL,
  `user_role` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `todos`;

CREATE TABLE `todos` (
  `todo_id` int(11) NOT NULL AUTO_INCREMENT,
  `todo_title` varchar(200) DEFAULT NULL,
  `todo_description` varchar(200) DEFAULT NULL,
  `todo_priority` int(1) DEFAULT NULL,
  `todo_is_complete` int(1) DEFAULT NULL,
  `owner_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`owner_id`) REFERENCES users(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;