from api.bin.filters import apply_filter
from typing import List, Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import StreamingResponse
import io


app = FastAPI()


filters_available = [
    "blur",
    "contour",
    "detail",
    "edge_enhance",
    "edge_enhance_more",
    "emboss",
    "find_edges",
    "sharpen",
    "smooth",
    "smooth_more",
]


@app.api_route("/", methods=["GET", "POST"])
def index():
  response = {
      "filters_available": filters_available,
      "usage": {"http_method": "POST", "URL": "/<filter_available>/"},
  }
  return jsonable_encoder(response)


@app.post("/{filter}")
def image_filter(filter: str, img: UploadFile = File(...)):
  if filter not in filters_available:
    response = {"error": "incorrect filter"}
    return jsonable_encoder(response)

  filtered_image = apply_filter(img.file, filter)

  return StreamingResponse(filtered_image, media_type="image/jpeg")
