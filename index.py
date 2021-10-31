import threading
import math
import random
import time
import requests
import numpy as np
from data import words

URL = "http://localhost:5000/"
wordsLength = len(words)
totalRequests = 1
totalTime = 1

def thread_function():
    print("Sending Translation request")
    st = time.time()
    print("start")
    text = words[random.randint(0, wordsLength - 1)]
    res = requests.post(URL, json = { "q": text, "source": "en", "target": "es" })
    en = time.time()
    print("Time taken")
    print(math.ceil(en * 1000) - math.ceil(st * 1000))
    print(res.json())

    #totalRequests = totalRequests + 1
    #totalTime = math.ceil(en * 1000) - math.ceil(st * 1000)

while(1):
    print("Avg Req Time")
    print(totalRequests/totalTime)
    noOfRequests = np.random.normal(4.0, 4.0)
    if(noOfRequests <= 0):
        continue
    
    noOfRequests = math.ceil(noOfRequests)
    
    noOfRequests = 1

    print("sending " + str(noOfRequests))

    threads = list()

    for index in range(noOfRequests):
        x = threading.Thread(target=thread_function)
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()

    print("Completed " + str(noOfRequests) + " successfully")

