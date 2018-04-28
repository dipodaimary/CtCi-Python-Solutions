class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
    def remove(self,data,previous):
        if self.data == data:
            previous.nextNode = self.nextNode
            del self
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data,self)
