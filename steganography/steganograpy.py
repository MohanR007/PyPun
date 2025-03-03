from stegano import lsb
# text = str(input("Enter the secret : "))
# secret = lsb.hide("1.jpg",text)
# secret.save("secret.png")


secret_message = lsb.reveal("secret.png")
print(secret_message)