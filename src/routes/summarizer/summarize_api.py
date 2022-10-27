import os
import sys

from flask import Flask, jsonify, request, Blueprint, url_for
from werkzeug.utils import redirect, secure_filename

from Algo.hashcal import hash_file
from src.components.extraction import extract
from src.components import summarizer
from src.components.file_extraction import extract_from_file,extract_from_docx


summarize_bp = Blueprint("summarize", __name__, url_prefix="/summarize")


@summarize_bp.route("/", methods=["GET"])
def summarize():
    if request.method == 'GET':
        # print(1111111111,file=sys.stderr)
        type = request.args.get("type")
        link = request.args.get("link")
        data = extract(int(type), link)
        result = summarizer.summarize(data)
        return jsonify(result)


@summarize_bp.route("/file", methods=["POST"])
def file():
    f = request.files.get('FILE')
    filename = hash_file(f.stream.read()) + "." + secure_filename(f.filename).split(".")[-1]
    print(f"Filename : {filename}",file=sys.stderr)
    f.stream.seek(0)
    f.save(os.path.join('UserFiles', filename))

    file_extn=filename.split(".")[1]
    print(file_extn, file=sys.stderr)
    # ExtractData
    if file_extn=='pdf':
        data=extract_from_file(filename)
        print(data,file=sys.stderr)
    if file_extn=='docx' or file_extn=="doc":
        data=extract_from_docx(filename)
    #print(data,file=sys.stderr)
    result = summarizer.summarize(data)
    return jsonify(result), 200
