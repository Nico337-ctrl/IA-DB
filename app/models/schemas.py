from pydantic import BaseModel
from typing import List, Dict, Any

class PostHumanQueryPayload(BaseModel):
    human_query: str

class PostHumanQueryResponse(BaseModel):
    result: List[Dict[str, Any]]
