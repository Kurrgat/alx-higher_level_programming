### 1. How to create a new MySQL user:

To create a new MySQL user, you can use the `CREATE USER` statement. Here's a basic example:

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```

Make sure to replace 'username' and 'password' with the desired username and password for the new user.

### 2. How to manage privileges for a user to a database or table:

You can use the `GRANT` statement to assign privileges to a user. Here's an example:

```sql
GRANT SELECT, INSERT, UPDATE ON database_name.* TO 'username'@'localhost';
```

This grants the user 'username' the SELECT, INSERT, and UPDATE privileges on all tables in the 'database_name'.

### 3. What’s a PRIMARY KEY:

A PRIMARY KEY is a column or a set of columns in a table that uniquely identifies each row in that table. It must contain unique values and cannot have NULL values.

Example of creating a table with a PRIMARY KEY:

```sql
CREATE TABLE example_table (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

### 4. What’s a FOREIGN KEY:

A FOREIGN KEY is a column or a set of columns in a table that refers to the PRIMARY KEY of another table. It establishes a link between the two tables, enforcing referential integrity.

Example of creating a table with a FOREIGN KEY:

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

### 5. How to use NOT NULL and UNIQUE constraints:

You can use the `NOT NULL` constraint to ensure that a column cannot have NULL values, and the `UNIQUE` constraint to ensure that all values in a column are unique.

Example:

```sql
CREATE TABLE example_table (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);
```

### 6. How to retrieve data from multiple tables in one request:

You can use the `JOIN` clause to retrieve data from multiple tables based on a related column. For example:

```sql
SELECT orders.order_id, products.product_name
FROM orders
JOIN products ON orders.product_id = products.product_id;
```

### 7. What are subqueries:

A subquery is a query nested inside another query. It can be used to retrieve data that will be used by the main query.

Example:

```sql
SELECT name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');
```

### 8. What are JOIN and UNION:

- **JOIN:** The `JOIN` clause is used to combine rows from two or more tables based on a related column between them. There are different types of joins, such as INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.

Example:

```sql
SELECT customers.customer_id, orders.order_id
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;
```

- **UNION:** The `UNION` operator is used to combine the result sets of two or more SELECT statements into a single result set. It removes duplicate rows by default.

Example:

```sql
SELECT city FROM customers
UNION
SELECT city FROM suppliers;
```
