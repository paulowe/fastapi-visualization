from fastapi import APIRouter
from fastapi import Response, status, Depends
from router.blog_post import required_functionality
from enum import Enum
from typing import Optional  # In case you want to provide optional parameters for your API methods

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get(
    '/all',
    summary = "Gets all blogs",
    description=" Moer detailde description",
    response_description="the list of all blogs rd ")
def get_all_blogs(page_size=2, page:Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {'message':f'All {page_size} blogs on page {page}', 'req': req_parameter}

@router.get(
    '/{id}/comments/{comment_id}',
    tags=['comment'])
def get_comment(id:int, comment_id:int, valid: bool = True, username: Optional[str]=None, req_parameter: dict = Depends(required_functionality)):
    """
     **id** - id of blog

     valid - bool

     uname - optional int 

    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid comment? {valid}, username {username}'}

class BlogType(str, Enum):
   short='short-blog'
   story='story-blog'
   howto='howto-blog'

@router.get('/type/{type}', tags=['blog'])
def get_blogs_by_type(type: BlogType, req_parameter: dict = Depends(required_functionality)):
    return {'message':f'Blogs of type {type}'} 


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id:int, response: Response, req_parameter: dict = Depends(required_functionality)):
    if id> 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog id {id} not found'}
    else: 
        response.status_code = status.HTTP_200_OK 
        return {'message':f'Blog with ID {id}'}
