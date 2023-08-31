import os

from PIL import Image
from pathlib import Path
from utils import get_project_root
from app.adapters.repository import AbstractRepository

UPLOAD_IMAGES_DIRECTORY = get_project_root() / "app" / "upload" / "uploads"                         # Move to a global config file
MODEL_DIR = get_project_root() / "models"                                                           # Move to a global config file

class LocalRepository(AbstractRepository):
    def add_image(self, image: Image):
        if not os.path.exists(UPLOAD_IMAGES_DIRECTORY):
            os.makedirs(UPLOAD_IMAGES_DIRECTORY)
        image_filename = Path(UPLOAD_IMAGES_DIRECTORY) / image.filename
        image.save(image_filename)

    def get_images(self) -> list:
        images = []
        for image in os.listdir(UPLOAD_IMAGES_DIRECTORY):
            try:
                with Image.open(UPLOAD_IMAGES_DIRECTORY / image) as img:
                    images.append(img)
            except:
                pass
        return images
    
    def get_image_by_name(self, path: str) -> Image:
        try:
            with Image.open(UPLOAD_IMAGES_DIRECTORY / path) as img:
                return img
        
        except FileNotFoundError:
            return None