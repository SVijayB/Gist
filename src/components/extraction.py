from newspaper import Article
from PIL import Image
import PyPDF2
from docx2pdf import convert
from pytesseract import pytesseract
import os

# Component used for data extraction from text.
def extract(type, link):
    tmp_type = ""
    if type == 1:  # Article link
        # url = "https://www.gadgetsnow.com/tech-news/india-becomes-the-first-country-in-asia-pacific-to-use-satellite-navigation-to-land-aircrafts/articleshow/91172431.cms"
        url = link
        article = Article(url)
        article.download()
        article.parse()
        result = article.text
        tmp_type = "Article"
    elif type == 2:  # Image taken
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        # image_path = r"assets\footercredits.png"
        image_path = link
        img = Image.open(image_path)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        result = text[:-1]
        tmp_type = "Image"
    elif type == 3:  # PDF file
        # pdfFileObj = open("example.pdf", "rb")
        pdfFileObj = open(link, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        result = ""
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            result = result + pageObj.extractText()
        pdfFileObj.close()
        tmp_type = "PDF"
    elif type == 4:  # Document file
        convert(link, "temp/output.pdf")
        result = extract(3, "temp/output.pdf")
        os.remove("temp/output.pdf")
        tmp_type = "Document"
    else:
        return {"error": "Invalid type"}

    return {"type": tmp_type, "link": link, "result": result}
