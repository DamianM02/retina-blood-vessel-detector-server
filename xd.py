
#--------------------------------------------------------------
# Brudnopis
# from typing import Literal
# print(1)
#
#
# def f(a: Literal["cat", "dog"]):
#     return 1
#
#
# f()

# from pydantic import BaseModel
#
# class User(BaseModel):
#     id: int
#     name: str =1
#
# d = {"id": "23"}
#
# u = User(**d)
# print(u)
# print(b"uu")


from typing import Annotated, Literal

from fastapi import FastAPI, Query, Body
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.post("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()], x: Annotated[int, Body(...)]):
    return x

@app.get("/itemsy/")
async def read_items(
    limit: Annotated[int, Query( gt=0, le=100)] = 100,
    offset: Annotated[int, Query( ge=0)] = 0,
    order_by: Annotated[Literal["created_at", "updated_at"], Query()] = "created_at",
    tags: Annotated[list[str], Query()] = [] # NIE WOLNO, bo wskaźniki
):
    return {
        "limit": limit,
        "offset": offset,
        "order_by": order_by,
        "tags": tags
    }


