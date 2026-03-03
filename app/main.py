from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.config.database import connect_to_mongo, close_mongo_connection
from app.routers import about, contact, experience, project, skill


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(about.router, prefix="/api/about", tags=["About"])
app.include_router(contact.router, prefix="/api/contact", tags=["Contact"])
app.include_router(experience.router, prefix="/api/experience", tags=["Experience"])
app.include_router(project.router, prefix="/api/projects", tags=["Project"])
app.include_router(skill.router, prefix="/api/skills", tags=["Skill"])


@app.get("/")
async def root():
    return {"message": "Portfolio Backend API", "version": settings.APP_VERSION}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

