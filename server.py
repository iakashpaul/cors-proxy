from pydantic import BaseModel,Json
from fastapi import FastAPI,Request,Response
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    transcript: Json

@app.get("/")
def base():
    return """PROXY ONLINE on /llm route $curl -X POST https://iakashpaul-cors-proxy-baseten.hf.space/llm --data '{"prompt":"hello"}'"""

prefix_prompt="""<s>[INST]Summarize the following transcript[/INST]\n"""
suffix_prompt="""\n"""
@app.post("/llm")
async def main(request: Request):
    input_json =  await request.json()
    print(input_json)
    final_prompt = prefix_prompt + str(input_json["prompt"]) + suffix_prompt
    resp = requests.post(
    "https://YOUR_MODEL_ID.api.baseten.co/production/predict",
    headers={"Authorization": "Api-Key YOUR_API_KEY"},
    json={'prompt': final_prompt ,'temperature': 0.001, 'max_new_tokens': 100, 'repetition_penalty':1.2},
)   
    llm_response = resp.json()
    llm_response = llm_response.rsplit("[/INST]")[-1].split("</s>")[0];
    print(llm_response)
    return {"text":str(llm_response)}
