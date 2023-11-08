# E-Market API Documentation

This document provides information about the endpoints available in my E-Market API.

## Table of Contents

1. [Orders](#orders)
2. [Products](#products)
3. [Users](#users)

## Orders

### List Orders

- **Endpoint**: `GET /orders/`
- **Description**: Retrieve a list of all orders.
- **Parameters**: None
- **Response**: An array of order objects, each containing order details such as order ID, customer information, and order items.

### Get Order Details

- **Endpoint**: `GET /orders/{id}/`
- **Description**: Retrieve details of a specific order by its unique ID.
- **Parameters**:
  - `{id}` (Path Parameter): The unique identifier of the order.
- **Response**: Detailed information about the specified order, including order ID, customer information, and order items.

### Create a New Order

- **Endpoint**: `POST /orders/`
- **Description**: Create a new order.
- **Request Body**: JSON object containing order details, including customer information and order items.
- **Response**: The newly created order with a unique ID.

### Delete an Order

- **Endpoint**: `DELETE /orders/{id}/`
- **Description**: Delete a specific order by its unique ID.
- **Parameters**:
  - `{id}` (Path Parameter): The unique identifier of the order.
- **Response**: Confirmation of the deletion or an error message if the order does not exist.

## Products

### List Products

- **Endpoint**: `GET /product/`
- **Description**: Retrieve a list of all products.
- **Parameters**: None
- **Response**: An array of product objects, each containing product details such as product ID, name, description, and price.

### Get Product Details

- **Endpoint**: `GET /product/{id}/`
- **Description**: Retrieve details of a specific product by its unique ID.
- **Parameters**:
  - `{id}` (Path Parameter): The unique identifier of the product.
- **Response**: Detailed information about the specified product, including product ID, name, description, and price.

### Create a New Product

- **Endpoint**: `POST /product/`
- **Description**: Create a new product.
- **Request Body**: JSON object containing product details, including name, description, and price.
- **Response**: The newly created product with a unique ID.

### Delete a Product

- **Endpoint**: `DELETE /product/{id}/`
- **Description**: Delete a specific product by its unique ID.
- **Parameters**:
  - `{id}` (Path Parameter): The unique identifier of the product.
- **Response**: Confirmation of the deletion or an error message if the product does not exist.

## Users

### List Users

- **Endpoint**: `GET /users/`
- **Description**: Retrieve a list of all users.
- **Parameters**: None
- **Response**: An array of user objects, each containing user details such as user ID, name, email, and role.

### Get User Details

- **Endpoint**: `GET /users/{id}/`
- **Description**: Retrieve details of a specific user by their unique ID.
- **Parameters**:
  - `{id}` (Path Parameter): The unique identifier of the user.
- **Response**: Detailed information about the specified user, including user ID, name, email, and role.

### Create a New User

- **Endpoint**: `POST /users/`
- **Description**: Create a new user.
- **Request Body**: JSON object containing user details, including name, email, and role.
- **Response**: The newly created user with a unique ID.

### Delete a User

- **Endpoint**: `DELETE /users/{id}/`
- **Description**: Delete a specific user by their unique ID.
- **Parameters**:
  - `{id}` (Path Parameter): The unique identifier of the user.
- **Response**: Confirmation of the deletion or an error message if the user does not exist.


