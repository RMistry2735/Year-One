def runners(runners):
    runners.sort(key=lambda x: x[1])
    total = 0
    for run, time in runners:
        total = total +int(time)

    avgtime = total // len(runners)
    srunner = max(runners, key=lambda x: x[1])
    frunner = min(runners, key=lambda x: x[1])

    return avgtime, srunner, frunner


runnerlist = []
print("Enter runner number and time in the following format ---> 'runner number::time in seconds'")
print("Type \"End\" once all values have been entered")
while True:
    runnertime = input()
    temp = runnertime.split("::")
    listlength = len(temp)
    if runnertime == "END":
        if not runnerlist:
            print("No data found")
        else:
            avg, fastest, slowest = runners(runnerlist)
            break
    elif listlength != 2 or temp[0] == "" or temp[1] == "":
        print("Error in data stream. Ignorning. Carry on.")
    else:
        runnerlist.append(temp)

print("Total Runners: " + str(len(runnerlist)))

seconds = avg % (24 * 3600)
minutes = seconds // 60
seconds %= 60
print(f"Average Time: {minutes} minutes, {seconds} seconds")

seconds = int(fastest[1]) % (24 * 3600)
mintues = seconds // 60
seconds %= 60
print(f"Slowest Time: {minutes} minutes, {seconds} seconds")

seconds = int(slowest[1]) % (24 * 3600)
mintues = seconds // 60
seconds %= 60
print(f"Fastest Time: {minutes} minutes, {seconds} seconds")
