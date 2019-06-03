CREATE TABLE user(id_tl bigint PRIMARY KEY, username varchar(255), sex BOOLEAN, age int);

CREATE TABLE category(name varchar(255) PRIMARY KEY, counter int);

CREATE TABLE question(id int PRIMARY KEY AUTO_INCREMENT, name varchar(255),
 category_name varchar(255), FOREIGN KEY(category_name) REFERENCES category(name));


CREATE TABLE response(id int PRIMARY KEY AUTO_INCREMENT,
  question_id int, FOREIGN KEY (question_id) REFERENCES question(id),
  yes_id bigint, FOREIGN KEY (yes_id) REFERENCES user(id_tl),
  no_id bigint, FOREIGN KEY (no_id) REFERENCES user(id_tl));

CREATE TABLE storage(id int PRIMARY KEY AUTO_INCREMENT,
  question_id int, FOREIGN KEY (question_id) REFERENCES question(id),
  yes_id bigint, FOREIGN KEY (yes_id) REFERENCES user(id_tl),
  no_id bigint, FOREIGN KEY (no_id) REFERENCES user(id_tl));
