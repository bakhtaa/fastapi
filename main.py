from fastapi import FastAPI
app= FastAPI()

@app.get("/")
async def root():
    return { "message": "hello world"}

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