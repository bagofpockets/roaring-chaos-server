from fastapi import APIRouter, Request, status

router = APIRouter()


@router.post(path='/health', status_code=status.HTTP_200_OK)
async def health_chekup(request: Request) -> dict:
    return {"healthy": True}
