import math
import random

###the following code is referred from https://leetcode.com/problems/design-skiplist/discuss/2184955/Python-pointers

class Node:
    
    def __init__(self,value=-1,rightnode=None,downnode=None):
        self.val=value
        self.next = rightnode
        self.down= downnode
    
class LookUpSkipList:
    
    def __init__(self,words,prob):
        self.head=Node()
        self.prob = prob
        level =int(math.log(len(words)))
        self.len = level
        curr = self.head
        curr.next = None
        for i in range(level-1):
            curr.down = Node(-1)
            curr =curr.down
            curr.next = None
        
        for i in range(len(words)):
            self.Insert(words[i])
        
        
    def Insert(self,num):

        levels = []
        curr= self.head

        while curr:
            if curr.next == None or num <= curr.next.val :
                levels.append(curr)
                curr =curr.down
            else:
                curr =curr.next

        prev = None
        while(levels):
            curr =levels.pop()
            node = Node(num)
            node.next =curr.next
            curr.next = node

            if prev:
                node.down = prev
                prev = node
            else:
                prev = node

            if LookUpSkipList.random(self):
                break;
                     
            
    def random(self):
        ran = []
        for i in range(0,10):
            ranin = random.randint(0,1)
            ran.append(ranin)

        if ran.count(0)/10 >= self.prob:
            return False
        else:
            return True
        
    def delete(self,num):
        current = self.head
        while current:
#             print(current.val)
            while current.next and current.next.val < num:
                current =current.next
            if current.next and current.next.val == num:
#               print("in if condition")
                current.next = current.next.next
            elif current.next and current.next.val == num and current.next.next==None:
                current.next = None
            current = current.down

            
    def print(self):
        current = self.head
        for i in range(self.len-1,-1,-1):
            previo = current.next
            while previo:
                print(previo.val,end=" -> ")
                previo = previo.next
            print("Level:",i)
            current =current.down
    
    def Search(self,num):
        curr =self.head
        while curr:
            if curr.val == num:
                return True
            else:
                if curr.next and curr.next.val <= num :
                    curr =curr.next
                else:
                    curr= curr.down
        if curr == None:
            self.Insert(num)
            return False
            

if __name__ == '__main__':
    
    lu_sk_lists = LookUpSkipList(["iub","usa","there","sort","god","ll","yy","rr","tt"],0.6)
    lu_sk_lists.print()
    print("-------------------------Insert------------------- ")
    lu_sk_lists.Insert("shash")
    lu_sk_lists.print()
    print("------------------------Delete---------------------")
    lu_sk_lists.delete("shash")
    lu_sk_lists.print()
    print("-------------------------Search---------------------")
    abc=lu_sk_lists.Search("abc")
    print(abc)
    print("-------------------------Search---------------------")
    abc=lu_sk_lists.Search("abc")
    print(abc)

     