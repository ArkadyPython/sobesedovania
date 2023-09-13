slov = {
    '(': ')',
    '[': ']',
    '{': '}'
}
balance = ['(((([{}]))))',
          '[([])((([[[]]])))]{()}',
          '{{[()]}}'
           ]
not_balance = [
            '}{}',
            '{{[(])]}}',
            '[[{())}]'
                      ]
class Stack(list):
    def isEmpty(self):
        if (len(self) == 0) == True:
            return 'Сбалансированно'
        else :
            return 'Несбалансированно'

    def push(self, new_elem):
        self.append(new_elem)

    def pop(self):
        if self.isEmpty() == 'Несбалансированно':
            item = self[-1]
            self.__delitem__(-1)
        return item

    def peek(self):
        if self.isEmpty() == 'Несбалансированно':
            return self[-1]

    def size(self):
        return len(self)

def check_stack(sq):
    stack = Stack()
    for elem in sq:
        if elem in slov:
            stack.push(elem)
        elif elem == slov.get(stack.peek()):
            stack.pop()
        else:
            return 'Несбалансированно'
    return stack.isEmpty()
if __name__ == '__main__':
    for sq in balance + not_balance:
        print(f'{sq:<30}{check_stack(sq)}')