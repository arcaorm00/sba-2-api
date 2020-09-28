import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from flask import Flask, render_template, request
from service.calculator_service import CalculatorService

from config import basedir

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc', methods=['POST'])
def calc():
    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']
    calc = CalculatorService()
    result = calc.calc(num1, num2, opcode)
    render_params = {}
    render_params['result'] = result
    return render_template('index.html', **render_params)

if __name__ == '__main__':
    print(f'***** {basedir}')
    app.run()
    