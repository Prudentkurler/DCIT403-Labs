from docx import Document
from docx.shared import Inches

def create_report():
    document = Document()
    document.add_heading('Lab 1: Environment Setup Report', 0)

    document.add_heading('1. Introduction', level=1)
    document.add_paragraph(
        'This report documents the setup of the development environment for the agent-based systems lab via XMPP. '
        'The environment consists of a local XMPP server (Prosody) running in a Docker container and a Python-based agent using the SPADE library.'
    )

    document.add_heading('2. System Components', level=1)
    document.add_paragraph(
        'The following components were successfully installed and configured:'
    )
    document.add_paragraph(
        '• XMPP Server: Prosody (running via Docker)', style='List Bullet'
    )
    document.add_paragraph(
        '• Agent Library: SPADE (Smart Python Agent Development Environment)', style='List Bullet'
    )
    document.add_paragraph(
        '• Programming Language: Python 3.14', style='List Bullet'
    )

    document.add_heading('3. Setup Verification', level=1)
    document.add_paragraph(
        'The Docker container for Prosody is up and running, exposing port 5222 for client connections. '
        'The Basic Agent script was configured to connect to "localhost" on port 5222 using the JID "basic_agent@localhost".'
    )

    document.add_paragraph(
        'Connection testing confirmed that the agent can authentication with the server. '
        'The container logs indicate the server is active and accepting connections.'
    )

    document.add_heading('4. Conclusion', level=1)
    document.add_paragraph(
        'The environment is fully operational and ready for Lab 2 implementation.'
    )

    document.save('Lab1_Report.docx')
    print("Report generated successfully: Lab1_Report.docx")

if __name__ == "__main__":
    create_report()
