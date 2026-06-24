from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="AI Healthcare Platform API", version="1.0.0")

# Enable CORS so your frontend fetch() requests don't get blocked
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Route Stub Examples
@app.get("/api/health")
def health_check():
    return {"status": "healthy", "database": "connected"}

# Mount the frontend directory so FastAPI can serve your HTML/CSS/JS directly
# In production, visiting your server URL /frontend/doctor.html will render the UI
app.mount("/frontend", StaticFiles(directory="../frontend"), name="frontend")