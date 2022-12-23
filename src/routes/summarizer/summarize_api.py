from flask import Flask, jsonify, request, Blueprint, send_from_directory
from werkzeug.utils import secure_filename
from src.routes.extraction.file_extraction import extract_from_file, extract_from_docx
from src.components.extraction import extract
from src.components import summarizer
from src.components.result_generation import result_generation
from datetime import datetime
import time
import os
from scripts.hashcal import hash_file

summarize_bp = Blueprint("summarize", __name__, url_prefix="/summarize")


@summarize_bp.route("/", methods=["GET"])
def summarize():
    type = request.args.get("type")
    link = request.args.get("link")
    report = request.args.get("report")
    return pdf_generator(type, link, report)


@summarize_bp.route("/file", methods=["POST"])
def file():
    f = request.files.get("FILE")
    report = request.args.get("report")
    filename = f.filename
    file_extn = filename.split(".")[1]
    f.stream.seek(0)
    f.save(os.path.join("temp_files", filename))
    filename = "temp_files/" + filename
    if file_extn == "png" or file_extn == "jpg" or file_extn == "jpeg":
        type = 2
    elif file_extn == "pdf":
        type = 3
    elif file_extn == "docx" or file_extn == "doc":
        type = 4
    return pdf_generator(type, filename, report)


def pdf_generator(type, filename, report):
    current_time = datetime.now()
    start_time = time.time()
    data = extract(int(type), filename)
    extraction_time = time.time() - start_time
    result = summarizer.summarize(data)
    summarizer_time = time.time() - start_time - extraction_time
    result["start_time"] = current_time
    result["extraction_time"] = round(extraction_time, 3)
    result["summarizer_time"] = round(summarizer_time, 3)
    if report != None and report == str(1):
        filepath = os.path.abspath(os.getcwd()) + "/temp"
        pdf_result = result_generation(result)
        return send_from_directory(filepath, pdf_result)
    return jsonify(result)
