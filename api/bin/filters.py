from PIL import Image, ImageFilter
import io


def apply_filter(file: object, filter: str) -> object:
  image = Image.open(file)
  image = image.filter(eval(f"ImageFilter.{filter.upper()}"))

  file = io.BytesIO()
  image.save(file, "JPEG")
  file.seek(0)

  return file
