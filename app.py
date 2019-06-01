import json


def run_app():
    print('Hello world!')

    with open('stats.json') as f:
        lines = f.readlines()
        for line in lines:
            print(json.dumps(json.loads(line), indent=4))
    f.close()


if __name__ == '__main__':
    run_app()
