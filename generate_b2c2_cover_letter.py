from fpdf import FPDF
import datetime

# --- Setup ---
pdf = FPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_margins(25, 25, 25)
pdf.set_xy(25, 25)

# --- Add Fonts ---
# Using standard Arial for Cover Letters as it's safe and professional
pdf.add_font('Cal', '', r'C:\Windows\Fonts\calibri.ttf')
pdf.add_font('Cal', 'B', r'C:\Windows\Fonts\calibrib.ttf')
pdf.set_font('Cal', '', 11)

w = 160  # Content width

# --- Header (Applicant Info) ---
pdf.set_font('Cal', 'B', 14)
pdf.cell(w, 8, 'Apisit Saeyang', new_x="LMARGIN", new_y="NEXT", align="C")
pdf.set_font('Cal', '', 10)
pdf.cell(w, 5, 'London, United Kingdom • +44 7442 891999', new_x="LMARGIN", new_y="NEXT", align="C")
pdf.cell(w, 5, 'apisit.syp@gmail.com • linkedin.com/in/apisit-saeyang', new_x="LMARGIN", new_y="NEXT", align="C")
pdf.ln(10)

# --- Date ---
current_date = datetime.date.today().strftime("%d %B %Y")
pdf.set_font('Cal', '', 11)
pdf.cell(w, 6, current_date, new_x="LMARGIN", new_y="NEXT")
pdf.ln(4)

# --- Recipient Info ---
pdf.set_font('Cal', 'B', 11)
pdf.cell(w, 6, 'B2C2 Recruitment Team', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Cal', '', 11)
pdf.cell(w, 6, 'B2C2', new_x="LMARGIN", new_y="NEXT")
pdf.cell(w, 6, 'London, United Kingdom', new_x="LMARGIN", new_y="NEXT")
pdf.ln(6)

# --- Salutation ---
pdf.cell(w, 6, 'Dear B2C2 Recruitment Team,', new_x="LMARGIN", new_y="NEXT")
pdf.ln(4)

# --- Body Paragraphs ---
# Paragraph 1: Introduction
p1 = ("I am writing to express my strong interest in the Junior Project Manager (Summer Internship) "
      "role at B2C2. As an MSc Financial Technology student at UCL with a deep fascination for crypto "
      "market infrastructure, I have closely followed B2C2’s evolution into a global leader for institutional "
      "liquidity. I am eager to contribute my strong organisational skills, analytical mindset, and ability "
      "to bridge the gap between complex financial concepts and operational delivery.")

pdf.multi_cell(w, 5.5, p1)
pdf.ln(4)

# Paragraph 2: Project Management / Organization
p2 = ("While my background includes financial modeling and analysis, my true strength lies in structuring work, "
      "facilitating collaboration, and translating complex requirements into actionable roadmaps. During my internships "
      "at Discover Management and SCB Asset Management, I frequently acted as a bridge between analytical workflows "
      "and senior management output. I learned how to track project dependencies, coordinate across teams to ensure "
      "deadlines were met, and maintain rigorous documentation for internal review processes. These experiences taught "
      "me that successful execution requires not just technical understanding, but meticulous organization, clear "
      "communication, and relentless follow-through.")

pdf.multi_cell(w, 5.5, p2)
pdf.ln(4)

# Paragraph 3: Crypto / Tech Bridge
p3 = ("In addition to my traditional finance experience, I bring hands-on knowledge of blockchain ecosystems. Having "
      "executed thousands of on-chain transactions and studied DeFi market structure natively, I am uniquely positioned "
      "to understand the technical requirements and workflows specific to a digital assets liquidity provider like B2C2. "
      "I am highly comfortable navigating technical discussions and translating them into clear acceptance criteria, "
      "making me well-suited to support the product implementation and troubleshooting processes between Tech and Ops teams.")

pdf.multi_cell(w, 5.5, p3)
pdf.ln(4)

# Paragraph 4: Conclusion
p4 = ("A fast-paced, high-pressure environment like B2C2 is exactly where I thrive. I am genuinely eager to learn "
      "project methodologies like Agile and Scrum from experienced professionals, and I am highly motivated to ensure "
      "smooth delivery on cross-departmental initiatives. I would welcome the opportunity to bring my proactive mindset "
      "and passion for problem-solving to your Product & Delivery team.")

pdf.multi_cell(w, 5.5, p4)
pdf.ln(4)

# --- Sign-off ---
pdf.cell(w, 6, 'Thank you for considering my application. I look forward to the possibility of discussing this role further.', new_x="LMARGIN", new_y="NEXT")
pdf.ln(6)

pdf.cell(w, 6, 'Sincerely,', new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)
pdf.set_font('Cal', 'B', 11)
pdf.cell(w, 6, 'Apisit Saeyang', new_x="LMARGIN", new_y="NEXT")

# --- Output ---
output_path = r'd:\job\Apisit_Saeyang_Cover_Letter_B2C2.pdf'
pdf.output(output_path)
print(f"B2C2 Cover Letter saved to: {output_path}")
