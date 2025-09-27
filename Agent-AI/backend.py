from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
  model_name: str
  model_provider: str
  system_prompt: str
  messages: List[str]
  allow_search: bool

from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAME=["llama-3.3-70b-versatile"]

app = FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
  """
  API endpoint to interact with the LangGraph and search tools
  It dynamically selects the model specified in the request  
  """

  if request.model_name not in ALLOWED_MODEL_NAME:
    return {"error": "Invalid model name"}

  
  response = get_response_from_ai_agent(
    llm_id=request.model_name,
    query=request.messages,
    allow_search=request.allow_search,
    system_prompt=request.system_prompt,
    provider=request.model_provider)

  return response

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)
