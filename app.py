from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    with open("data/advisories.json") as f:
        advisories = json.load(f)
    with open("data/iocs.json") as f:
        iocs = json.load(f)
    return templates.TemplateResponse("index.html", {"request": request, "advisories": advisories, "iocs": iocs})

@app.get("/advisory/{advisory_id}", response_class=HTMLResponse)
async def advisory_detail(advisory_id: int, request: Request):
    with open("data/advisories.json") as f:
        advisories = json.load(f)
    advisory = advisories[advisory_id] if advisory_id < len(advisories) else {}
    return templates.TemplateResponse("advisory_detail.html", {"request": request, "advisory": advisory})