# import os
# from twilio.rest import Client
# from dotenv import load_dotenv

# def check_otp(phone_number, otp):
#     load_dotenv()
#     account_sid = os.environ['TWILIO_ACCOUNT_SID']
#     auth_token = os.environ['TWILIO_AUTH_TOKEN']
#     verification_sid = os.environ['TWILIO_VERIFICATION_SID']
#     client = Client(account_sid, auth_token)

#     otp_verification_check = client.verify.services(verification_sid).verification_checks.create(to=phone_number, code=otp)

#     return otp_verification_check.status

# # Example usage:
# # phone_number = '+919048020515'  # Replace this with the desired phone number
# # otp_check = '153126'  # Replace this with the OTP to check
# # status = check_otp(phone_number, otp_check)
# # print(status)
