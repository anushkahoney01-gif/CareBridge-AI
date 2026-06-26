from fastapi import APIRouter

router = APIRouter()

@router.get("/patient")
def patient_home():
    return {"message": "Patient router is working"}
