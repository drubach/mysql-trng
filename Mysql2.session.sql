use Chinook;

-- show tables;

-- SELECT FirstName, LastName FROM Customer;

SELECT FirstName, LastName, InvoiceDate, Total
FROM Customer
LEFT JOIN Invoice ON Customer.CustomerID = Invoice.CustomerID
ORDER BY Total DESC, InvoiceDate DESC
LIMIT 10;

