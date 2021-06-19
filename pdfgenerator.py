import os

from fpdf import FPDF

img_dir = 'screenshot'
img_path = os.path.join(os.getcwd(), img_dir)

report_dir = 'report'
report_path = os.path.join(os.getcwd(), report_dir)

resource_dir = os.path.join(os.getcwd(),'resource_dir')
resource_comp_logo_path = os.path.join(resource_dir, 'ie_comp_logo.png')


# class PDF(FPDF):
#     def header(self):
#         # Logo
#         self.image(resource_comp_logo_path, 10, 8, 33)
#         # Arial bold 15
#         self.set_font('Arial', 'B', 15)
#         # Move to the right
#         self.cell(80)
#         # Title
#         self.cell(30, 10, 'Sonicwall-Report', 1, 0, 'C')
#         # Line break
#         self.ln(20)
#
#     # Page footer
#     def footer(self):
#         # Position at 1.5 cm from bottom
#         self.set_y(-15)
#         # Arial italic 8
#         self.set_font('Arial', 'I', 8)
#         # Page number
#         self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


pdf = FPDF('L', 'mm', 'A4')
pdf.set_auto_page_break(0)
for filename in os.listdir(img_path):
    filename = os.path.join(img_path, filename)
    print(filename)
    pdf.add_page()
    pdf.image(filename, 0, 0, 210, 297)
pdf.output(os.path.join(report_path, "Sonicwall.pdf"))
