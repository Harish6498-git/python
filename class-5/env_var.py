import os

# enter the password through cli
# export password="harish" 
password = os.getenv("password")
print(password)

# export api_token="axvxhvnvugkb86nv"
api_token = os.getenv("api_token")
print(api_token)


# Environmental variables are used to excute sensitive information through cli 
# Like passwords, api_tokens, etc..