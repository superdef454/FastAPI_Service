from typing import List
import uuid
from fastapi import APIRouter, Response

# from ..models.models import Edu_prog, Edu_prog_file, Up, Up_file
# from ..services.ID import GenService

router = APIRouter(
    prefix='/IDS',
)

@router.get('/')
def get_edu_prog(
    size: int
):
    out = {"IDS":[]}
    for i in range(size):
        out['IDS'].append(i)
    return out

# @router.get('/up', response_model=List[Up])
# def get_up(
#     size: int
# ):
#     return GenService().get_up(size=size)

# @router.post('/edu_prog')
# def create_json_file_edu_prog(
#     edu_prog_file: Edu_prog_file
# ):
#     return Response(content=GenService().json_edu_prog(edu_prog_file), media_type="text/plain")

# @router.post('/up')
# def create_json_file_up(
#     up_file: Up_file
# ):
#     return Response(content=GenService().json_up(up_file), media_type="text/plain")