
DROP DATABASE db_mathquiz;
CREATE DATABASE db_mathquiz;
USE db_mathquiz;

CREATE TABLE Avatar (
	avatar_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	avatar_blob BLOB
);

CREATE TABLE Player (
	player_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	username VARCHAR(24),
	email VARCHAR(64),
	password VARCHAR(24),
	credits INT DEFAULT 0,
	level INT DEFAULT 1,
	register_date DATE DEFAULT CURDATE(),
	active_avatar_id INT,
	freezetime INT,
	doublepoint INT,
	skipround INT,
	FOREIGN KEY (active_avatar_id) REFERENCES Avatar (avatar_id)
);

CREATE TABLE Game (
	game_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	player_id INT,
	score INT DEFAULT 0,
	start_time DATETIME,
	end_time DATETIME,
	questions_answered INT DEFAULT 0,
	FOREIGN KEY (player_id) REFERENCES Player (player_id)
);

CREATE TABLE Owned_Avatars (
	player_id INT,
	avatar_id INT,
	FOREIGN KEY (player_id) REFERENCES Player (player_id),
	FOREIGN KEY (avatar_id) REFERENCES Avatar (avatar_id)
);
