import main
import time

def analyzer(data):
    count = 0
    for i in data:
        count += i
    count /= len(data)



start_time = time.time()
data = []

while True:
    current_time = time.time()
    
    if current_time - start_time >= 30:
        total_count = analyzer(data)
        #call another function that will initialize neural network 
        start_time = time.time()
        continue