from fastapi import FastAPI
from routers import books
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.include_router(books.router, prefix="/books", tags=["books"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API de Libros",
        version="1.0.0",
        description="Esta es una API de libros",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi