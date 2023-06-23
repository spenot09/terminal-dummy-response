from fastapi import FastAPI, File, Form, HTTPException, Depends, Body, UploadFile
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
from pydantic import BaseModel


class QuestionResponse(BaseModel):
    response: str


bearer_scheme = HTTPBearer()
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
assert BEARER_TOKEN is not None


def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme != "Bearer" or credentials.credentials != BEARER_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return credentials


app = FastAPI(dependencies=[Depends(validate_token)])


@app.post("/", response_model=QuestionResponse)
def home(prompt=Body(...)):
    """
    Reroute
    """

    return create(prompt)


@app.post("/chatgpt", response_model=QuestionResponse)
def create(prompt=Body(...)):
    """
    Example function where ChatGPT response will come
    """

    return {
        "response": prompt["prompt"]
        + " - Good question, sadly I'm not fully functional juuuuust yet"
    }
