import socket
import json
import pandas as pd

HOST, PORT = "172.25.126.105", 8000 #assign ip address and port

#server process: initialize oscket -> bind -> listen -> accept -> recv
#cliend process: connect to the server -> send HTTP POST
count = 0
dataFrame = pd.DataFrame() #it will be updated per every incoming data from client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    while True:
        try:
            conn, addr = sock.accept() #accept incoming connection request and return socket object
            data = conn.recv(5000).decode()
            #some of incoming socekts don't bring data
            #the size of the header is fixed and using the length, we can filter header only data
            if len(data) > 259: #259 is the length of HTTP POST request header
                data = data[259:] #filter header

                # convert str into json
                my_data = json.loads(data)
                my_json = json.dumps(my_data, indent=4, sort_keys=True)
                print(my_json)

                # convert json into data frame
                frame = pd.json_normalize(my_data, record_path=["payload"])
                dataFrame = pd.concat([dataFrame,frame], ignore_index = True) #update dataFrame

                count+=1
                if count == 30:
                    break
            conn.close()
        except Exception as E:
            print(E)

dataFrame.to_csv('file.csv')