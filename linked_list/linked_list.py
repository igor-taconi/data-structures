class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        """Retorna o número de elementos na estrutura."""
        return self._size

    def __str__(self):
        """Representa o conteúdo da LinkedList quando ela for printada."""
        if not self._head:
            return 'LinkedList[]'
        linked_list = 'LinkedList['
        auxiliary = self._head
        while True:
            linked_list += (
                f"'{auxiliary.data}'"
                if type(auxiliary.data) == str
                else f'{auxiliary.data}'
            )
            if not auxiliary.next:
                linked_list += ']'
                break
            linked_list += ', '
            auxiliary = auxiliary.next
        return linked_list

    def __repr__(self):
        """Representa o conteúdo da LinkedList em modo de DEBUG."""
        return self.__str__()

    def __iter__(self):
        """Implementa iter(self). Torna a LinkedList passível de iterações."""
        auxiliary = self._head
        for pos in range(self._size):
            yield f'{auxiliary.data}'
            if auxiliary.next is None:
                break
            auxiliary = auxiliary.next

    def __getitem__(self, index):
        """Retorna o objeto no index, self[index].
        Args:
            index: índice da LinkedList.
        """
        auxiliary = self._getnode(index)
        if auxiliary:
            return auxiliary.data
        else:
            raise IndexError("index out of range")

    #
    def __setitem__(self, index, item):
        """Define self[index] como item.
        Args:
            index: índice a ser a inserido
            item: objeto a ser inserido
        """
        auxiliary = self._getnode(index)
        if not auxiliary:
            raise IndexError("index out of range")
        auxiliary.data = item

    def append(self, item):
        """Adiciona e retorna o item no final da DoublyLinkedList.
        Args:
                item: objeto a ser adicionado
        """
        if not self._head:
            self._head = Node(item)
            self._size += 1
            return self._head.data
        auxiliary = self._head
        while True:
            if not auxiliary.next:
                break
            auxiliary = auxiliary.next
        auxiliary.next = Node(item)
        self._size += 1
        return auxiliary.next.data

    def _getnode(self, index):
        """Pega o objeto no index informado.
        Args:
            index: índice do objeto
        """
        if not self._head:
            raise IndexError("index out of range")
        auxiliary = self._head
        for i in range(index):
            if not auxiliary:
                raise IndexError("index out of range")  # return None
            auxiliary = auxiliary.next
        return auxiliary

    def index(self, item):
        """Retorna o primeiro índice do item.
        Args:
                item: objeto a ser verificado.
        """
        if not self._head:
            raise IndexError('The LinkedList is empty')
        index = 0
        auxiliary = self._head
        while True:
            if auxiliary.data == item:
                return index
            if auxiliary.next is None:
                raise ValueError(f'{item} is not in LinkedList')
            index += 1
            auxiliary = auxiliary.next

    def insert(self, index, item):
        """Insere e retorna o item no index.
        Args:
                index: índice a ser inserido.
                item: objeto a ser inserido.
        """
        node = Node(item)
        if index == 0:
            node.next = self._head
            self._head = node
            self._size += 1
            return self._head.data
        auxiliary = self._getnode(index - 1)
        node.next = auxiliary.next
        auxiliary.next = node
        self._size += 1
        return auxiliary.next.data

    def pop(self, index=-1):
        """Remove e retorna o item no index (último por default).
        Args:
                index: índice do objeto a ser removido.
        """
        if index == -1:
            index = self._size - 1
        if not self._head:
            raise IndexError('The LinkedList is empty')
        if index >= self._size or index < 0:
            raise IndexError('pop index out of range')

        if index == 0:
            if self._size == 1:
                auxiliary = self._head.data
                self._head = None
                self._size -= 1
                return auxiliary
            auxiliary = self._head.data
            self._head = self._head.next
            self._size -= 1
            return auxiliary
        aux_index = 1
        preceding = self._head
        auxiliary = self._head.next
        while True:
            if aux_index == index:
                item = preceding.next.data
                preceding.next = auxiliary.next
                auxiliary.next = None
                self._size -= 1
                return item
            preceding = auxiliary
            auxiliary = auxiliary.next

    def remove(self, item):
        """Remove e retorna a primeira ocorrencia do item.
        Args:
                item: objeto a ser removido.
        """
        if not self._head:
            raise ValueError(f'{item} is not in list')
        if self._head.data == item:
            auxiliary = self._head.data
            self._head = self._head.next
            self._size -= 1
            return auxiliary
        preceding = self._head
        auxiliary = self._head.next
        while True:
            if not auxiliary.next:
                raise ValueError(f'{item} is not in list')
            if auxiliary.data == item:
                preceding.next = auxiliary.next
                auxiliary.next = None
                self._size -= 1
                return item
            preceding = auxiliary
            auxiliary = auxiliary.next

    def count(self, item):
        """Retorna o número de ocorrencia do item.
        Args:
                item: objeto a ser verificado
        """
        if not self._head:
            return 0
        counter = 0
        auxiliary = self._head
        while True:
            if auxiliary.data == item:
                counter += 1
            if auxiliary.next is None:
                return counter
            auxiliary = auxiliary.next
