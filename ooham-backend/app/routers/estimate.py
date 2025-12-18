from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
# from app.services import estimator
import asyncio

getestimaterouter = APIRouter()

class EstimateRequest(BaseModel):
    project_description: Optional[str] = None
    seniority: Optional[str] = None
    deadline_preference: Optional[str] = None
    budget: Optional[str] = None

@getestimaterouter.post("/estimate")
async def getestimate(req: EstimateRequest):
    # 1) parse features via OpenAI (async)
    # features = await estimator.call_openai_parse(req.project_description)
    # # 2) generate estimate payload
    # payload = estimator.generate_estimate_payload(features, req.seniority, req.deadline_preference, req.budget)
    
    dummyData = {
        "estimated_time": "8-10 weeks",
        "estimated_cost": "$45,000 - $60,000",
        "currency": "USD",
        "risk_score": "Medium (6/10)",
        "notes": "Based on moderate complexity and mid-level team",
        "team": [
            "1 Senior Full-Stack Developer",
            "1 Mid-Level Frontend Developer",
            "1 UI/UX Designer",
            "1 QA Engineer"
        ],
        "risks": [
            "Third-party API integration complexity",
            "Potential scope creep in user requirements",
            "Database schema changes mid-project",
            "Authentication and authorization complexity"
        ],
        "task_breakdown": [
            "Requirements gathering and documentation (1 week)",
            "UI/UX design and prototyping (2 weeks)",
            "Backend API development (3 weeks)",
            "Frontend development (3 weeks)",
            "Integration and testing (2 weeks)",
            "Deployment and launch (1 week)"
        ],
        "architecture": {
            "frontend": "Next.js with TypeScript",
            "backend": "FastAPI (Python)",
            "database": "PostgreSQL",
            "hosting": "Vercel (Frontend), Railway (Backend)",
            "authentication": "NextAuth.js",
            "apis": ["Stripe for payments", "SendGrid for emails"]
        }
    }

    return dummyData