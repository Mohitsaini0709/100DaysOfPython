# Check The Message Will Be Spam Or not

m1 = "Pay Now"
m2 = "Subscribe Now"
m3 = "Click Here "
m4 = "Buy Now "
m5 = "Make More Money Now "

message = input("Entre Your Message :")

if (m1 in message or m2 in message or m3 in message or m4 in message or m5 in message ):
    print("This Message Is A Spam")
else:
   print("This Message Is Not A Spam")