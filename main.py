from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

class ContactForm(BaseModel):
    name: str
    email: str
    message: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

def send_email(name: str, email: str, message: str):
    try:
        # Email configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "workwithfusioncode@gmail.com"
        sender_password = "dcqo froc hfso mijv"  # Replace with Gmail App Password
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email
        msg['Subject'] = f"New Contact Form Message from {name}"
        
        body = f"""
New message from Fusion website:

Name: {name}
Email: {email}
Message: {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

@app.post("/contact")
async def contact(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    # Send email192.
    email_sent = send_email(name, email, message)
    
    if email_sent:
        return {"status": "success", "message": "Thank you for your message! We'll get back to you soon."}
    else:
        return {"status": "error", "message": "Failed to send message. Please try again."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
