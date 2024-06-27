numOfProcess=int(input("Enter Number of processes:"))
#asking user the number of processes
burstList=[]#
#creating a empty list
#using for loop to get input of burst time upto no. of process time.
for i in range(numOfProcess):
    burstTime = int(input(f"Enter the burst time for process {i+1}:"))
    #taking input from user for every process's burst time.
    burstList.append(burstTime)
print("This is the burst time given by user",burstList)
    #appending data into the list

#Calculating the average waiting time
waitingList=[0,]
#creating with 0 in the list because waiting time will be 0 for the 1st
waitingTime=0
for j in range(1,numOfProcess):
    waitingTime+=burstList[j-1]
    waitingList.append(waitingTime)
print("This list is containing Waiting time of processes",waitingList)
sum=0
for k in waitingList:
    sum+=k
AverageWaitingTime=sum/len(waitingList)

#TAT = Burst time + Waiting time hence followed the pattern to get the end result
turnAroundList=[]
turnAroundTime=0
for l in range(0,numOfProcess):
    turnAroundTime+=burstList[l]
    turnAroundList.append(turnAroundTime)
print("This list is containing turnAroundtime of processes",turnAroundList)
tat=0
for m in turnAroundList:
    tat+=m
AverageTurnaroundTime=tat/len(turnAroundList)

#Answers of the questions
print("The average waiting time is",AverageWaitingTime)
print("The average turnaroundtime is",AverageTurnaroundTime)







