from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_cpf', methods=['POST'])
def calcular_cpf():
    cpf_base = request.form['cpf_input']

    if len(cpf_base) != 9 or not cpf_base.isdigit():
        return render_template('index.html', error='Digite os 9 primeiros dígitos do CPF.')

    cpf_base = int(cpf_base)
    m = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    cpf_digits = [int(digit) for digit in str(cpf_base).zfill(9)]

    d1 = 11 - (sum(a * b for a, b in zip(cpf_digits, m)) % 11)
    d1 = d1 if d1 < 10 else 0

    m.insert(0, 11)
    cpf_digits.append(d1)

    d2 = 11 - (sum(a * b for a, b in zip(cpf_digits, m)) % 11)
    d2 = d2 if d2 < 10 else 0

    cpf_completo = "{:09d}{}{}".format(cpf_base, d1, d2)

    return render_template('index.html', cpf_completo=cpf_completo)

if __name__ == '__main__':
    app.run(debug=True)
