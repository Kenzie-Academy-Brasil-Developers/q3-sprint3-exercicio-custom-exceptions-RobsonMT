import csv
from ..exc import EmptyListError, CpfExistError

FILENAME='dados_pessoas.csv'

def read_csv():
    with open(FILENAME) as fp:
        reader = csv.DictReader(fp)
        peoples = list(reader)

    if peoples:
        return peoples

    raise(EmptyListError)


def create_people(data_body):
    peoples = read_csv()

    filter_cpf_exists = [people for people in peoples if people['cpf'] == str(data_body['cpf'])]

    if filter_cpf_exists:
        raise(CpfExistError(data_body['cpf']))

    fieldnames=['nome', 'idade', 'cpf']
    
    with open(FILENAME, 'a') as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writerow(data_body)