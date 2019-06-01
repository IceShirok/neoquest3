import json


def run_app():
    print('Hello world!')

    with open('skills.json') as f:
        lines = f.readlines()
        for line in lines:
            skill = json.loads(line)
            print(json.dumps(skill, indent=4))
    f.close()


if __name__ == '__main__':
    run_app()
