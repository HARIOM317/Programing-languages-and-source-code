# import cv2
# import numpy as np
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=16)

fd = open("Text.txt", 'r')

for i in fd:
    pdf.cell(200, 10, txt=i, ln=1, align='C')

pdf.output("Test_PDF.pdf")



