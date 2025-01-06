from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()
users: dict[str, str] = {'1': 'Имя: Example, возраст: 18'}



# @app.get("/")
# async def home_page() -> str:
#     return "Главная страница"
#
#
# @app.get("/user/admin")
# async def admin_page() -> str:
#     return "Вы вошли как администратор"

# @app.get("/user/{user_id}")
# async def user_page(user_id: Annotated[int, Path(gt=0,
#                                                  lt=100,
#                                                  description="Enter User ID",
#                                                  example=1)]):
#     return f"Вы вошли как пользователь № {user_id}"



@app.get("/users")
async def get_users() -> dict[str, str]:
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
    key = list(users.keys())
    user_id = str(len(key)+1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered."


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
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is updated."


@app.delete("/user/{user_id}/")
async def delete_user(user_id: Annotated[int, Path(ge=1,
                                             le=2000,
                                             description="Enter user_id",
                                             example="1")]):
    users.pop(str(user_id), None)
    return f"User {user_id} is deleted."