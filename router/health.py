from typing import Optional

from fastapi import APIRouter, Depends, Header, HTTPException

router = APIRouter()

@router.get("/", status_code=200)
def health_check():
    return {"status": "ok"}

