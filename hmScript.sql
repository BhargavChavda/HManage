-- Creating Database
CREATE SCHEMA IF NOT EXISTS hm;
USE hm;

-- Creating the table customer
DROP TABLE IF EXISTS customer;
CREATE TABLE customer(
cust_id int(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,
name char(20) DEFAULT NULL,
address char(100) DEFAULT NULL,
phone char(15) DEFAULT NULL,
email char(80) DEFAULT NULL,
idproof char(20) DEFAULT NULL,
idproofno char(25) DEFAULT NULL,
children int(2) DEFAULT NULL,
female int(2) DEFAULT NULL,
male int(2) DEFAULT NULL
);

-- Dumping values in customer
INSERT INTO customer(cust_id, name, address, phone, email, idproof, idproofno, children, female, male)
VALUES
(1,'Bhargav Chavda', 'Kalakruti Ave.','9424936806','bc05@outlook.com', 'Aadhar Card', '2325 2647 1238', 0,1,1);

-- Creating the table rooms
DROP TABLE IF EXISTS rooms;
CREATE TABLE IF NOT EXISTS rooms(
room_id int(3) PRIMARY KEY AUTO_INCREMENT,
roomno int(3) UNIQUE,
roomt char(50) DEFAULT NULL,
roomr float(10,2) DEFAULT NULL,
status char(20) DEFAULT NULL
);

-- Dumping values in rooms
INSERT INTO rooms(room_id,roomno,roomt,roomr,status)
VALUES
(1,101,'AC',2500.00,'Occupied'),
(2,102,'Non-AC',1000.00,'Available');

-- Creating the table bookings
DROP TABLE IF EXISTS bookings;
CREATE TABLE IF NOT EXISTS bookings(
    book_id int(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    room_id int(20),
    cust_id int(50),
    room_no char(3),
    checkin date,
    checkout date DEFAULT NULL
);

-- Dumping values in bookings
INSERT INTO bookings(book_id,room_id,cust_id,room_no,checkin,checkout)
VALUES
(1,1,1,'101','2022-10-18','2022-10-22');