'''
The given question can be solved by simple backtracking and ordering of variables.

First, the adjacent-state file is read and an adjacency dictionary is created.

Then we determine appropriate frequency with respect to each state and store in solution dictionary: freqdict

The method "assign" recursively calls itself and to find the possible frequency for next state. If this fails it back tracks to previous known state..

The method "check" checks if current a particular frequency can be assigned to a state without violating any constraints.

If a frequency assignment for a state is determined safe by "check" function, then that frequency is assigned to the state by "assign" function.
If no frequencies can be allotted to a particular state, the "assign" function backtracks to last valid assignment.
When all states have being assigned frequencies, the program stops and displays total number of backtracks and final output is saved in a text file.

However, in case of legacy systems, these states are preassigned frequencies and we find appropriate frequencies for the other states only.

To make this more efficient, the order of states is predetermined such that most constraining states are selected first. In other words, states with more neighbours are selected before states with lesser neighbours. To do this, states are sorted in decreasing number of neighbours.
Only this improvement is enough to solve the NP-hard problem in efficient time.



'''
import sys
__author__ = 'tejashree'
def check(state,freq):#check for validity of assignment
    adjacent=addjacentdict[state]
    for i in adjacent:
        if i in freqdict:
            if freqdict[i]==freq:
                return False
    return True

def assign(k):#recursive function
    global backtrack, foundsolution, finalanswer
    for i in radiofreq:
        if check(stateslist[k],i):
            freqdict[stateslist[k]]=i
            if k+1<len(stateslist):
                assign(k+1)#recursive part of function
            else:#base function starts here
                for key,value in sorted(freqdict.items()):
                    finalanswer=finalanswer+key+" "+value+"\n"
                foundsolution=True
                raise MyError()#base function ends here
        elif i==radiofreq[-1]:
            backtrack=backtrack+1;

class MyError(Exception):
    pass

if __name__ == "__main__":
    backtrack=0
    finalanswer=""
    foundsolution=False
    #creation of adacency dictionary starts here
    adjacentfile=open("adjacent-states","r")
    states=adjacentfile.readlines()
    adjacentlist=[]
    for i in states:
        i=i.rstrip("\n")
        info=i.split(" ")
        adjacentlist.append(info)
    addjacentdict={};
    for i in adjacentlist:
        addjacentdict[i[0]] = i[1:]
    #creation of adacency dictionary ends here
    freqdict={}
    radiofreq=["A","B","C","D"]
    #presorting of variables i.e states starts here
    stateslist= addjacentdict.keys()
    statesort=[]
    for i in stateslist:
          statesort.append([i,len(addjacentdict[i])])
    statesort=sorted(statesort,key=lambda student: student[1],reverse=True)
    stateslist=[x[0] for x in statesort]
    #presorting of variables i.e states ends here
    #Legacy system management start here
    f=[]
    for arg in sys.argv:
        f.append(arg)
    constraints=open(f[1],"r")
    con=constraints.readlines()
    constates=[]
    for i in con:
        i=i.rstrip("\n")
        info=i.split(" ")
        freqdict[info[0]]=info[1]
        constates.append(info[0])

    for i in constates:
        if i in stateslist:
            stateslist.remove(i)
    #Legacy system management ends here

    try:
        assign(0)#Assigning frequencies to rest of the states
    except MyError as e:
        pass
    print "Number of backtracks:", backtrack
    f = open('results.txt', 'w')
    f.write(finalanswer)
    f.close()
    #if no solution:
    if not foundsolution:
        print "failed to find soltion"