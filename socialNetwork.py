#The Social Network
#In this problem, you will work with a social network. In this case, a "social network" consists of a set of individuals,
# and for each individual, a list of his contacts. (The contact relationship is not necessarily symmetric: A may be a contact of B,
# but B may not be a contact of A.) Let's define C to be an extended contact of A if C is a direct contact of A, or C can be reached
# by following the contact chains starting with A. Choose one or more appropriate data structures to model a social network like this.
# Devise an efficient algorithm that takes a social network as input and computes, for each individual in the network, his/her extended contact list.



extList = []
# network = Dictionary having details of whole network
# name = Name of person
def findContactList(network, name, extList):
    if name not in network.keys():
        print "This guy is not onthis platform!!"
        return
    if name not in extList:
        extList.append(name)
    for x in network[name]:
        if x not in extList:
            extList.append(x)
            findContactList(network,x, extList)
    return


def remContact(network, person, friend):
    if person not in network.keys():
        print "The "+ person+" itself doesn't exist !!"
    else:
        if friend not in network[person]:
            print person+" has no connecteion with "+friend
        else:
            network[person].remove(friend)
            print " Contact Deleted \m/"

    return


def addContact(network, person, friend):
    if person not in network.keys():
        network[person] = [friend]
    else:
        if friend not in network[person]:
            network[person].append(friend)
    if friend not in network.keys():
        network[friend] = []

    return

def addPerson(network, person):
    if person not in network.keys():
        network[person] = []
    else:
        print "Person is already in network !!"

    return



network = {}

print "Enter number of people: "
num = int(raw_input())
print "Enter name and friends list for each person individually \n Ex: A C F H \n A is a person, who has direct friends C,F and H"
for i in range(0,num):
    data = raw_input().split(" ")
    for x in range(1,len(data)):
        addContact(network,data[0],data[x])
#print network

while(1):

    print "\n 1 - Add new contact in friend list \n 2 - Remove a contact from friend list \n 3 - Add new Person \n 4 - Find Extended Contact List \n 5 - Finish the Script !! \m/"
    val = int(raw_input())
    if val == 3:
        print "Enter name of person"
        name = raw_input().split(" ")
        addPerson(network, name[0])
    elif val == 1:
        print "Enter name of person and the name of new contact :"
        names = raw_input().split(" ")
        addContact(network, names[0], names[1])
    elif val == 2:
        print "Enter name of person and the name of contact to be deleted :"
        names = raw_input().split(" ")
        remContact(network, names[0], names[1])


    elif val == 4:
        print "Enter name of person, for which you would like to see all contacts: "
        name = raw_input()
        extList = []
        findContactList(network, name, extList)
        extList.remove(name)
        if len(extList) == 0:
            print name+" has no friends yet .. :("
        else:
            print name+"\'s extended contacts: ",
            print extList
    elif val == 5:
        break
    else:
        print "dude what are you doing ... read the options first !!"



