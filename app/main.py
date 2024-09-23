from fastapi import FastAPI
from app.models import SummarizeRequest, SummarizeResponse
from app.utils import summarize_text

app = FastAPI()

@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    summary = summarize_text(request.text)
    return {"summary": summary}
