import time
import imaplib
import email
from email.header import decode_header
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Email credentials
EMAIL_ACCOUNT = "nishantnargide@verificient.com"
EMAIL_PASSWORD = "Nishant@kal3L"  # Consider using App Password if you're using 2FA
IMAP_SERVER = "imap.gmail.com"  # For Gmail, change if using another provider
IMAP_PORT = 993


# Function to fetch OTP from the latest email, including quoted text
def get_otp_from_email():
    # Connect to the mail server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

    # Select the inbox folder
    mail.select("inbox")

    # Search for all emails (you can specify a more specific filter if needed)
    status, messages = mail.search(None, 'ALL')

    # Get the latest email
    email_ids = messages[0].split()
    latest_email_id = email_ids[-1]

    # Fetch the email by ID
    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

    # Parse the email content
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")

            # Get the email body content (assuming OTP is in the body)
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = msg.get_payload(decode=True).decode()

            # Clean up the email body to remove quoted text
            body = clean_quoted_text(body)

            # Search for the OTP in the email body (you may need to adjust this regex pattern)
            otp_match = re.search(r"Your OTP is:\s*(\d{6})", body)
            if otp_match:
                otp = otp_match.group(1)
                return otp

    return None  # If OTP is not found


# Function to clean the quoted text from email
def clean_quoted_text(body):
    # Remove quoted text by looking for lines that begin with ">" (common for replies)
    lines = body.splitlines()
    cleaned_lines = []
    for line in lines:
        if not line.startswith(">"):  # Exclude lines that start with ">"
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)






driver = webdriver.Chrome()
driver.get("https://preproduction.verificient.com/login/")
driver.maximize_window()
print(driver.title)
#Login
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("nishantnargide+electron_inst@verificient.com")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Password@12")
driver.find_element(By.XPATH,"//button[@data-callback='onSubmit']").click()
time.sleep(60)

#wait = WebDriverWait(driver,10)
#wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='col-sm-12']")))
print(driver.find_element(By.XPATH,"//div[@class='col-sm-12']").text)
time.sleep(5)




