import threading
import math
import time
import requests
import numpy as np

URL = "http://18.206.235.40:5000/translate"

def thread_function():
    print("Sending Translation request")
    res = requests.post(URL, json = { "q": "Hello World", "source": "en", "target": "es" })
    print(res.json())

while(1):
    noOfRequests = np.random.normal(4.0, 4.0)
    if(noOfRequests <= 0):
        continue
    
    noOfRequests = math.ceil(noOfRequests)

    print("sending " + str(noOfRequests))

    threads = list()
    noOfRequests = 1
    for index in range(noOfRequests):
        x = threading.Thread(target=thread_function)
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()

    print("Completed " + str(noOfRequests) + " successfully")

