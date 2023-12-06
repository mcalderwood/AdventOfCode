from pathlib import Path
import math

class Pair:
    def __init__(self, d1, d2):
        if type(d1) is Pair:
            d1.parent = self
        if type(d2) is Pair:
            d2.parent = self
        self.left = d1
        self.right = d2
        self.parent = None
    
    def reduce(self):
        #print("Reducing: ", str(self))
        while True:            
            if self.explode():
                #print("exploded:", self)
                continue
            if self.split():
                #print("splitted:", self)
                continue
            break
        return self
    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "[" + str(self.left) + "," + str(self.right) + "]"
    
    def split(self):
        if type(self.left) is not Pair and self.left >= 10:
            self.left = Pair(math.floor(self.left / 2), math.ceil(self.left / 2)) 
            self.left.parent = self
            return True
        elif type(self.left) is Pair and self.left.split():
            return True
        elif type(self.right) is not Pair and self.right >= 10:
            self.right = Pair(math.floor(self.right / 2), math.ceil(self.right / 2)) 
            self.right.parent = self
            return True
        elif type(self.right) is Pair and self.right.split():
            return True
        else:
            return False

    # return (bool - did explode?)
    def explode(self, lvl = 0):
        if lvl == 3:
            if type(self.left) is Pair:
                # Find left number and add left.left to it
                n = self

                while n.parent != None and n.parent.left is n:
                    n = n.parent

                if n.parent != None and n.parent.right is n:
                    if type(n.parent.left) is not Pair:
                        n.parent.left += self.left.left
                    else:
                        n = n.parent.left
                        while type(n.right) == Pair:
                            n = n.right
                        n.right += self.left.left

                # Find right number and add left.right to it
                if type(self.right) is not Pair:
                    self.right += self.left.right
                else:
                    n = self.right
                    while type(n.left) == Pair:
                        n = n.left
                    n.left += self.left.right
                
                self.left = 0

                return True

            elif type(self.right) is Pair:
                # Find left number and add right.left to it
                if type(self.left) is not Pair:
                    self.left += self.right.left
                else:
                    n = self.left
                    while type(n.right) == Pair:
                        n = n.right
                    n.right += self.right.left
                
                # Find right number and right.right to it

                n = self
                while n.parent != None and n.parent.right is n:
                    n = n.parent

                if n.parent != None and n.parent.left is n:
                    if type(n.parent.right) is not Pair:
                        n.parent.right += self.right.right
                    else:
                        n = n.parent.right
                        while type(n.left) == Pair:
                            n = n.left
                        n.left += self.right.right

                self.right = 0

                return True
            else:
                return False
                
        elif lvl < 3:
            if type(self.left) is Pair:
                if self.left.explode(lvl+1):
                    return True
            if type(self.right) is Pair:
                if self.right.explode(lvl+1):
                    return True
            return False
    
    def magnitude(self):
        if type(self.left) is Pair:
            left_value = self.left.magnitude()
        else: 
            left_value = self.left
        
        if type(self.right) is Pair:
            right_value = self.right.magnitude()
        else:
            right_value = self.right

        return (left_value * 3) + (right_value * 2)

def parse_number(str):
    # Find comma for top-level pair
    nest_level = 0
    comma_idx = -1

    if str[0] != '[':
        return int(str)

    for i in range(len(str)):
        c = str[i]
        if c == '[':
            nest_level += 1
        elif c == ']':
            nest_level -= 1
        elif c == ',' and nest_level == 1:
            comma_idx = i
            break

    if comma_idx == -1:
        print ("Bad syntax! ", str)
        return

    left = parse_number(str[1:comma_idx])
    right = parse_number(str[comma_idx+1:len(str)-1])

    return Pair(left,right)

def add_numbers(left, right):
    return Pair(left, right).reduce()
    #return reduce(sum)

#
#def explode(number, level):
#    if type(number) is tuple and level == 4:


path = Path(__file__).parent / "aoc-day18-input.txt"
with open(path) as my_file:
    input_array = my_file.readlines()

#n = parse_number("[[[[5,11],[13,0]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]")
#n.explode()
#print(n)
#exit()

numbers = []
for n in input_array:
    numbers.append(parse_number(n.strip(" \r\n")))
max = 0

for num1 in range(len(input_array)):
    for num2 in range(len(input_array)):
        if num1 == num2:
            continue
        n1 = parse_number(input_array[num1].strip(" \r\n"))
        n2 = parse_number(input_array[num2].strip(" \r\n"))
        mag = add_numbers(n1, n2).magnitude()
        print ("mag (", mag, "): ", num1, " ", num2)
        if mag > max:
            
            max = mag
print (max)
exit()
        



sum = parse_number(input_array[0].strip(" \r\n"))
#print(sum)
for line in input_array[1:]:
    sum = add_numbers(sum, parse_number(line.strip(" \r\n")))
    #print(sum)

#print(sum)
print(sum.magnitude())
exit()

#num = parse_number("[[[[0,7],4],[15,[0,13]]],[1,1]]")
#num.split()
#print(num)
#num.split()
#print(num)

num = add_numbers(parse_number("[[[[4,3],4],4],[7,[[8,4],9]]]"), parse_number("[1,1]"))
#num.reduce()
print(num)
exit()

num = parse_number("[[[[[9,8],1],2],3],4]")
#num = parse_number("[7,[6,[[5,4],[[3,2],1]]]]")
#num = parse_number("[7,[6,[5,4],[[3,2],1]]]]")
num.explode()
print(num)

num = parse_number("[7,[6,[5,[4,[3,2]]]]]")
num.explode()
print(num)

num = parse_number("[[6,[5,[4,[3,2]]]],1]")
num.explode()
print(num)

num = parse_number("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
num.explode()
print(num)

num = parse_number("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
num.explode()
print(num)

exit()

