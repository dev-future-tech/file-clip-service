create role librarian with login password 'letmein';
create database library_db with owner librarian;

create table files(
    file_id bigint generated always as identity not null,
    file_name varchar(120),
    content TEXT,
    primary key (file_id)
);
