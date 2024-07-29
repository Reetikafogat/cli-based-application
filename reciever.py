# this is recievers side code 
import socket
from datetime import datetime
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_address="192.168.135.69"
port_no=2525

complete_address=(ip_address, port_no)
s.bind(complete_address)

print("hey i am listening")

while True: 
    data,address=s.recvfrom(100)
    # creating a file where we want to write the message with current time and date 
    
    your_ip=address[0]
    file=open(your_ip + '.txt','a')
    your_msg =data.decode('ascii')
    date=datetime.now()
    dt=str(date )
    message_with_date_n_time=f"{{'the message with current date and time :',{date}}} :{your_msg }"
    file.write(message_with_date_n_time )
    print(message_with_date_n_time)
    file.close()

    # thank u message

    sender_address=data[1]
    thanx_msg="thank you for your message"
    s.sendto(thanx_msg.encode('ascii'),address)
    
    