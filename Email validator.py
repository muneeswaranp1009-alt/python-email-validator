print("\n..........Python Email Validator.............\n")

def mail_val(email):
    if len(email) == 0 or ' ' in email:
        return False
    
    if email.count("@") != 1:
        return False
    
    local , domain = email.split("@")
    
    if len(local) == 0:
        return False
    
    if '.' not in domain:
        return False
    
    if domain.startswith('.') or domain.endswith('.'):
        return False
    
    return True

email = input("Enter the Email Address to Check : ")

status = "Valid" if mail_val(email) else "Invalid"
print(f"\n{email}: {status}")