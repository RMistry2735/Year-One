import statistics

runners = []
runnerstime = []
runnercnt = 0
print("Enter the runners numbers and their times separated by two colons e.g.(123::300)\nType 'END' when you are done")
while True:
    usr_in = input()
    temp = usr_in.split("::")
    if usr_in == "END" and runnercnt == 0:
        print("No data found, nothing to do.")
        exit()
    if usr_in =="END":
        break
    elif temp[0]=="" or temp[1]=="":
        print("Error in data stream, Ignoring, Continue.")
    else:
        runners.append(int(temp[0]))
        runnerstime.append(int(temp[1]))
        runnercnt +=1

print("Total runners:",len(runners))

fst = min(runnerstime)
fstmin = int(fst/60)
fst -= (fstmin*60)
fstsec = fst
print("Fastest Time:",fstmin,"minutes,",fstsec,"seconds")

slst = max(runnerstime)
slstmin = int(slst/60)
slst -= (slstmin*60)
slstsec = slst
print("Slowest Time:",slstmin,"minutes,",slstsec,"seconds")

avg = statistics.mean(runnerstime)
avgmin = int(avg/60)
avg -= (avgmin*60)
avgsec = int(avg)
print("Average Time:",avgmin,"minutes,",avgsec,"seconds")

new_list = list(map(list, zip(runners, runnerstime)))
sorted_list = sorted(new_list, key=lambda x: x[1], reverse=False)
fst = sorted_list[0][0]
print(f"The fastest runner was #{fst}")
