class Node(object):
    def __init__(self, data):
        self.data   =   data
        self.pnext  =   None
    
    def __repr__(self):
        return  str(self.data)

class List:
    def __init__(self):
        self.length =   0
        self.head   =   None
    
    def is_empty(self):
        return  self.length ==  0

    def append(self, this_node):
        if isinstance(this_node, Node):
            pass
        else:
            this_node   =   Node(data=this_node)
        if self.is_empty():
            self.head   =   this_node
        else:
            node        =   self.head
            while node.pnext:
                node    =   node.pnext
            if node.pnext == None:
                node.pnext       =   this_node
                this_node.pnext  =   None
            
                
                

        self.length     +=  1 

    def insert(self, value, index):
        """
            inst_node <===> inserted_node    
        """
        inst_node    =   Node(data=value)
        current_node =   self.head
        if index    ==  0:
            self.head       =   inst_node
            inst_node.pnext =   current_node
        else:
            while index-1:
                current_node    =   current_node.pnext
                index -= 1  
    def delete(self, value):
        pass
    
    def printlist(self):
        current_node    =   self.head
        while current_node.pnext:
            print(current_node.data,"-->")
            current_node    =   current_node.pnext
        print(current_node.data)
            
        
        
           


if __name__ == '__main__':
    node1  =    Node(data='node1')
    node2  =    Node(data='node2')
    node3  =    Node(data='fuck')
    node4  =    Node(data='hi')
    list1  =    List()
    list1.append(node2)
    list1.append(node1)
    list1.append(node3)
    list1.append(node4)
    list1.printlist()


        
        
        
    
                
        
        

        
