class Node:
    def __init__(self, item):
        self.data = item
        self.preceding = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Retorna o número de elementos na estrutura."""
        return self._size

    def __str__(self):
        """Representa o conteúdo da DoublyLinkedList."""
        if not self._head:
            return 'DoublyLinkedList[]'
        doubly_linked_list = 'DoublyLinkedList['
        auxiliary = self._head
        while True:
            doubly_linked_list += (
                f"'{auxiliary.data}'"
                if type(auxiliary.data) == str
                else f'{auxiliary.data}'
            )
            if auxiliary == self._tail:
                doubly_linked_list += ']'
                break
            doubly_linked_list += ', '
            auxiliary = auxiliary.next
        return doubly_linked_list

    def __repr__(self):
        """Representa o conteúdo da DoublyLinkedList em modo de DEBUG."""
        return self.__str__()

    def __iter__(self):
        """Implementa iter(self). Torna a estrutura passível de iterações."""
        auxiliary = self._head
        for pos in range(self._size):
            yield f'{auxiliary.data}'
            if auxiliary.next is None:
                break
            auxiliary = auxiliary.next

    def __add__(self, obj):
        """Somar objetos."""
        if (
            type(obj) == list
            or type(obj) == tuple
            or type(obj) == set
            or type(obj) == dict
        ):
            raise TypeError(
                'can only concatenate DoublyLinkedList with the same type'
            )
        from copy import deepcopy

        if type(self) == type(obj):
            auxiliary = deepcopy(self)
            for item in obj:
                auxiliary.append(item)
            return auxiliary

    def __getitem__(self, index):
        """Retorna o objeto no index, self[index].
        Args:
            index: índice da DoublyLinkedList.
        """
        if index >= self._size or index < 0:
            raise IndexError('Index out of range')
        aux_index = 0
        auxiliary = self._head
        while True:
            if aux_index == index:
                return auxiliary.data
            if auxiliary.next is None:
                return
            aux_index += 1
            auxiliary = auxiliary.next

    def __setitem__(self, index, item):
        """Define self[index] como item.
        Args:
            index: índice a ser a inserido
            item: objeto a ser inserido
        """
        self.pop(index)
        self.insert(index, item)

    def clear(self):
        """Remove todos os items da DoublyLinkedList."""
        self._head = None
        self._tail = None
        self._size = 0

    def copy(self):
        """Retorna uma cópia superficial da DoublyLinkedList."""
        shallow_copy = self
        return shallow_copy

    def reverse(self):
        """Reverte NA ORDEM."""
        ...

    def sort(self, reverse=False):
        """Ordena a DoublyLinkedList.
        Args:
            reverse: False por default, se True, ordena de forma decresente.
        """
        ...

    def append(self, item):
        """Adiciona e retorna o item no final da DoublyLinkedList.
        Args:
                item: objeto a ser adicionado
        """
        if not self._head:
            self._head = Node(item)
            self._tail = self._head
            self._size += 1
            return self._head.data
        auxiliary = Node(item)
        auxiliary.preceding = self._tail
        self._tail.next = auxiliary
        self._tail = auxiliary
        self._size += 1
        return self._tail.data

    def insert(self, index, item):
        """Insere e retorna o item no index.
        Args:
                index: índice a ser inserido.
                item: objeto a ser inserido.
        """
        if index >= self._size:
            return self.append(item)
        if index == 0:
            auxiliary = Node(item)
            auxiliary.next = self._head
            self._head.preceding = auxiliary
            self._head = auxiliary
            return auxiliary.data

        auxiliary = self._head
        for i in range(index - 1):
            auxiliary = auxiliary.next

        node_new = Node(item)
        node_new.preceding = auxiliary
        node_new.next = auxiliary.next
        node_new.next.preceding = node_new
        auxiliary.next = node_new
        return node_new.data

    def pop(self, index=-1):
        """Remove e retorna o item no index (último por default).
        Args:
                index: índice do objeto a ser removido.
        """
        if index == -1:
            index = self._size - 1
        if not self._head:
            raise IndexError('The DoublyLinkedList is empty')
        if index >= self._size or index < 0:
            raise IndexError('pop index out of range')

        if index == 0:
            if self._size == 1:
                auxiliary = self._head.data
                self._head = None
                self._tail = None
                self._size -= 1
                return auxiliary
            auxiliary = self._head.data
            self._head = self._head.next
            self._size -= 1
            return auxiliary

        if index == self._size - 1:
            auxiliary = self._tail.data
            self._tail.preceding.next = None
            self._tail = self._tail.preceding
            self._size -= 1
            return auxiliary

        auxiliary = self._head
        for i in range(index):
            auxiliary = auxiliary.next
        auxiliary.preceding.next = auxiliary.next
        auxiliary.next.preceding = auxiliary.preceding
        self._size -= 1
        return auxiliary.data

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

    def index(self, item):
        """Retorna o primeiro índice do item.
        Args:
                item: objeto a ser verificado.
        """
        if not self._head:
            raise IndexError('The DoublyLinkedList is empty')
        index = 0
        auxiliary = self._head
        while True:
            if auxiliary.data == item:
                return index
            if auxiliary.next is None:
                raise ValueError(f'{item} is not in DoublyLinkedList')
            index += 1
            auxiliary = auxiliary.next

    def remove(self, item):
        """Remove e retorna a primeira ocorrencia do item.
        Args:
                item: objeto a ser removido.
        """
        index = 0
        auxiliary = self._head
        while True:
            if auxiliary.data == item:
                return self.pop(index)
            if auxiliary.next is None:
                raise ValueError(f'{item} is not in DoublyLinkedList')
            index += 1
            auxiliary = auxiliary.next
