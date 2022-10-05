import time
start_time = time.time()

a=0
while a<=10000:
    print(a , end="  ")
    a+=1

print("--- %s seconds ---" % (time.time() - start_time))