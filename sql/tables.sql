CREATE TABLE user(id int PRIMARY KEY AUTO_INCREMENT, id_tl long, username varchar(255), sex BOOLEAN, age int)

CREATE TABLE question(id int PRIMARY KEY AUTO_INCREMENT, name varchar(255), category varchar(255))

CREATE TABLE response(id int PRIMARY KEY AUTO_INCREMENT,
  question_id int, FOREIGN KEY (question_id) REFERENCES question(id) not null,
  yes_id int, FOREIGN KEY (yes_id) REFERENCES user(id),
  no_id int, FOREIGN KEY (yes_id) REFERENCES user(id))

CREATE TABLE storage(id int PRIMARY KEY AUTO_INCREMENT,
  question_id int, FOREIGN KEY (question_id) REFERENCES question(id) not null,
  yes_id int, FOREIGN KEY (yes_id) REFERENCES user(id) not null,
  no_id int, FOREIGN KEY (yes_id) REFERENCES user(id) not null)