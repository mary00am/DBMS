create schema if not exists lib;

create table if not exists lib.members(
memberId integer primary key,
name varchar(50),
contactNumber varchar(10));

create table if not exists lib.genres(
genreID integer primary key,
genreName varchar(50),
description varchar(200));

create table if not exists lib.publishers(
publisherID integer primary key,
publisherName varchar(50),
location varchar(100));

create table if not exists lib.books(
bookID integer primary key,
genreID integer references lib.genres(genreId),
title varchar(100),
author varchar(50),
publisher integer references lib.publishers(publisherID),
ISBNNumber varchar(20));


 
create table if not exists lib.borrowings(
borrowingId integer primary key,
bookID integer references lib.books(bookID),
memberID integer references lib.members(memberID),
borrowDate date,
returnDate date,
dueDate date);



