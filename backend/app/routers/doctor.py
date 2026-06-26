from fastapi import APIRouter

router = APIRouter()

@router.get("/doctor")
def doctor_home():
    return {"message": "Doctor router is working"}
