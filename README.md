# Basic -FASTAPI

A simple REST API built with FastAPI that implements CRUD (Create, Read, Update, Delete) operations for managing items in an in-memory store.

## Features

- RESTful API endpoints for item management
- In-memory data storage
- Pydantic models for data validation
- Automatic API documentation
- Type hints and response models
- Error handling

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/VishalPrasanna11/Basic-FASTAPI.git
cd Basic-FASTAPI
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS and Linux:
```bash
source venv/bin/activate
```

4. Install the required packages:
```bash
pip install fastapi uvicorn
```

## Project Structure

```
.
├── README.md
├── main.py
└── routes.py
```

## Running the Application

Start the server with:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /items | List all items |
| GET | /items/{item_id} | Get a specific item |
| POST | /items | Create a new item |
| PUT | /items/{item_id} | Update an existing item |
| DELETE | /items/{item_id} | Delete an item |

## API Documentation

After starting the server, you can access:
- Interactive API documentation (Swagger UI) at `http://localhost:8000/docs`
- Alternative API documentation (ReDoc) at `http://localhost:8000/redoc`

## Using Postman

### Setting Up Postman

1. Create a new collection in Postman (e.g., "FastAPI CRUD")
2. Set the base URL to: `http://localhost:8000`
3. For all requests that include a body, set the header:
   - Key: `Content-Type`
   - Value: `application/json`

### Example Requests

### 1. Create Item (POST /items/)
```json
{
    "name": "Laptop",
    "description": "MacBook Pro M2",
    "price": 1299.99,
    "is_available": true
}
```

### 2. Get All Items
- Method: GET
- URL: `/items`
- No body required

### 3. Get Specific Item
- Method: GET
- URL: `/items/1`
- No body required

### 4. Update Item (PUT /items/1)
```json
{
    "name": "Updated Laptop",
    "description": "MacBook Pro M2 Max",
    "price": 1499.99,
    "is_available": true
}
```

### 5. Delete Item
- Method: DELETE
- URL: `/items/1`
- No body required

### Testing Tips
- Use the "Collections" feature in Postman to save all your requests
- Create environment variables for base URL
- Use the "Tests" tab to write automated tests
- Use "Save Response" feature to compare responses across different runs

## Data Model

### Item

```python
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True
```

## Error Handling

The API includes basic error handling:
- 404 Not Found: When requesting a non-existent item
- 422 Validation Error: When sending invalid data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your chosen license here]

## Contact

[Add your contact information here]