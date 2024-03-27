# Product Management RESTful API

## Introduction

This project aims to create a RESTful API for managing product data, including CRUD operations, token-based authentication, permission management, pagination, reverse URL, and serialization.

## Instructions

### Getting Started

To get started with the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/lkhaoua12/Django-REST.git
    cd Django-REST
    ```

2. Create a new virtual environment and activate it:

    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

3. Navigate to the project directory:

    ```bash
    cd dev
    ```

4. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Navigate to the backend directory:

    ```bash
    cd backend
    ```

6. Start the Django development server:

    ```bash
    python3 manage.py runserver
    ```

7. Access the Django Rest Framework built-in browser view:

    ```
    http://localhost:8000/api/products/
    ```

8. Alternatively, you can access the API using the provided Python client:

    ```bash
    cd py_client
    python3 client.py
    ```

### Using the API

Once the server is running, you can use the API to perform CRUD operations on product data. Additionally, token-based authentication and permission management are implemented for secure access.

### Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests with your enhancements or bug fixes.

