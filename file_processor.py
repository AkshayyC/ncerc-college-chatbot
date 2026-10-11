
from pathlib import Path
from io import BytesIO

from PIL import Image
import pytesseract
from pypdf import PdfReader
# Windows Tesseract OCR executable location
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}


def extract_text_from_file(file_storage):
    """Extract text from an uploaded PDF, JPEG, or PNG file."""

    filename = file_storage.filename or ""
    extension = Path(filename).suffix.lower().lstrip(".")

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Unsupported file type. Upload a PDF, JPG, JPEG, or PNG file."
        )

    file_bytes = file_storage.read()

    if not file_bytes:
        raise ValueError("The uploaded file is empty.")

    if extension == "pdf":
        reader = PdfReader(BytesIO(file_bytes))
        pages = []

        for page in reader.pages:
            page_text = page.extract_text() or ""
            if page_text.strip():
                pages.append(page_text.strip())

        extracted_text = "\n\n".join(pages)

        if not extracted_text.strip():
            raise ValueError(
                "No selectable text was found in this PDF. "
                "Scanned PDFs need OCR, which we will add next."
            )

        return extracted_text

    image = Image.open(BytesIO(file_bytes))
    image.verify()

    image = Image.open(BytesIO(file_bytes))
    extracted_text = pytesseract.image_to_string(image)

    if not extracted_text.strip():
        raise ValueError(
            "No readable text was found in this image. "
            "Try a clearer image."
        )

    return extracted_text.strip()
