1) Make sure you have your database running.
2) execute the DDL SQL queries in ashfaq.sql file.
3) Execute the SQL DML SQL queries in ashfaq.data.sql file.
4) Before running app.py file, set the environmental variables as follows.
   1) DB_HOST=<url_where_database_is_running>
   2) DB_PORT=<database_port>
   3) DB_NAME=<database_name>
   4) DB_USER=<database_user>
   5) DB_PASSWORD=<database_password>
5) There are 3 methods GET, POST and DELETE. I used a software called postman to test my API endpoints. 
6) There are 5 endpoints for each of the 5 entities namely BOOKS, MEMBERS, PUBLISHERS,BORROWINGS, GENRES.
7) To access these entities, use GET request http://localhost:3000/<entity_name> or http://localhost:3000/<entity_name>/id.
8) For example http://localhost:3000/books, http://localhost:3000/members, http://localhost:3000/books/1.
9) To delete a data by id, send DELETE request to http://localhost:3000/<entity_name>/id. For example DELETE http://localhost:3000/books/1
10) To send a POST request, refer the DDL SQL file ashfaq.sql to note the fields and use the url as follows http://localhost:3000/<tbname>?<key=value> pairs.
11) For example http://localhost:3000/members?memberId=12&name=popey&contactNumber=978978.
