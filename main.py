from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, rows in df.iterrows():
    pdf.add_page()
    pdf.set_font("Helvetica", style="B", size=22)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 12, txt=rows["Topic"], ln=1, align="L")
    pdf.line(10, 21, 200, 21)

pdf.output("test.pdf")
