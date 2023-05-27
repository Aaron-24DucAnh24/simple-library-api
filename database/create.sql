create table user (
    userid integer primary key,
    username text not null,
    email text unique not null,
    password text not null,
    role text default "reader"
);

create table books (
    bookid integer primary key,
    bookname text unique,
    author text,
    year integer,
    total_number integer not null check (total_number > 0),
    available_number integer check (available_number < total_number or available_number = total_number)
);

create table borrows (
    bookid integer,
    userid integer,
    foreign key (userid) references users(userid),
    foreign key (bookid) references books(bookid),
    primary key (bookid, userid)
);
