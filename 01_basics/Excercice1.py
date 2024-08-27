questions = [
    ["What is the full form of A","Apple","Ant","And","Apti",1],
    ["What is the full form of A","Apple","Ant","And","Apti",1],
    ["What is the full form of A","Apple","Ant","And","Apti",1],
    ["What is the full form of A","Apple","Ant","And","Apti",1],
]

levels = [100,1000,10000,100000]

def kotipoti() :
    total = 0
    for i in range(len(questions)) :
        question = questions[i]
        print("\n\n")
        print(f"{i+1}. {question[0]} for Rs.{levels[i]}")
        print(f"1.{question[1]}      2.{question[2]}")
        print(f"3.{question[3]}      4.{question[4]}")
        result = int(input("Enter the currect option: "))
        if(result != question[-1]):
            print("Incorrect answer")
            return
        total += levels[i]
        print(f"Right ans and you got total Rs.{total}")


kotipoti()