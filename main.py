import argparse
import csv
from tabulate import tabulate


def read_csv(file_path: str) -> list[dict]:
    with open(file_path, mode='r') as file:
        return list(csv.DictReader(file))


def filter_data(data: list[dict], condition: str) -> list[dict]:
    if not condition:
        return data

    column, value = condition.split('=')
    filtered = []
    for row in data:
        if column in row and row[column] == value:
            filtered.append(row)
    return filtered


def aggregate_data(data: list[dict], agg: str) -> dict:
    if not agg:
        return {}

    column, func = agg.split('=')
    values = [float(row[column]) for row in data if column in row]

    if func == 'avg':
        result = sum(values) / len(values)
    elif func == 'min':
        result = min(values)
    elif func == 'max':
        result = max(values)
    else:
        return {}

    return {func: round(result, 2)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    parser.add_argument('--where')
    parser.add_argument('--aggregate')
    args = parser.parse_args()

    data = read_csv(args.file)
    filtered = filter_data(data, args.where)

    if args.aggregate:
        result = aggregate_data(filtered, args.aggregate)
        print(tabulate([result], headers='keys', tablefmt='grid'))
    else:
        print(tabulate(filtered, headers='keys', tablefmt='grid'))


if __name__ == '__main__':
    main()