from fpdf import FPDF

def create_report(name,disease,result,risk):

    pdf=FPDF()

    pdf.add_page()

    pdf.set_font("Arial",size=16)

    pdf.cell(200,10,"AI Health Report",ln=True)

    pdf.cell(200,10,"Name: "+name,ln=True)

    pdf.cell(200,10,"Disease: "+disease,ln=True)

    pdf.cell(200,10,"Risk: "+str(risk)+"%",ln=True)

    pdf.cell(200,10,"Result: "+result,ln=True)

    file=name+"_report.pdf"

    pdf.output(file)

    return file