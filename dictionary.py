import json
import difflib
def arrange(outputt,key):
    print("::",key)
    for i in outputt:
                print("-",i)

def fun():                            
    print("What To search:")
    data=input()            #Take Word from user
    data=data.lower()       #Lowercase It To avoid case errors
    if data in dataset:     # check for word in json file
        if(type(dataset[data])==list):
            output=dataset[data]
            arrange(output,data)
        else:
            print("-",dataset[data])
           
    else:
        #To get Closest Match
        if difflib.get_close_matches(data,dataset):
            x=difflib.get_close_matches(data,dataset)
            for j in x:
                if j in dataset:
                    
                    arrange(dataset[j],j)
        else:
            print("Given word Is Wrong Please Check it Again!")


dataset=json.load(open("data.json"))  #loads the json file
count=1
while count==1:
    fun()
    print("\n Want to search Anything Else?\nThen Type 1 Else 0")   #for again searching
    count=int(input())