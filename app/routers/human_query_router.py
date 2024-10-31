from fastapi import APIRouter
from models.schemas import PostHumanQueryPayload, PostHumanQueryResponse
from services.openai_service import generate_sql_query, generate_answer
from services.db_service import get_schema, query

router = APIRouter()

@router.post("/human_query", response_model=PostHumanQueryResponse)
async def human_query(payload: PostHumanQueryPayload):
    schema = await get_schema()
    sql_query = await generate_sql_query(payload.human_query, schema)
    
    if not sql_query:
        return {"error": "Falló la generación de la consulta SQL"}

    result = await query(sql_query)
    answer = await generate_answer(result, payload.human_query)
    if not answer:
        return {"error": "Falló la generación de la respuesta"}

    return {"answer": answer}
