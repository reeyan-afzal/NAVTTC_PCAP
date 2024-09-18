# Task 49 - Queue
class QueueError:
    pass


class ParentQueue:
    def __init__(self):
        self._queue = []
        
    def put(self, elem):
        self._queue.append(elem)

    def get(self):
        if len(self._queue):
            val = self._queue[0]
            del self._queue[0]
            return val
        else:
            return 'Queue is Empty'

    def return_queue_list(self):
        return self._queue


class ChildQueue(ParentQueue):
    def __init__(self):
        super().__init__()

    def put(self, elem):
        super().put(elem)

    def get(self):
        return super().get()

    def is_empty(self):
        _queue_list = super().return_queue_list()
        if not len(_queue_list):
            return True
        else:
            return False

    def display_queue(self):
        elements = ", ".join([str(self.return_queue_list()[elem]) for elem in range(len(self.return_queue_list()))])
        return elements


queue = ChildQueue()
queue.put(1)
queue.put("Dog")
queue.put(False)
print("The Queue consists: [" + queue.display_queue() + "]")
for i in range(4):
    if not queue.is_empty():
        print(queue.get())
    else:
        print("Queue Error")
