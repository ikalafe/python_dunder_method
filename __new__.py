class Printer:
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super().__new__(self)
        return self._instance
    
p1 = Printer()
p2 = Printer()
print(p1 is p2)