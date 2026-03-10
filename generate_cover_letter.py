from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(auto=True, margin=25)
pdf.add_page()
pdf.set_margins(30, 25, 30)

# Use DejaVu for Unicode support
pdf.add_font('DejaVu', '', r'C:\Windows\Fonts\times.ttf', uni=True)
pdf.add_font('DejaVu', 'B', r'C:\Windows\Fonts\timesbd.ttf', uni=True)

# --- Sender Info ---
pdf.set_xy(30, 25)
pdf.set_font('DejaVu', 'B', 12)
pdf.cell(0, 6, 'Apisit Saeyang', new_x="LMARGIN", new_y="NEXT")

pdf.set_font('DejaVu', '', 11)
pdf.cell(0, 5.5, 'London, United Kingdom', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.5, '+44 7442 891999', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.5, 'apisit.syp@gmail.com', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.5, 'LinkedIn: Apisit Saeyang', new_x="LMARGIN", new_y="NEXT")

pdf.ln(6)

# --- Date ---
pdf.cell(0, 5.5, '9 March 2026', new_x="LMARGIN", new_y="NEXT")
pdf.ln(6)

# --- Recipient ---
pdf.cell(0, 5.5, 'Hiring Manager', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.5, 'Nomura', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.5, 'London, United Kingdom', new_x="LMARGIN", new_y="NEXT")

pdf.ln(8)

# --- Salutation ---
pdf.cell(0, 5.5, 'Dear Hiring Manager,', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

# --- Body ---
lh = 5.8
w = 150

para1 = (
    "I\u2019d like to apply for the Product Manager \u2013 Digital Solutions role at Nomura."
)
pdf.multi_cell(w, lh, para1)
pdf.ln(4)

para2 = (
    "My background is in finance. I interned in investment banking and equity research "
    "in Bangkok, and honestly, I enjoyed the analytical side, but what kept drawing my "
    "attention was the technology side. I started getting into blockchain and digital "
    "assets back in 2021, not from an academic angle, but by actually using the products. "
    "Trading on-chain, navigating DeFi protocols, and figuring out how things like "
    "liquidity, collateral, and settlement work in practice across different networks. "
    "Over time, that curiosity turned into something more serious."
)
pdf.multi_cell(w, lh, para2)
pdf.ln(4)

para3 = (
    "That\u2019s a big part of why I chose to do my MSc in Financial Technology at UCL. "
    "The programme gave me the chance to study things like DLT, blockchain technologies, "
    "machine learning, innovation and strategy in finance in a structured way, and have "
    "a chance to connect with the real builders and researchers in the DLT seminar course, "
    "combining them back to the institutional finance world I already knew. It helped me "
    "think about where these technologies actually fit within capital markets, not just "
    "where people hope they will."
)
pdf.multi_cell(w, lh, para3)
pdf.ln(4)

para4 = (
    "What draws me to Nomura is that the firm seems to be asking the same question: "
    "how do you take emerging technologies and turn them into real infrastructure for "
    "institutional clients? That\u2019s the kind of problem I want to work on, and I think "
    "having both the finance foundation and genuine experience in the digital asset space "
    "puts me in a good position to contribute to the Digital Solutions team."
)
pdf.multi_cell(w, lh, para4)
pdf.ln(4)

para5 = "Thanks for your time. I\u2019d be happy to discuss further."
pdf.multi_cell(w, lh, para5)

pdf.ln(8)

# --- Closing ---
pdf.cell(0, 5.5, 'Best regards,', new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)
pdf.set_font('DejaVu', 'B', 11)
pdf.cell(0, 5.5, 'Apisit Saeyang', new_x="LMARGIN", new_y="NEXT")

# --- Output ---
output_path = r'd:\job\Apisit_Saeyang_Cover_Letter.pdf'
pdf.output(output_path)
print(f"Cover letter saved to: {output_path}")
