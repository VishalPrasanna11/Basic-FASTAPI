from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Define the Item model
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

app = FastAPI()

# In-memory storage
items = []
item_id_counter = 1

@app.get("/")
def read_root():
    """Return a welcome message."""
    return {"Hello": "World"}

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    """Create a new item."""
    global item_id_counter
    item.id = item_id_counter
    item_id_counter += 1
    items.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    """Get all items."""
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    """Get a specific item by ID."""
    item = next((item for item in items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    """Update an existing item."""
    for i, item in enumerate(items):
        if item.id == item_id:
            updated_item.id = item_id  # Preserve the original ID
            items[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item."""
    for i, item in enumerate(items):
        if item.id == item_id:
            del items[i]
            return {"message": f"Item {item_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")