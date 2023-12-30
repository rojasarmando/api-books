from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"data": []}

@router.get("/{book_id}")
def get_book(book_id: int):
    # Lógica para obtener un libro por ID
    return {"message": f"Get book with id {book_id}"}

@router.post("/")
def create_book():
    # Lógica para crear un nuevo libro
    return {"message": "Create a new book"}






