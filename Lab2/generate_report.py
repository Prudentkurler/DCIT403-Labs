from docx import Document
import os

def create_report():
    document = Document()
    document.add_heading('Lab 2: Sensor Agent Report', 0)

    document.add_heading('1. SensorAgent Code', level=1)
    document.add_paragraph('The SensorAgent is implemented using the SPADE library. It periodically polls the DisasterEnvironment to detect events.')
    document.add_paragraph('Key components:')
    document.add_paragraph('• SensingBehaviour: A Cyclic/Periodic behaviour that calls environment.get_environment_state().', style='List Bullet')
    document.add_paragraph('• Logic: Logs detected events to a file and prints them to console.', style='List Bullet')
    
    document.add_heading('2. Explanation of Percepts', level=1)
    document.add_paragraph('The agent perceives the following attributes from the environment:')
    document.add_paragraph('• Type: The classification of the disaster (e.g., fire, flood).', style='List Bullet')
    document.add_paragraph('• Severity: The intensity of the event (low, medium, high, critical).', style='List Bullet')
    document.add_paragraph('• Location: The (x, y) coordinates where the event occurred.', style='List Bullet')
    document.add_paragraph('• Timestamp: The time at which the event was generated.', style='List Bullet')
    
    document.add_heading('3. Event Logs', level=1)
    document.add_paragraph('Below is a sample of the events detected and logged by the agent:')
    
    log_path = 'event_log.txt'
    try:
        with open(log_path, 'r') as f:
            logs = f.read()
            # Add logs in a monospace font style if possible, or just as paragraph
            p = document.add_paragraph(logs)
            p.style = 'No Spacing' 
    except FileNotFoundError:
        document.add_paragraph(f"Error: {log_path} not found.")

    document.save('Lab2_Report.docx')
    print("Report generated: Lab2_Report.docx")

if __name__ == "__main__":
    create_report()
