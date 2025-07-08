import os
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from fastapi import FastAPI
from . import llm, db



app = FastAPI()

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    sql_query: str
    data: Optional[List[Dict[str, Any]]] = None
    error: Optional[str] = None

@app.post("/api/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    sql = llm.generate_sql(request.question)
    result_df, db_error = db.execute_query(sql)

    if db_error:
        print(f'Database error: {db_error}')
        return QueryResponse(sql_query=sql, data=[], error=db_error)
        
    response_data = result_df.to_dict(orient='records') if result_df is not None else []

    return QueryResponse(sql_query=sql, data=response_data, error=None)