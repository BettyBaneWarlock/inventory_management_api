# inventory_management_api

Project Description
The Inventory Management System is a web application built with Django that helps users efficiently manage their inventory items. The application allows authenticated users to add, edit, delete, and view their inventory items, including details such as item name, description, quantity, price, and category. The system also provides functionality for tracking low inventory levels and notifying users when an item is running low.

The project implements features for user authentication, allowing users to register, log in, and securely access their own inventory data. The backend is powered by Django, utilizing a RESTful API to handle CRUD operations for inventory items. The system uses SQLite as the database and is designed to be lightweight and efficient, with a simple and user-friendly interface for managing inventory.

This project is intended to provide a foundational inventory management solution that can be easily customized and expanded to meet specific needs. It serves as a practical example of how to build a full-stack application with Django and how to integrate an API for inventory management.

API Documentation for Inventory Management System

Base URL:
https://beteldessalegn.pythonanywhere.com/api/

1. Authentication
To interact with the API, you must authenticate using a token.

Endpoint to get the Auth Token:
POST /api-token-auth/

Request Body:
{
    "username": "your_username",
    "password": "your_password"
}

Response:
{
    "token": "your_auth_token"
}
Use this token for subsequent requests.

How to include the token in requests:
For all other API requests, include the Authorization header with the token:
Authorization: Token your_auth_token

2. Inventory Items
GET /inventory-items/
Get a list of all inventory items for the logged-in user.

Request:
GET /api/inventory-items/
Authorization: Token your_auth_token

Response:
[
    {
        "id": 1,
        "name": "Item Name",
        "description": "Item Description",
        "quantity": 10,
        "price": 100.00,
        "category": "Category Name",
        "date_created": "2025-01-10T12:00:00Z",
        "user": 1
    }
]

POST /inventory-items/
Create a new inventory item.

Request:
POST /api/inventory-items/
Authorization: Token your_auth_token
Content-Type: application/json

Request Body:
{
    "name": "New Item",
    "description": "Item Description",
    "quantity": 20,
    "price": 150.00,
    "category": 1
}

Response:
{
    "id": 2,
    "name": "New Item",
    "description": "Item Description",
    "quantity": 20,
    "price": 150.00,
    "category": "Category Name",
    "date_created": "2025-01-10T12:00:00Z",
    "user": 1
}

PUT /inventory-items/{id}/
Update an existing inventory item.

Request:
PUT /api/inventory-items/2/
Authorization: Token your_auth_token
Content-Type: application/json

Request Body:
{
    "name": "Updated Item",
    "description": "Updated Description",
    "quantity": 15,
    "price": 120.00,
    "category": 1
}

Response:
{
    "id": 2,
    "name": "Updated Item",
    "description": "Updated Description",
    "quantity": 15,
    "price": 120.00,
    "category": "Category Name",
    "date_created": "2025-01-10T12:00:00Z",
    "user": 1
}

DELETE /inventory-items/{id}/
Delete an inventory item.

Request:
DELETE /api/inventory-items/2/
Authorization: Token your_auth_token

Response:
{
    "message": "Item deleted successfully"
}

3. Categories
GET /categories/
Get a list of all available categories.

Request:
GET /api/categories/
Authorization: Token your_auth_token

Response:
[
    {
        "id": 1,
        "name": "Category 1"
    },
    {
        "id": 2,
        "name": "Category 2"
    }
]
4. Error Responses

400 Bad Request: Your request is invalid. It will contain error details in the response body.
401 Unauthorized: You need to provide a valid token to access this resource.
404 Not Found: The resource was not found.
500 Internal Server Error: Something went wrong on the server.

Example Requests Using Postman
a. GET All Inventory Items:

URL: https://beteldessalegn.pythonanywhere.com/api/inventory-items/
Method: GET
Headers:
Authorization: Token your_auth_token

b. Create New Inventory Item:

URL: https://beteldessalegn.pythonanywhere.com/api/inventory-items/
Method: POST
Body (JSON):
{
    "name": "New Item",
    "description": "Item Description",
    "quantity": 20,
    "price": 150.00,
    "category": 1
}

c. Update Inventory Item:

URL: https://beteldessalegn.pythonanywhere.com/api/inventory-items/2/
Method: PUT
Body (JSON):
{
    "name": "Updated Item",
    "description": "Updated Description",
    "quantity": 15,
    "price": 120.00,
    "category": 1
}

d. Delete Inventory Item:

URL: https://beteldessalegn.pythonanywhere.com/api/inventory-items/2/
Method: DELETE
Headers:
Authorization: Token your_auth_token
