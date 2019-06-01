from flask import Flask, render_template
from pet.pet import Pet

import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


@app.route('/')
def index():
    my_pet = Pet(name='Wulgar', species='Lupe', color='Desert', gender='Male')
    return render_template('index.html',
                           title='Pet Page',
                           pet=my_pet)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
