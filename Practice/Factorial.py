class Recurse:

    def recurse(self, num):
        if num == 0:
            return 1
        return num * self.recurse(num - 1)





re = Recurse()

val = re.recurse(5)
print(val)