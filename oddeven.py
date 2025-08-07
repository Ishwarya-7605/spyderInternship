class odd_even:

    def __init__(self,num):
        self.num = num

    def od_eve(self):
        if(self.num%2==0):
            print("the num is even: ",self.num)
        else:
            print("the num is odd:",self.num)

number=odd_even(39)
number.od_eve()
