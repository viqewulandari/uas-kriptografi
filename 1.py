import random
import base64
import string

def generate_captcha():
  # Generate random number with 10 digits
  random_num = ''.join(str(random.randint(0,9)) for i in range(10))
  
  # Encode random number in base64 
  random_b64 = base64.b64encode(random_num.encode('utf-8')).decode('utf-8')

  # Take first 10 characters from left
  captcha = random_b64[:10]

  return captcha

captcha = generate_captcha()
print(captcha)