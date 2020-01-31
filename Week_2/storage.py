import os
import tempfile
import json
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def file_check():
    if not os.path.exists(storage_path):
        return dict()

    with open(storage_path, 'r') as f:
        data = f.read()
        if data:
            return json.loads(data)
        return dict()


def show_key(key):
    data = file_check()
    return data.get(key)


def add(key, value):
    data1 = file_check()
    if key in data1:
        data1[key].append(value)
    else:
        data1[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data1))


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-k', '--key', help='key', required=True)
    parse.add_argument('-v', '--value', help='value')
    parse.add_argument('--clear', help='clear')

    args = parse.parse_args()

    if args.clear:
        os.remove(storage_path)
    elif args.key and args.value:
        add(args.key, args.value)
    elif args.key:
        print(show_key(args.key))
