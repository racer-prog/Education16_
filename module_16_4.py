from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id : int
    username : str
    age : int

@app.get("/users")
async def get_users() -> list:
    return users


@app.post("/user/{username}/{age}")
async def register_user(username: Annotated[str, Path(min_length=5,
                                             max_length=20,
                                             description="Enter username",
                                             example="UrbanUser")],
               age: Annotated[int, Path(ge=18,
                                        le=120,
                                        description="Enter age",
                                        example="24"
                                        )]):
    if len(users) == 0:
        id = 1
    else:
        id = len(users) + 1
    a = User(id = id, username = username, age = age)
    users.append(a)
    return a


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1,
                                             le=2000,
                                             description="Enter user_id",
                                             example="1")],
               username: Annotated[str, Path(min_length=5,
                                             max_length=20,
                                             description="Enter username",
                                             example="UrbanUser")],
               age: Annotated[int, Path(ge=18,
                                        le=120,
                                        description="Enter age",
                                        example="24"
                                        )]):

    for u in users:
        if u.id == user_id:
            u.username = username
            u.age = age
            return u

        raise HTTPException(status_code=404, detail="User was not found")



@app.delete("/user/{user_id}/")
async def delete_user(user_id: Annotated[int, Path(ge=1,
                                             le=2000,
                                             description="Enter user_id",
                                             example="1")]):
    for u in users:
        print(users.index(u))
        if u.id == user_id:
            users.pop(users.index(u))
            return u
        raise HTTPException(status_code=404, detail="User was not found")