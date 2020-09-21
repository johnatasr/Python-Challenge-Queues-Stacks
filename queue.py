
class QueueEnqueueException(Exception):
    def __init__(self):
        self.message = "The queue is full"

    def __str__(self):
        if self.message:
            return 'QueueEnqueueException, {0} '.format(self.message)
        else:
            return 'QueueEnqueueException has been raised'


class QueueDequeueException(Exception):
    def __init__(self):
        self.message = "The queue is empty"

    def __str__(self):
        if self.message:
            return 'QueueDequeueException, {0} '.format(self.message)
        else:
            return 'QueueDequeueException has been raised'


class Queue:
    def __init__(self):
        self.__size = 1000                          # Length of queue
        self.items = [None] * self.__size           # A list with None values to be used in queue
        self.__front = -1                           # First position of queue
        self.__rear = -1                            # Last position of queue

    @classmethod
    def __reset_obj_list(cls):    # Function to restart all positions in queue
        cls.__rear = -1
        cls.__front = -1

    # Verify if the queue is full
    def is_full(self) -> bool:
        if self.__front == 0 and self.__rear == (self.__size - 1):
            return True
        else:
            return False

    # Verify if the queue is empty
    def is_empty(self) -> bool:
        if self.__front == -1 or self.items[0] == None:   # Check if the top of our fake "array" is empty or exists elements inside the first position
            return True
        else:
            return False

    # Add elements in queue
    def enqueue(self, element):
        if self.is_full():
            raise QueueEnqueueException()
        else:
            if self.__front == -1:
                self.__front = 0
            self.__rear = self.__rear + 1
            self.items[self.__rear] = element
            print(f"Inserted {element}")

    # Remove first element added in queue
    def dequeue(self):
        if self.is_empty():
            raise QueueDequeueException()
        else:
            element = self.items[self.__front]
            if self.__front > self.__rear:
               self.__reset_obj_list()
            else:
                del self.items[self.__front]
                self.__rear -= 1
                self.items = self.items + [None]
            print(f"Deleted: {element}")
            return element

    # Length of queue
    def __len__(self) -> int:
        if self.__rear == -1:
            return 0
        elif self.__rear == 0:
            return 1
        else:
            return self.__rear + 1

    # A string representation of class
    def __str__(self):
        if self.__rear == -1:
            return str("")
        else:
            queue_str = ""
            for index, item in enumerate(self.items[self.__front:(self.__rear + 1)]):
                if index > 0:
                    queue_str = queue_str + f" -> {item}"
                else:
                    queue_str = queue_str + f"{item}"

            return queue_str

    def __repr__(self):
        if self.__rear == -1:
            return str('')
        else:
            queue_str = ''
            for index, item in enumerate(self.items[self.__front:(self.__rear + 1)]):
                if index > 0:
                    queue_str = queue_str + f' -> {item}'
                else:
                    queue_str = queue_str + f'{item}'

            return queue_str


if __name__ == "__main__":

    # Test Print

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(34)
    queue.enqueue(367)
    print(queue)
    print(len(queue))
    queue.dequeue()
    print(queue)
    print(len(queue))
    print(f'Is full ?  {queue.is_full()}')
    print(f'Is empty ? {queue.is_empty()}')
    queue.dequeue()
    queue.dequeue()
    print(queue)
    print(len(queue))






