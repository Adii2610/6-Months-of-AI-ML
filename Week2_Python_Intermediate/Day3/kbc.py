q = ["who is the greatest in the world?", "1 + 1 = ?", "who is the leader?"]
a = ["Aditya", "2", "Aditya"]
score = 0

for i in range(0,len(q)):
    print(q[i])
    ans = input("ans: ")
    if ans == a[i]:
        print("Currect Answer!!!")
        score += 1
    else:
        print("Wrong Answer!!!")

print(f'score = {score}')
