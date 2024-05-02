-- Inserts for lib.members table
INSERT INTO lib.members (memberId, name, contactNumber) VALUES
(1, 'John Doe', '1234567890'),
(2, 'Jane Smith', '9876543210'),
(3, 'Alice Johnson', '5551234567'),
(4, 'Bob Williams', '9876543210'),
(5, 'Emma Brown', '1234567890'),
(6, 'Michael Davis', '5559876543'),
(7, 'Sarah Wilson', '5553219876'),
(8, 'David Martinez', '1235556789'),
(9, 'Olivia Anderson', '9871234560'),
(10, 'James Taylor', '5557891234');

-- Inserts for lib.genres table
INSERT INTO lib.genres (genreID, genreName, description) VALUES
(1, 'Fiction', 'Books based on imaginative or fabricated stories'),
(2, 'Non-fiction', 'Books based on real events or facts'),
(3, 'Mystery', 'Books dealing with the solution of a crime or the unraveling of secrets'),
(4, 'Science Fiction', 'Books exploring imaginative concepts such as futuristic science and technology'),
(5, 'Fantasy', 'Books featuring magical or supernatural elements'),
(6, 'Romance', 'Books focusing on romantic love and relationships'),
(7, 'Thriller', 'Books that create excitement and suspense'),
(8, 'Horror', 'Books designed to scare or frighten the reader'),
(9, 'Biography', 'Books about the life of a real person written by someone else'),
(10, 'History', 'Books detailing past events and their significance');

-- Inserts for lib.publishers table
INSERT INTO lib.publishers (publisherID, publisherName, location) VALUES
(1, 'Penguin Random House', 'New York, USA'),
(2, 'HarperCollins Publishers', 'London, UK'),
(3, 'Simon & Schuster', 'New York, USA'),
(4, 'Hachette Livre', 'Paris, France'),
(5, 'Macmillan Publishers', 'London, UK'),
(6, 'Scholastic Corporation', 'New York, USA'),
(7, 'Pearson Education', 'London, UK'),
(8, 'Springer Nature', 'Berlin, Germany'),
(9, 'Wiley', 'Hoboken, USA'),
(10, 'Oxford University Press', 'Oxford, UK');

-- Inserts for lib.books table
INSERT INTO lib.books (bookID, genreID, title, author, publisher, ISBNNumber) VALUES
(1, 1, 'To Kill a Mockingbird', 'Harper Lee', 1, '9780061120084'),
(2, 2, 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 4, '9780062316097'),
(3, 3, 'The Da Vinci Code', 'Dan Brown', 2, '9780307474278'),
(4, 4, 'The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', 5, '9780345391803'),
(5, 5, 'Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 6, '9780747532743'),
(6, 6, 'Pride and Prejudice', 'Jane Austen', 7, '9780141439518'),
(7, 7, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 1, '9780307269751'),
(8, 8, 'Dracula', 'Bram Stoker', 3, '9780141439846'),
(9, 9, 'Steve Jobs', 'Walter Isaacson', 2, '9781451648539'),
(10, 10, 'A Brief History of Time', 'Stephen Hawking', 8, '9780553380163');

-- Inserts for lib.borrowings table
INSERT INTO lib.borrowings (borrowingId, bookID, memberID, borrowDate, returnDate, dueDate) VALUES
(1, 1, 1, '2024-03-01', '2024-03-15', '2024-04-01'),
(2, 2, 2, '2024-03-02', '2024-03-16', '2024-04-02'),
(3, 3, 3, '2024-03-03', '2024-03-17', '2024-04-03'),
(4, 4, 4, '2024-03-04', '2024-03-18', '2024-04-04'),
(5, 5, 5, '2024-03-05', '2024-03-19', '2024-04-05'),
(6, 6, 6, '2024-03-06', '2024-03-20', '2024-04-06'),
(7, 7, 7, '2024-03-07', '2024-03-21', '2024-04-07'),
(8, 8, 8, '2024-03-08', '2024-03-22', '2024-04-08'),
(9, 9, 9, '2024-03-09', '2024-03-23', '2024-04-09'),
(10, 10, 10, '2024-03-10', '2024-03-24', '2024-04-10');
