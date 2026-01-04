from fastapi import APIRouter 
from schemas.people_schema import People
from service.people_service import PeopleService 

router = APIRouter(
    prefix='/people',
    tags=["people"],
)

@router.get('/')
async def get_all_people():
    return PeopleService.get_all_people()
