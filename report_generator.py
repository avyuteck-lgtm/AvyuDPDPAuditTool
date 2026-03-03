from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib import colors

# -------- Confidential Watermark --------
def draw_watermark(c, w, h, text="CONFIDENTIAL"):
    c.saveState()

    c.setFont("Helvetica-Bold", 60)
    c.setFillColorRGB(0.85, 0.85, 0.85)  # light grey

    c.translate(w/2, h/2)
    c.rotate(45)

    c.drawCentredString(0, 0, text)

    c.restoreState()

# -------- Regulatory Risk Classification --------
def regulatory_segment(score):

    if score >= 90:
        return "Administrative Compliance"
    elif score >= 75:
        return "Regulatory Attention Required"
    elif score >= 50:
        return "High Probability of Complaint"
    else:
        return "Regulatory Enforcement Exposure"

# -------- Currency Formatter --------
def inr(amount):
    crore = amount / 10000000
    if crore >= 1:
        return f"₹{crore:.2f} Crore"

    lakh = amount / 100000
    if lakh >= 1:
        return f"₹{lakh:.2f} Lakh"

    return f"₹{amount}"


# -------- Text Wrapper --------
def split_text(text, length):
    words = text.split()
    lines = []
    current = ""

    for w in words:
        if len(current + w) < length:
            current += w + " "
        else:
            lines.append(current)
            current = w + " "

    lines.append(current)
    return lines


# -------- Main Report Generator --------
def generate_report(result, impacts, actions, filename="DPDPA_Report.pdf", org="Client Organization", auditor="Avyu Technologies OPC Pvt Ltd"):

    c = canvas.Canvas(filename, pagesize=A4)
    w, h = A4

    # ================= CERTIFICATE PAGE =================
    certificate_id = f"AVYU-DPDPA-{datetime.now().strftime('%Y%m%d%H%M')}"

    if result['score'] >= 85:
        status = "COMPLIANT"
    elif result['score'] >= 60:
        status = "PARTIALLY COMPLIANT"
    else:
        status = "HIGH RISK - NON COMPLIANT"

    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(w/2, h-120, "DPDP Compliance Risk Status Certificate")

    c.setFont("Helvetica", 14)
    c.drawCentredString(w/2, h-180, "This is to certify that")

    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(w/2, h-220, org)

    c.setFont("Helvetica", 13)
    c.drawCentredString(w/2, h-260, "has undergone Digital Personal Data Protection Act (DPDPA)")

    c.drawCentredString(w/2, h-285, "Compliance Assessment by")

    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h-315, "Avyu Technologies OPC Pvt Ltd")

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(w/2, h-370, f"STATUS: {status}")

    c.setFont("Helvetica", 14)
    score = result.get("score", 0)
    c.drawCentredString(w/2, h-410, f"Compliance Score: {score}%")

    valid_until = datetime.now().replace(year=datetime.now().year + 1)
    c.drawCentredString(w/2, h-450, f"Certificate Valid Until: {valid_until.strftime('%d %B %Y')}")

    c.setFont("Helvetica", 10)
    c.drawCentredString(w/2, 120, f"Certificate ID: {certificate_id}")

    c.drawString(70, 160, "Authorized Auditor")
    c.drawString(70, 140, "Avyu Technologies OPC Pvt Ltd")

    # Move to next page
    c.showPage()
    draw_watermark(c, w, h)

    # ================= EXECUTIVE SUMMARY PAGE =================
    y = h - 70

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "DPDPA COMPLIANCE ASSESSMENT REPORT")
    y -= 30

    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Organization: {org}")
    y -= 18
    c.drawString(50, y, f"Assessment Date: {datetime.now().strftime('%d %B %Y')}")
    y -= 18
    c.drawString(50, y, f"Audited By: {auditor}")
    y -= 30

    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Regulatory Risk Position")
    y -= 18

    segment = regulatory_segment(result['score'])
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Risk Classification: {segment}")
    y -= 30

    # Risk Assessment
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Risk Assessment")
    y -= 20

    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Compliance Score: {result['score']}%")
    y -= 15
    c.drawString(50, y, f"Risk Level: {result['risk_level']}")
    y -= 15
    c.drawString(50, y, "Potential Regulatory Penalty: Subject to adjudication by Data Protection Board of India.")
    y -= 30

    # Violations
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Key Compliance Violations")
    y -= 20

    c.setFont("Helvetica", 11)
    for v in result["violations"]:
        text = f"{v['section']} : {v['issue']}"
        for line in split_text(text, 85):
            c.drawString(60, y, "• " + line)
            y -= 15

    y -= 20

    # Business Impact
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Business Impact")
    y -= 20

    c.setFont("Helvetica", 11)
    if impacts:
        for i in impacts:
            for line in split_text(i, 85):
                c.drawString(60, y, "• " + line)
                y -= 15
    else:
        c.drawString(60, y, "• Risk of regulatory inquiry and reputational harm.")
        y -= 15

    y -= 20

    # Remediation
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Recommended Remediation Plan")
    y -= 20

    c.setFont("Helvetica", 11)

    if actions:
        for a in actions:
            c.drawString(60, y, a["action"])
            y -= 15
            for s in a["steps"]:
                c.drawString(70, y, "- " + s)
                y -= 13
            c.drawString(70, y, f"Estimated Implementation Cost: {a['cost']}")
            y -= 20
    else:
        # Auto-generate remediation from violations
        for v in result["violations"]:
            text = f"For non-compliance under {v['section']}, implement corrective controls addressing: {v['issue']}"
            for line in split_text(text, 85):
                c.drawString(60, y, "• " + line)
                y -= 15
        

    # ================= DISCLAIMER PAGE =================
    c.showPage()
    draw_watermark(c, w, h)
    y = h - 80

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Important Disclaimer")
    y -= 30

    c.setFont("Helvetica", 10)

    disclaimer = """
This report is an independent compliance assessment prepared by Avyu Technologies OPC Pvt Ltd.
The assessment is based on representations, documentation, and technical observations at the time of audit.
Regulatory authorities including the Data Protection Board of India may independently evaluate compliance.
This report does not grant statutory immunity nor replace legal advice.
"""

    for line in split_text(disclaimer, 95):
        c.drawString(50, y, line)
        y -= 14
        
    # ================= SIGNATURE BLOCK (Bottom Anchored) =================
    bottom_y = 90  # distance from bottom of page

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, bottom_y + 40, "Authorized Compliance Auditor")

    c.drawString(50, bottom_y + 20, "____________________________")

    c.setFont("Helvetica", 11)
    c.drawString(50, bottom_y, auditor)

    c.save()