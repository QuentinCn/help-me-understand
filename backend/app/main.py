from fastapi import FastAPI
import torch
import os
import psycopg2

app = FastAPI()


@app.get("/hello")
def hello_world():
    response = {"message": "Hello World"}

    # Check GPU availability
    if torch.cuda.is_available():
        gpu_info = {
            "gpu_available": True,
            "gpu_count": torch.cuda.device_count(),
            "gpu_name": torch.cuda.get_device_name(0),
            "cuda_version": torch.version.cuda
        }
    else:
        gpu_info = {"gpu_available": False}

    response["gpu_info"] = gpu_info
    return response

DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/test-db")
def test_db():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return {"result": result}

@app.get("/add-qa")
def add_qa():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    pdf_id = 'auui'
    question = 'ijioj'
    answer = 'ijioj'
    feedback_score = True

    cur.execute(
        """
        INSERT INTO qa_logs (pdf_id, question, answer, feedback_score)
        VALUES (%s, %s, %s, %s)
        RETURNING id, creation_time
        """,
        (pdf_id, question, answer, feedback_score)
    )
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {"result": result}