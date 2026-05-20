-- Create the database
CREATE DATABASE IF NOT EXISTS LittleLemonDB;
USE LittleLemonDB;

-- Create the Customers table
CREATE TABLE Customers (
    CustomerID INT NOT NULL PRIMARY KEY,
    FullName VARCHAR(255),
    City VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(45),
    CountryCode VARCHAR(10)
);

-- Create the Menu table
CREATE TABLE Menu (
    MenuID INT NOT NULL PRIMARY KEY,
    CourseName VARCHAR(100),
    CuisineName VARCHAR(100),
    StarterName VARCHAR(100),
    DesertName VARCHAR(100),
    Drink VARCHAR(100),
    Sides VARCHAR(100)
);

-- Create the Bookings table
CREATE TABLE Bookings (
    BookingID INT NOT NULL PRIMARY KEY,
    BookingDate DATE,
    TableNumber INT,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create the Orders table
CREATE TABLE Orders (
    OrderID INT NOT NULL PRIMARY KEY,
    OrderDate DATE,
    DeliveryDate DATE,
    Cost DECIMAL(10,2),
    Sales DECIMAL(10,2),
    Quantity INT,
    Discount DECIMAL(10,2),
    DeliveryCost DECIMAL(10,2),
    CustomerID INT,
    MenuID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (MenuID) REFERENCES Menu(MenuID)
);