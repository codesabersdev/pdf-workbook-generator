from fpdf import FPDF
import pandas as pd


class FPDF(FPDF):
    def header(self):
        # Add your header content here (e.g., logo, title)
        pass

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Set font for footer
        self.set_font('Arial', 'I', 10)
        # Display page number
        self.cell(0, 10, f'Page {self.page_no()} / {{nb}}', 0, 0, 'C')
        # page_num = self.page_no()
        # self.cell(0, 10, str(page_num), align="C")


pdf = FPDF(orientation="P", unit="mm", format="A4")
# Enable numbering on the page
pdf.alias_nb_pages()

df = pd.read_csv('topics.csv')

for index, rows in df.iterrows():
    count = 1
    for page in range(rows["Pages"]):
        pdf.add_page()
        # Styling for the Main Headings
        pdf.set_font("Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 12, txt=rows["Topic"], align="L")
        # Styling for the header page number
        pdf.set_font("Times", style="I", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 12, txt=f"Page {count} of {rows['Pages']}", align="R")
        count += 1
        # For the separator
        pdf.set_line_width(1)
        pdf.line(10, 22, 200, 22)
        # For adding page rulings --- START---
        pdf.set_line_width(0.3)
        for y in range(32, 290, 10):
            pdf.line(10, y, 200, y)
        # For adding page rulings --- END ---

pdf.output("Python Workbook.pdf")
