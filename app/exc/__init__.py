class EmptyListError(Exception):
    def __init__(self) -> None:
        self.message = {'error': 'The list is empty!'}
        super().__init__(self.message)

class CpfExistError(Exception):
    def __init__(self, cpf) -> None:
        self.message = {'error': f'CPF {cpf} already exists!'}
        super().__init__(self.message)