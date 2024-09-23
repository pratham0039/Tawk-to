from fastapi import FastAPI
from app.models import SummarizeRequest, SummarizeResponse
from app.utils import summarize_text
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    summary = summarize_text(request.text)
    return {"summary": summary}


# Serve the OpenAPI spec
app.mount("/openapi", StaticFiles(directory="openapi"), name="openapi")