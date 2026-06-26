import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from app.config import settings
from app.database import Base, engine

# Import routers (we will create these next)
from app.routers import doctor, patient

# Automatically create the database tables if they don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

# Setup CORS policies so frontend Fetch API requests function across origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specific URLs in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register modular route endpoints
app.include_router(doctor.router, prefix="/api", tags=["Doctor Operations"])
app.include_router(patient.router, prefix="/api", tags=["Patient Operations"])

# Serve frontend static assets only if the directory exists
frontend_dir = os.path.join(os.path.dirname(__file__), "../../frontend")
if os.path.isdir(frontend_dir):
    app.mount("/frontend", StaticFiles(directory=frontend_dir), name="frontend")

@app.get("/")
def read_root():
    return {"status": "CareBridge AI is running"}

# Shared backend health check endpoint
@app.get("/api/health")
def health_check():
    return {"status": "healthy", "app": settings.APP_NAME}
