import statistics

runners = []
runnersTime = []
runnerCount = 0
print("Enter the runners numbers and their times separated by two colons e.g.(123::300)")
print("Type 'END' when you are done")
while True:
    usr_in = input()
    temp = usr_in.split("::")
    if usr_in == "END" and runnerCount == 0:
        print("No data found, nothing to do.")
        exit()
    if usr_in =="END":
        break
    elif temp[0]=="" or temp[1]=="":
        print("Error in data stream, Ignoring, Continue.")
    else:
        runners.append(int(temp[0]))
        runnersTime.append(int(temp[1]))
        runnerCount +=1

print("Total runners:",len(runners))

fastest = min(runnersTime)
fastestmin = int(fastest/60)
fastest -= (fastestmin*60)
fastestsec = fastest
print("Fastest Time:",fastestmin,"minutes,",fastestsec,"seconds")

slowest = max(runnersTime)
slowestmin = int(slowest/60)
slowest -= (slowestmin*60)
slowestsec = slowest
print("Slowest Time:",slowestmin,"minutes,",slowestsec,"seconds")

avg = statistics.mean(runnersTime)
avgmin = int(avg/60)
avg -= (avgmin*60)
avgsec = int(avg)
print("Average Time:",avgmin,"minutes,",avgsec,"seconds")

new_list = list(map(list, zip(runners, runnersTime)))
sorted_list = sorted(new_list, key=lambda x: x[1], reverse=False)
fastest = sorted_list[0][0]
print(f"The fastest runner was #{fastest}")
