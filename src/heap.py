import dataclasses

@dataclasses.dataclass
class MinHeap:

    items: list = dataclasses.field(default_factory=list)

    def get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1
    
    def get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2
    
    def get_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2
    
    def has_left_child(self, index: int) -> bool:
        return self.get_left_child_index(index) < len(self.items)
    
    def has_right_child(self, index: int) -> bool:
        return self.get_right_child_index(index) < len(self.items)
    
    def has_parent(self, index: int) -> bool:
        return self.get_parent_index(index) >= 0
    
    def get_left_child_item(self, index: int): 
        if not self.has_left_child(index):
            return None
        
        left_child_index = self.get_left_child_index(index)
        return self.items[left_child_index]
    
    def get_right_child_item(self, index: int):

        if not self.has_right_child(index):
            return None
        
        right_child_index = self.get_right_child_index(index)
        return self.items[right_child_index]
    
    def get_parent_item(self, index: int):
        if not self.has_parent(index):
            return None
        
        parent_index = self.get_parent_index(index)
        return self.items[parent_index]

    def swap(self, index1: int, index2: int) -> None:
        temp = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = temp

    def peek(self):
        if len(self.items) == 0:
            raise RuntimeError('heap is empty')
        return self.items[0]
    
    def poll(self):
        if len(self.items) == 0:
            raise RuntimeError('heap is empty')
        
        item = self.items[0]

        self.items[0] = self.items[-1]
        self.items = self.items[:-1]

        self.heapify_down()
        
        return item

    def heapify_down(self) -> None:
        
        index = 0

        while(self.has_left_child(index)):
            smaller_child_index = self.get_left_child_index(index)

            if self.has_right_child(index) and self.get_right_child_item(index) < self.get_left_child_item(index):
                smaller_child_index = self.get_right_child_index(index)
            
            if self.items[index] >= self.items[smaller_child_index]:
                self.swap(index, smaller_child_index)
            
            index = smaller_child_index

    def heapify_up(self) -> None:
        
        index = len(self.items) - 1

        while (self.has_parent(index) and self.get_parent_item(index) > self.items[index]):
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)
 
        

    def add(self, item):
        self.items.append(item)
        self.heapify_up()
