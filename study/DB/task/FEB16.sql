-- 문제 1
SELECT
	productCode, productName, MSRP
FROM products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products)
ORDER BY
	MSRP;
-- 문제 2
SELECT 
	customerNumber, customerName
FROM (
	SELECT *
    FROM customers
    INNER JOIN orders USING (customerNumber)
    WHERE DATE(orderDate)
    BETWEEN '2003-01-06' AND '2003-03-26') AS orderlist
ORDER BY
	customerNumber;
-- 문제 3
SELECT
	productCode, productName, productLine, MSRP
FROM 
	products
WHERE 
	productLine = 'Classic Cars' AND 
	MSRP = (SELECT MAX(MSRP) FROM products);
-- 문제 4
SELECT 
	customerNumber, customerName, country
FROM 
	customers
WHERE 
	country = (SELECT MAX(country) FROM customers)
ORDER BY 
	customerNumber;
-- 문제 5
SELECT
	customerNumber, customerName, order_count
FROM (
	SELECT customerNumber,customerName,COUNT(orderNumber) AS order_count
    FROM customers
    INNER JOIN orders USING (customerNumber)
    GROUP BY customerNumber
) AS orderList
ORDER BY 
	order_count DESC
LIMIT 1;
-- 문제 6 
SELECT DISTINCT
	productCode, productName
FROM (
	SELECT *
	FROM orderdetails
	INNER JOIN orders USING (orderNumber)
    WHERE YEAR(orderDate) = '2004') AS orderDate2004
INNER JOIN products USING (productCode)
ORDER BY 
	productCode DESC;