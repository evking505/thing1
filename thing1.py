class Collatz:

    def __init__(self, num=-1):
        self.num = num

    def compute(self, num=-1):
        counter = 0
        if(num != -1):
            self.num = num
        if(self.num == -1):
            print("Please use a number >1")
            return
        if(self.num > 1):
            while(self.num != 1):
                if(self.num%2 == 0):
                    self.num /= 2
                else:
                    self.num = ((self.num*3)+1)
                counter += 1
                #print(self.num)
            return counter
