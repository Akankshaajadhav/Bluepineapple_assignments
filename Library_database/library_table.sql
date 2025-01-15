drop table if exists borrowed_book;
drop table if exists book;

create table book(
  id serial primary key,
  name varchar(20) not null,
  author varchar(30) not null,
  price int not null,
  allocated BOOLEAN DEFAULT FALSE
);

CREATE TABLE borrowed_book(
    book_id INTEGER REFERENCES book(id),
    user_id TEXT NOT NULL,
    PRIMARY KEY (book_id, user_id)
);





