from docx import Document
from docx2pdf import convert
from datetime import datetime
import os
import re


def result_generation(data):
    document = Document()

    p = document.add_paragraph()
    p = p.insert_paragraph_before("                    ")
    r = p.add_run()
    r.add_picture("report_logo.jpeg")

    ID = open("assets/ID.txt", "r").read()
    now = datetime.now()
    DateAndTime = now.strftime("%d/%m/%Y %H:%M:%S")

    updated_ID = int(ID) + 1
    update = open("assets/ID.txt", "w")
    update.write(str(updated_ID))
    update.close()

    section = document.sections[0]
    header = section.header
    paragraph = header.paragraphs[0]
    paragraph.text = (
        "ID:"
        + str("{num:0>4}".format(num=str(ID)))
        + " Generated at : "
        + str(DateAndTime)
    )
    paragraph.style = document.styles["Header"]

    document.add_heading("Results", 0)

    document.add_heading("Content Extracted")
    document.add_paragraph("Type : " + data["type"])
    document.add_paragraph(
        "Upload Date : " + str(data["start_time"].strftime("%d/%m/%Y"))
    )
    document.add_paragraph(
        "Upload Time : " + str(data["start_time"].strftime("%H:%M:%S"))
    )

    document.add_heading("Execution Time")
    document.add_paragraph("Extraction : " + str(data["extraction_time"]) + " seconds")
    document.add_paragraph(
        "Summarization : " + str(data["summarizer_time"]) + " seconds"
    )

    document.add_page_break()

    document.add_heading("Report", 0)
    document.add_heading("Content Extracted", 1)
    document.add_paragraph(data["content"])

    document.add_heading("Summary Generated", 1)
    document.add_paragraph(data["summary"])

    document.add_heading("Title Generated", 1)
    document.add_paragraph(data["title"])
    document.add_paragraph(
        "======================================================================"
    )

    doc_location = "temp\Result_{num:0>4}.docx".format(num=str(ID))
    document.save(doc_location)
    convert(doc_location, output_path="temp")
    os.remove(doc_location)
