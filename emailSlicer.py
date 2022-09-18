

def main():
    print("Welcome to the email slicer")
    print("")
    
    emailInput = input("Input your email address: ")
    
    (username, domain) = emailInput.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username : ", username)
    print("Domain: ", domain)
    print("Extension : ", extension)

main()  