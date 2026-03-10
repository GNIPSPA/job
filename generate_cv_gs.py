from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(auto=False)
pdf.add_page()
pdf.set_margins(20, 15, 20)
pdf.set_xy(20, 15)

pdf.add_font('Cal', '', r'C:\Windows\Fonts\calibri.ttf')
pdf.add_font('Cal', 'B', r'C:\Windows\Fonts\calibrib.ttf')
pdf.add_font('Cal', 'I', r'C:\Windows\Fonts\calibrii.ttf')

w = 170

# ============================
# HEADER
# ============================
pdf.set_font('Cal', 'B', 15)
pdf.cell(w, 7, 'Apisit Saeyang', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Cal', '', 9.5)
pdf.cell(w, 5, 'London, United Kingdom | Tel: +44 7442 891999 | Email: apisit.syp@gmail.com | LinkedIn: Apisit Saeyang', new_x="LMARGIN", new_y="NEXT")

pdf.ln(4)

# ============================
# EDUCATION
# ============================
pdf.set_font('Cal', 'B', 12)
pdf.cell(w, 6, 'EDUCATION', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

pdf.set_font('Cal', 'B', 10)
label = 'MSc Financial Technology (FinTech)'
lw = pdf.get_string_width(label)
pdf.cell(lw, 5, label, new_x="END")
pdf.set_font('Cal', '', 10)
pdf.cell(w - lw, 5, ', University College London (UCL) | 2025\u20132026 (Expected)', new_x="LMARGIN", new_y="NEXT")
pdf.ln(1.5)

pdf.set_font('Cal', 'B', 10)
label2 = 'BBA in Finance'
lw2 = pdf.get_string_width(label2)
pdf.cell(lw2, 5, label2, new_x="END")
pdf.set_font('Cal', '', 10)
pdf.cell(w - lw2, 5, ', Assumption University of Thailand | Graduated 2024', new_x="LMARGIN", new_y="NEXT")

pdf.ln(5)

# ============================
# EXPERIENCE
# ============================
pdf.set_font('Cal', 'B', 12)
pdf.cell(w, 6, 'EXPERIENCE', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

# --- Discover Management ---
pdf.set_font('Cal', 'B', 10)
pdf.multi_cell(w, 5, 'Investment Banking Intern \u2014 Discover Management (Bangkok, Thailand | Nov 2024 \u2013 Jan 2025)')

bullets_dm = [
    "Reviewed client and public company disclosures and financial statements, extracting and structuring key company, financial, and market data to support valuation analysis and internal review processes.",
    "Assisted in building and reviewing financial and valuation models (DCF, trading & transaction comparables).",
    "Conducted market, industry, and company analysis, translating insights into structured recommendations for senior team members.",
    "Supported preparation of investment memoranda and pitch decks.",
]

pdf.set_font('Cal', '', 9.5)
for b in bullets_dm:
    pdf.set_x(22)
    pdf.multi_cell(w - 2, 4.8, '- ' + b)
    pdf.ln(0.5)

pdf.ln(3)

# --- SCB Asset Management ---
pdf.set_font('Cal', 'B', 10)
pdf.multi_cell(w, 5, 'Equity Research Intern (Buy-Side) \u2014 SCB Asset Management (Bangkok, Thailand | Apr 2024 \u2013 May 2024)')

bullets_scb = [
    "Initiated coverage and conducted earnings reviews for SET-listed companies, building financial models and presenting insights to fund managers.",
    "Supported senior analysts on ongoing coverage, contributing to investment presentations and research materials.",
    "Attended management meetings, analyst briefings, and industry forums, gaining exposure to institutional research workflows.",
    "Assisted with proxy voting and stewardship activities.",
]

pdf.set_font('Cal', '', 9.5)
for b in bullets_scb:
    pdf.set_x(22)
    pdf.multi_cell(w - 2, 4.8, '- ' + b)
    pdf.ln(0.5)

pdf.ln(5)

# ============================
# PROJECTS
# ============================
pdf.set_font('Cal', 'B', 12)
pdf.cell(w, 6, 'PROJECTS', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

# --- CFA Research Challenge ---
pdf.set_font('Cal', 'B', 10)
pdf.cell(w, 5, 'CFA Institute Research Challenge | 2025', new_x="LMARGIN", new_y="NEXT")

pdf.set_font('Cal', '', 9.5)
pdf.set_x(22)
pdf.multi_cell(w - 2, 4.8, '- Led a team in a global equity research competition, conducting in-depth company analysis, financial modeling, valuation, and investment thesis development under CFA Institute standards.')
pdf.ln(2)

# --- CMCC ---
pdf.set_font('Cal', 'B', 10)
pdf.cell(w, 5, 'Capital Market Case Competition (CMCC) \u2014 First Runner-Up (Jun 2024 \u2013 Aug 2024)', new_x="LMARGIN", new_y="NEXT")

bullets_cmcc = [
    "Led the team to evaluate M&A targets and designed fundraising and digital incentive strategies for a listed media company (ONEE).",
    "Delivered an end-to-end investment and strategy pitch covering valuation logic, execution roadmap, and stakeholder impact.",
]

pdf.set_font('Cal', '', 9.5)
for b in bullets_cmcc:
    pdf.set_x(22)
    pdf.multi_cell(w - 2, 4.8, '- ' + b)
    pdf.ln(0.5)

pdf.ln(2)

# --- Blockchain ---
pdf.set_font('Cal', 'B', 10)
pdf.cell(w, 5, 'Blockchain & Digital Asset Ecosystems (2021 \u2013 Present)', new_x="LMARGIN", new_y="NEXT")

bullets_bc = [
    "Hands-on experience across distributed ledger and blockchain ecosystems, including EVM-based networks, non-EVM architectures, and Bitcoin.",
    "Executed 10,000+ on-chain transactions across DeFi protocols and developed practical understanding of crypto market structure, liquidity, and incentive dynamics.",
]

pdf.set_font('Cal', '', 9.5)
for b in bullets_bc:
    pdf.set_x(22)
    pdf.multi_cell(w - 2, 4.8, '- ' + b)
    pdf.ln(0.5)

pdf.ln(5)

# ============================
# SKILLS
# ============================
pdf.set_font('Cal', 'B', 12)
pdf.cell(w, 6, 'SKILLS', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

skills = [
    ("Finance & Valuation: ", "Financial modeling (DCF, trading & transaction comparables), equity research, capital markets, M&A analysis, scenario & sensitivity analysis, monte carlo simulation"),
    ("FinTech & Digital Assets: ", "Distributed ledger technology (DLT) & blockchain fundamentals, tokenomics & incentive design, DeFi market structure, crypto market structure, liquidity & incentive dynamics"),
    ("Tools: ", "Excel (advanced financial models), PowerPoint (investment decks), Python (basic), Solidity (basic), AI-assisted analytical workflows"),
    ("Languages: ", "Thai (Native), English (Professional Working Proficiency), Mandarin Chinese (Basic Conversational)"),
]

for label, content in skills:
    # First line: bold label + start of content
    pdf.set_font('Cal', 'B', 9.5)
    label_w = pdf.get_string_width(label)
    pdf.cell(label_w, 5, label, new_x="END")
    pdf.set_font('Cal', '', 9.5)
    remaining_w = w - label_w
    content_w = pdf.get_string_width(content)
    if content_w <= remaining_w:
        pdf.cell(remaining_w, 5, content, new_x="LMARGIN", new_y="NEXT")
    else:
        # Split content: what fits on first line, rest on next line from left margin
        words = content.split(' ')
        first_line = ''
        rest_words = []
        for i, word in enumerate(words):
            test = first_line + (' ' if first_line else '') + word
            if pdf.get_string_width(test) <= remaining_w - 2:
                first_line = test
            else:
                rest_words = words[i:]
                break
        pdf.cell(remaining_w, 5, first_line, new_x="LMARGIN", new_y="NEXT")
        if rest_words:
            rest_text = ' '.join(rest_words)
            pdf.set_x(20)
            pdf.multi_cell(w, 5, rest_text)
    pdf.ln(1.5)

# --- Output ---
output_path = r'd:\job\CV_Apisit_Saeyang_GS.pdf'
pdf.output(output_path)
print(f"CV saved to: {output_path}")
print(f"Page height used: ~{pdf.get_y():.1f}mm out of 297mm")
