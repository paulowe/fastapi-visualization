from typing import Dict, List, Optional
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str
class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comments: int
    tags: List[str] = []
    # Key and value are both strings
    metadata: Dict[str, str] = {'key': "val1"}
    image: Optional[Image] = None

@router.post('/new/{id}/')
def create_blog(blog: BlogModel, id:int, version=1):
    return {'data': blog,
            'id': id,
            'version': version}

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int, comment_title:int = Query(...,
    title='Title of comment',
    description='some description about comment_title',
    alias='coomentTitle',
    deprecated=True),
    content:str = Body('hey great post on RBC wealth management solutions'),
    mandatoryfield:str = Body(..., min_length=20, regex='^[a-z\s]*$'),
    v: Optional[List[str]] = Query([1.0, 2.1, 3.2]),
    comment_id: int = Path(None, gt=5, le=10)):

    return {'blog': blog,
    'id': id,
    'comment_title': comment_title,
    'content': content,
    'mandatoryfield': mandatoryfield,
    'version': v,
    'comment_id': comment_id
    }  


def required_functionality():
    return {'message': 'Learning FastAPI is important at RBC'}
