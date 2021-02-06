class Node:
    def __init__(self, item):
        self.data = item
        self.preceding = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def __len__(self):
        """Retorna o tamanho da Stack."""
        return self._size

    def __str__(self):
        """Representa o conteúdo da Stack quando ela for printada."""
        if not self.top:
            return 'Stack[]'
        auxiliary = self.top
        stack = 'Stack['
        while True:
            stack += (
                f"'{auxiliary.data}'"
                if type(auxiliary.data) == str
                else f'{auxiliary.data}'
            )
            if not auxiliary.preceding:
                stack += ']'
                break
            stack += ', '
            auxiliary = auxiliary.preceding
        return stack

    def __repr__(self):
        """Representa o conteúdo da Stack em modo de DEBUG."""
        return self.__str__()

    def push(self, item):
        """Insere um objeto no topo.
        Args:
            item: objeto a ser inserido.
        """
        auxiliary = Node(item)
        auxiliary.preceding = self.top
        self.top = auxiliary
        self._size += 1
        return self.top.data

    def pop(self):
        """Remove o objeto do topo."""
        if not self.top:
            raise IndexError('The stack is empty')
        auxiliary = self.top
        self.top = auxiliary.preceding
        self._size -= 1
        return auxiliary.data

    def peek(self):
        """Retorna o topo sem remover."""
        if not self.top:
            raise IndexError('The stack is empty')
        return self.top.data

    def contain(self, item):
        """Verifica se contém o objeto na Stack.
        Args:
            item: objeto a ser verificado.
        """
        if not self.top:
            raise IndexError('The stack is empty')
        auxiliary = self.top
        while auxiliary:
            if auxiliary.data == item:
                return True
            auxiliary = auxiliary.preceding
        return False
