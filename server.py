from fastapi import FastAPI, HTTPException
import uvicorn
from config import db

from pydantic import BaseModel
from fastapi.responses import JSONResponse
from starlette import status
from route.city import cityPath
from route.email import emailPath



# python -m venv venv
app = FastAPI()



app.include_router(emailPath)
app.include_router(cityPath)
@app.get('/get', status_code=status.HTTP_200_OK)
async def hello():
    return "Hello server is workingsssss"


# # python -m uvicorn server:app --reload



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8181)