import os
import sys

from flask import jsonify, request, Blueprint
from fpdf import FPDF
from werkzeug.utils import secure_filename
from Algo.hashcal import hash_file
from src.components import summarizer
from src.components.extraction import extract
from src.components.file_extraction import extract_from_file, extract_from_docx

summarize_bp = Blueprint("summarize", __name__, url_prefix="/summarize")


def generate(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("Poppins", style="", fname="Poppins\\Poppins-Light.ttf", uni=True)
    pdf.add_font("Poppins", style="B", fname="Poppins\\Poppins-SemiBold.ttf", uni=True)
    pdf.add_font("Poppins", style="I", fname="Poppins\\Poppins-BlackItalic.ttf", uni=True)
    pdf.add_font("Poppins", style="BI", fname="Poppins\\Poppins-BoldItalic.ttf", uni=True)
    pdf.set_font("Poppins", size=15)
    ln = 0
    for key in data.keys():
        pdf.set_font("Poppins","B",size=18)
        pdf.cell(0,10,txt=key.upper(),align='C',ln=1)
        pdf.set_font("Poppins", "", size=12)
        pdf.multi_cell(0, 10, txt=data.get(key), align='L')
        ln += 1
    pdf.output("new_file.pdf")


@summarize_bp.route("/", methods=["GET"])
def summarize():
    if request.method == 'GET':
        # print(1111111111,file=sys.stderr)
        type = request.args.get("type")
        link = request.args.get("link")
        data = extract(int(type), link)
        result = summarizer.summarize(data)
        generate(result)
        return jsonify(result)


@summarize_bp.route("/file", methods=["POST"])
def file():
    f = request.files.get('FILE')
    filename = hash_file(f.stream.read()) + "." + secure_filename(f.filename).split(".")[-1]
    print(f"Filename : {filename}", file=sys.stderr)
    f.stream.seek(0)
    f.save(os.path.join('UserFiles', filename))

    file_extn = filename.split(".")[1]
    print(file_extn, file=sys.stderr)
    # ExtractData
    if file_extn == 'pdf':
        data = extract_from_file(filename)
        print(data, file=sys.stderr)
    if file_extn == 'docx' or file_extn == "doc":
        data = extract_from_docx(filename)
    # print(data,file=sys.stderr)
    result = summarizer.summarize(data)
    return jsonify(result), 200
