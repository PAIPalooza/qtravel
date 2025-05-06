"""
QTravel API - Main FastAPI Application
Follows QTravel coding standards with clear responsibility boundaries and error handling
"""
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from sqlalchemy.orm import Session
import os

# Import models and schemas - will be populated as we implement features
from app.models import Base

app = FastAPI(
    title="QTravel API",
    description="AI-powered travel planning API",
    version="0.1.0"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint - health check"""
    return {"status": "ok", "message": "QTravel API is running"}

# API version info endpoint
@app.get("/api/version")
async def version():
    """API version information"""
    return {
        "version": "0.1.0",
        "name": "QTravel API",
        "schema_version": "1.0.0"
    }

# Placeholder for the generate-itinerary endpoint from issue #5
@app.post("/generate-itinerary")
async def generate_itinerary():
    """
    Generate a travel itinerary based on user preferences
    To be implemented in issue #5
    """
    return {"message": "Endpoint to be implemented"}

# Main application startup
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
