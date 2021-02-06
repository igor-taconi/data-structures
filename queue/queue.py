class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        """Retorna o tamanho da Queue."""
        return self._size

    def __str__(self):
        """Representa o conteúdo da Queue quando ela for printada."""
        if not self.head:
            return 'Queue[]'
        queue = 'Queue['
        auxiliary = self.head
        while True:
            queue += (
                f"'{auxiliary.data}'"
                if type(auxiliary.data) == str
                else f'{auxiliary.data}'
            )
            if auxiliary == self.tail:
                queue += ']'
                break
            queue += ', '
            auxiliary = auxiliary.next
        return queue

    def __repr__(self):
        """Representa o conteúdo da Stack em modo de DEBUG."""
        return self.__str__()

    def equeue(self, item):
        """
        Insere um objeto no fim da Queue.
        Args:
            item: objeto a ser inserido.
        """
        if not self.head:
            self.head = Node(item)
            self.tail = self.head
            return self.tail.data
        self.tail.next = Node(item)
        self.tail = self.tail.next
        self._size += 1
        return self.tail.data

    def dequeue(self):
        """Remove o primeiro objeto."""
        if not self.head:
            raise IndexError('The queue is empty')
        auxiliary = self.head.data
        self.head = self.head.next
        self._size -= 1
        return auxiliary

    def first(self):
        """Retorna o primeiro objeto."""
        if not self.head:
            raise IndexError('The queue is empty')
        return self.head.data

    def contain(self, item):
        """
        Verifica se contém o objeto na Queue e retorna o índice.
        Args:
            item: objeto a ser verificado.
        """
        if not self.head:
            raise IndexError('The queue is empty')
        auxiliary = self.head
        _size = 0
        while True:
            if auxiliary.data == item:
                return _size
            if auxiliary == self.tail:
                break
            _size += 1
            auxiliary = auxiliary.next
        raise ValueError(f'{item} is not in Queue')
