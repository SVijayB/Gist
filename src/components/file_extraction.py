import PyPDF2
from docx2pdf import convert
import sys
import fitz


def extract_from_file(filename):

    """ pdfFileObj = open('UserFiles/' + filename, "rb")
    print(filename,file=sys.stderr)
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
    result = ""
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        result = result + pageObj.extractText()
    pdfFileObj.close()
    tmp_type = "PDF"
    print(result,file=sys.stderr)
    return {"type": tmp_type, "article": result}"""

    fileObj = fitz.open('UserFiles/' + filename)
    result = ""
    for page in fileObj:
        result += page.get_text() + chr(12)
    tmp_type = "PDF"
    # print(result, file=sys.stderr)
    result = result.encode("ascii", "ignore")
    result = result.decode()
    result = result.replace("\x92", "")
    result = result.replace("\x0c", "")
    return {"type": tmp_type, "article": result}


def extract_from_docx(filename):
    convert(f"UserFiles/{filename}", output_path=f"UserFiles/{filename.split('.')[0]}.pdf")
    return extract_from_file(f"{filename.split('.')[0]}.pdf")


