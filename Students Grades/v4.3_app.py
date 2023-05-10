from flask import Flask, render_template, request
import v4_2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_software', methods=['POST'])
def run_software():
    # Call your Python software's function here and get the result
    result = v4_2.main()
    return {'result': result}

if __name__ == '__main__':
    app.run(debug=True)
