## implementing basic stack operation

stack = [1,2,3,6,5,0,55,40,56]

class stacking:

    def push(self, num):
          stack.append(int(num)) 
          print(stack)
          return 0
    
    def poping(self):

        stack.remove(stack[-1])

        # stack.pop()
        print(stack)
        return 0 

sta = stacking()

flag = True
while flag == True:

    ch = input("What u want push or pop: ")
    if ch == 'push' or ch =='Push':
        ele = input("Enter element: ")
        sta.push(ele)
    
    elif ch == 'pop' or ch == 'Pop':
         sta.poping()
    else:
        print("Do valid choice")
        
    con = input("Want to continue 0(yes) or 1 (no): ")
    if(con == "1"):
        flag = False
        # break
    
        
    # i += 1

