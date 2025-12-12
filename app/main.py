from fastapi import FastAPI

app = FastAPI(title="CI/CD FastAPI App")

@app.get("/")
def root():
    return {"message": "FastAPI работает"}

@app.get("/about")
def about():
    return {"project": "CI/CD c Docker и GitHub Actions"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items")
def create_item(item: dict):
    return {"created_item": item}
