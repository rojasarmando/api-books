from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    """
    A function to read the root path.

    Returns:
        dict: A dictionary containing the data.
    """
    return {"data": []}

@router.get("/{book_id}")
def get_book(book_id: int):
    """
    Retrieves a book by its ID.

    Parameters:
        book_id (int): The ID of the book to retrieve.

    Returns:
        dict: A dictionary containing a message with the ID of the retrieved book.
    """
    # Lógica para obtener un libro por ID
    return {"message": f"Get book with id {book_id}"}

@router.post("/")
def create_book():
    """
    Create a new book.

    This function is responsible for creating a new book. It does not accept any parameters.
    
    Returns:
        dict: A dictionary containing a message confirming the creation of a new book.
    """
    # Lógica para crear un nuevo libro
    return {"message": "Create a new book"}






