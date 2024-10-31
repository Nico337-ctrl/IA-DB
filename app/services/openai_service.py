import openai
from config.settings import settings

openai.api_key = settings.OPEN_AI_API_KEY

async def generate_sql_query(human_query: str, schema: str) -> str:
    system_message = f"""..."""  # Mensaje del sistema definido previamente
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": human_query},
        ]
    )
    return response.choices[0].message["content"]

async def generate_answer(result: list, human_query: str) -> str:
    system_message = f"""..."""  # Mensaje del sistema para generar respuestas legibles
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
        ]
    )
    return response.choices[0].message["content"]
