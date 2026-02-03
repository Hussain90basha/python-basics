environment = "PROD"
change_ticket = False

if environment == "PROD":
    change_ticket = True
    print("Please provide a change ticket")
elif environment == "Staging":
    print("Welcome to staging environment")    
else:
    print("Please login with your crendentials")    
