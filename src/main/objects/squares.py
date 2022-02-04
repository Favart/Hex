class Squares():
    
    def __init__(self,n):
        self.squares = []
        for i in range(n):
            for j in range(n):
                self.squares.append((i,j))
        self.pulled = []
        
    def pull(self,square):
        self.squares.remove(square)
        self.pulled.append(square)

    def get_last(self):
        return self.squares
    
    def get_pulled(self):
        return self.pulled
