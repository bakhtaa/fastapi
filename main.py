from datetime import datetime
from random import randint
from fastapi import FastAPI, HTTPException, Request, Response
from typing import Any
app= FastAPI()

data = [
    {
        "campaign_id" : 1,
        "name": "summer lanch",
        "due_date": datetime.now(),
        "created_at": datetime.now()
    },
    {
        
        "campaign_id" : 2,
        "name": "hiver lanch",
        "due_date": datetime.now(),
        "created_at": datetime.now()
    },
    {
        "campaign_id" : 3,
        "name": "black friday",
        "due_date": datetime.now(),
        "created_at": datetime.now()
    }
]
@app.get("/")
async def root():
    return { "message": "hello world"}



@app.get("/compaigns")
async def read_compaigns():
    return ({ "compaigns": data})


@app.get('/compaigns/{id}')
async def getcompaign(id: int):
    for item in data:
        if item.get("campaign_id")==id:
            return({"selected item": item})
    raise HTTPException(status_code=404)


@app.post('/compaigns', status_code=201)
async def createcompaign(body: dict[str, Any]):
    
    print(body)
    new : Any = {
        "campaign_id" : randint(100,1000),
        "name": body.get("name"),
        "due_date": body.get("due_date"),
        "created_at": datetime.now()
    }
    data.append(new)
    return { "compaign": new}

@app.put("/compaigns/{id}")
async def updatecompaign(id : int, body : dict[str, Any]):
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            updated_compaign :  Any= {
                "campaign_id": campaign.get("campaign_id"),
                "name": body.get("name"),
                "due_date": body.get("due_date"),
                "created_at": campaign.get("created_at")
            }
            data[index]=updated_compaign
            return {"updated": updated_compaign}
    raise HTTPException(status_code=404)

@app.delete("/campaigns/{id}")
async def deletecampaign(id: int):
    for index,campaign in enumerate(data):
        if campaign.get("campaign_id")==id:
            data.pop(index)
            return Response(status_code=204)



  


"""
campaigns:
-campaign_id
-name
-due_date
-created_at

the compaign contains marketing pieces
pieces:
_piece_id
_campaign_id
_name
_content
_contetnt_type
_created_at
"""