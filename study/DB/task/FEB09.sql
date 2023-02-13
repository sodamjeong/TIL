-- 문제 1
SELECT 
	*
FROM 
	employees;
    
-- 문제 2
SELECT
	customerNumber, customerName, phone
From
    customers;
-- 문제 3
SELECT
    firstName, lastName, email
FROM
    employees
ORDER BY
    firstName ASC;
-- 문제 4
SELECT
    firstName AS '이름', lastName AS '성', email AS '이메일'
FROM
    employees
ORDER BY
    이름 ASC;
-- 문제 5
SELECT
    employeeNumber, lastName, firstName, officeCode, jobTitle
FROM
    employees
ORDER BY
    jobTitle DESC, officeCode DESC;
-- 문제 6
SELECT
    *
FROM
    orderdetails
ORDER BY
    quantityOrdered ASC, priceEach ASC;
-- 문제 7
SELECT
    customerNumber, country, contactFirstName
FROM
    customers
ORDER BY
    country ASC, contactFirstName DESC;
-- 문제 8
SELECT
    productCode, quantityInStock, buyPrice, quantityInStock*buyPrice
FROM
    products
ORDER BY
    quantityInStock * buyPrice DESC;