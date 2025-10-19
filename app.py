from flask import Flask, request, send_file
from PyPDF2 import PdfMerger
import os

app = Flask(_name_)

@app.route('/')
def home():
    return "✅ Editsome Backend Running!"

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    files = request.files.getlist("files")
    merger = PdfMerger()
    for f in files:
        merger.append(f)
    output_path = "merged.pdf"
    merger.write(output_path)
    merger.close()
    return send_file(output_path, as_attachment=True)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
