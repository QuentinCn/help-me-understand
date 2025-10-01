from fastapi import FastAPI
import torch
import os

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