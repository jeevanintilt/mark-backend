from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user_router
from database import engine
import models
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Add your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    print("Starting the server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)