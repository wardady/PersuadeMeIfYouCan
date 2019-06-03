create database persuade_me character set utf8mb4 collate utf8mb4_general_ci;
use persuade_me;
create user 'TretiakO'@'%' identified by 'qW12345678qW!';
grant all privileges on persuade_me.* to 'TretiakO'@'%' with grant option;
flush privileges;

