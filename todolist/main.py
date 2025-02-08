from http import HTTPStatus

from fastapi import FastAPI

from todolist.routers.auth import router_auth
from todolist.routers.users import router_users
from todolist.schema import Message

app = FastAPI()


app.include_router(router_auth)
app.include_router(router_users)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}
