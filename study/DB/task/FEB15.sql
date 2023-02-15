-- 문제 1
SELECT
	employeeNumber,lastName,firstName,city
FROM employees
INNER JOIN offices
	ON employees.officeCode=offices.officeCode
ORDER BY
	employeeNumber;
    
-- 문제 2
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
-- 문제 3
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
-- 문제 4
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
-- 문제 5
-- 문제 2번은 LEFT JOIN 으로 customers 가 기준이 되어 offices 에 값이 없더라도
-- customers 의 항목이 모두 나오고 offices에 값이 없으면 NULL로 표시됩니다.
-- 문제 3번 RIGHT JOIN은 offices 기준으로 조회 되고 문제 4번은 INNER JOIN 으로
-- 두 테이블 모두 값이 있는 교집합만 조회가 됩니다.

-- 문제 6
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
UNION
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
-- 문제 7
SELECT
	orderdetails.orderNumber, orderDate
FROM orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
	orderNumber;
-- 문제 8
SELECT
	orderNumber, orderdetails.productCode, productName
FROM orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;
-- 문제 9
SELECT
	orders.orderNumber, orderdetails.productCode, orderDate, productName
FROM orders
INNER JOIN orderdetails ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;
