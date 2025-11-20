
import time 


secret_key = 123456 

def generate_otp(): 
    return str((int(time.time()) + secret_key) % 1000000).zfill(6) 


password = input("Enter your password: ") 
if password == "12345": 
    otp = generate_otp() 
    print(f"Your OTP is: {otp}") 
    user_otp = input("Enter the OTP: ") 
    if user_otp == otp: 
        print("Authentication complete.") 
    else: 
        print("Invalid OTP.") 
else: 
    print("Incorrect password.")
