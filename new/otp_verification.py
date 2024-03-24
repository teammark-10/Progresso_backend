# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Set environment variables for your credentials
# Read more at http://twil.io/secure
class verification:
    load_dotenv()
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    verification_sid = os.environ['TWILIO_VERIFICATION_SID']
    client = Client(account_sid, auth_token)
    def sent_otp(number):
        verified_number=number
        veri = verification.client.verify.v2.services(verification.verification_sid) \
        .verifications \
        .create(to=verified_number, channel="sms")
        return veri.status

    def verify_otp(number, otp):
        otp_code = otp
        verified_number = number
        verification_check = verification.client.verify.v2.services(verification.verification_sid) \
        .verification_checks \
        .create(to=verified_number, code=otp_code)
        return verification_check.status
    
# print(verification.verify_otp("+919048020515","655680"))
# print(verification.sent_otp("+919048020515"))