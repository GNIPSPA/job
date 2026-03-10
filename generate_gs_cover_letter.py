from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(auto=True, margin=25)
pdf.add_page()
pdf.set_margins(30, 25, 30)

pdf.add_font('TNR', '', r'C:\Windows\Fonts\times.ttf')
pdf.add_font('TNR', 'B', r'C:\Windows\Fonts\timesbd.ttf')

# --- Sender Info ---
pdf.set_xy(30, 25)
pdf.set_font('TNR', 'B', 12)
pdf.cell(0, 6, 'Apisit Saeyang', new_x="LMARGIN", new_y="NEXT")

pdf.set_font('TNR', '', 11)
pdf.cell(0, 5.5, 'London, United Kingdom', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.5, '+44 7442 891999', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.5, 'apisit.syp@gmail.com', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.5, 'LinkedIn: Apisit Saeyang', new_x="LMARGIN", new_y="NEXT")

pdf.ln(6)

# --- Date ---
pdf.cell(0, 5.5, '10 March 2026', new_x="LMARGIN", new_y="NEXT")
pdf.ln(6)

# --- Recipient ---
pdf.cell(0, 5.5, 'Hiring Manager', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.5, 'Goldman Sachs', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5.5, 'London, United Kingdom', new_x="LMARGIN", new_y="NEXT")

pdf.ln(8)

# --- Salutation ---
pdf.cell(0, 5.5, 'Dear Hiring Manager,', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

# --- Body ---
lh = 5.8
w = 150

para1 = (
    "I'd like to apply for the Digital Assets Tokenisation Analyst role "
    "at Goldman Sachs."
)
pdf.multi_cell(w, lh, para1)
pdf.ln(4)

para2 = (
    "My background is in finance. I interned in investment banking and equity "
    "research in Bangkok, and honestly, I enjoyed the analytical side, but what "
    "kept drawing my attention was the technology side. I started getting into "
    "blockchain and digital assets back in 2021, not from an academic angle, but "
    "by actually using the products. Trading on-chain, navigating DeFi protocols, "
    "and figuring out how things like liquidity, collateral, and settlement work "
    "in practice across different networks. Over time, that curiosity turned into "
    "something more serious."
)
pdf.multi_cell(w, lh, para2)
pdf.ln(4)

para3 = (
    "That's a big part of why I chose to do my MSc in Financial Technology at UCL. "
    "The programme gave me the chance to study things like DLT, blockchain "
    "technologies, machine learning, and innovation in finance in a structured way, "
    "and have a chance to connect with the real builders and researchers in the DLT "
    "seminar course, combining them back to the institutional finance world I already "
    "knew. It helped me think about where tokenisation and digital asset infrastructure "
    "actually fit within capital markets, not just where people hope they will."
)
pdf.multi_cell(w, lh, para3)
pdf.ln(4)

para4 = (
    "What draws me to Goldman Sachs is that the firm is clearly building real "
    "capability in digital assets, not just experimenting. The opportunity to work "
    "on tokenisation within Global Markets, at the intersection of traditional "
    "finance and blockchain, is exactly the kind of role where I think my "
    "combination of hands-on crypto experience and institutional finance background "
    "can add value."
)
pdf.multi_cell(w, lh, para4)
pdf.ln(4)

para5 = "Thanks for your time. I'd be happy to discuss further."
pdf.multi_cell(w, lh, para5)

pdf.ln(8)

# --- Closing ---
pdf.set_font('TNR', '', 11)
pdf.cell(0, 5.5, 'Best regards,', new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)
pdf.set_font('TNR', 'B', 11)
pdf.cell(0, 5.5, 'Apisit Saeyang', new_x="LMARGIN", new_y="NEXT")

# --- Output ---
output_path = r'd:\job\Apisit_Saeyang_Cover_Letter_GS.pdf'
pdf.output(output_path)
print(f"Cover letter saved to: {output_path}")
