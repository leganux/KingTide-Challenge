from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.user_routes import user
from routes.file_routes import file
from routes.file_upload_routes import upload as file_up
from routes.photo_upload_routes import upload as photo_up
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def welcome():
    return {"message": "Welcome to king tide test backend"}


app.include_router(user)
app.include_router(file)
app.include_router(photo_up)
app.include_router(file_up)

app.mount("/files", StaticFiles(directory="files"), name="files")
