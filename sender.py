
# this is sender side code 
import socket

#socket.af_inet---> through the internet
# socket.sock_dgram
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target_ip="192.168.135.69"

target_port=2525
target_address=(target_ip,target_port)

condition=True
while condition:

    message=input("plz enter your msg: ")
    message_encryption =message.encode('ascii')
    s.sendto(message_encryption, target_address)
    print("your message has been sent")

# for printing thank u message
    
    thanx_msg="thank you for your message"
    print(f"Received: {thanx_msg}")


    permission=input("press Y to continue message sending and N for quiting ")
    if permission=="Y":
        condition=False
