from fastapi import FastAPI, Path, Query
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

# 创建fastapi实例
app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


# 路径参数
@app.get('/user/{user_id}')
async def path_param(user_id: int):
    return {'userid': user_id}


# 枚举参数
class Gender(str, Enum):
    male = 'male'
    female = 'female'


@app.get('/gender/{gender}')
async def gender(gender: Gender):
    return {'gender': gender}


# 查询参数
@app.get('/user')
async def get_user(uid: int, name: Optional[str] = 'wc'):
    return {'userid': uid, 'username': name}


# 路径参数和查询参数混合调用
@app.get('/user_name/{user_id}')
async def get_user_id(user_id: int, name: str = 'wc'):
    return {'userid': user_id, 'username': name}


# 发送请求体
class User(BaseModel):
    # field为请求体的参数进行校验  ...为必选项，里面的参数和query参数差不多
    uid: int = Field(...)
    name: str = 'wc'
    sex: Gender


@app.post('/user')
async def post_user(user: User):
    return {'uid': user.uid, 'name': user.name, 'sex': user.sex}


#路径参数的校验 ...为必选项
@app.get('/user/{uid}')
async def get_user_id(uid: int = Path(..., title='user id', ge=0, le=10000)):
    return {'uid': uid}


# 查询参数的校验 ...为必选项
@app.get('/book')
async def get_book(bid: int = Query(..., ge=100, le=999)):
    return {'bid': bid}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='fastapi_test:app', reload=True)
