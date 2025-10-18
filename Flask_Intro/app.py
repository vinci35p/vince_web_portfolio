from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Calculate area of circle
@app.route('/calc_circle', methods=['POST'])
def calc_circle():
    data = request.get_json()
    radius = float(data.get('radius', 0))
    if radius <= 0:
        return jsonify({'error': 'Please enter a valid radius.'})
    area = 3.1416 * radius * radius
    return jsonify({'area': round(area, 2)})

# Calculate area of triangle
@app.route('/calc_triangle', methods=['POST'])
def calc_triangle():
    data = request.get_json()
    base = float(data.get('base', 0))
    height = float(data.get('height', 0))
    if base <= 0 or height <= 0:
        return jsonify({'error': 'Please enter valid base and height values.'})
    area = 0.5 * base * height
    return jsonify({'area': round(area, 2)})

# Convert text to uppercase
@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.get_json()
    text = data.get('text', '')
    return jsonify({'result': text.upper()})

if __name__ == '__main__':
    app.run(debug=True)
