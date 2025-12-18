from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers.estimate import getestimaterouter 
from core.database import Base,engine
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

@asynccontextmanager
async def lifespan(app:FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Smart Estimator Backend",lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(getestimaterouter,prefix="/ooham/api")

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
