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

# Infix to Postfix Conversion
@app.route('/infix_to_postfix', methods=['POST'])
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
        
    def is_empty(self):
        return self.top is None
    
    def print_stack(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            current = self.top
            print("Stack Elements (top --> bottom): ")
            while current:
                print(current.data)
                current = current.next

# Infix to postfix conversion

def ranking(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    output = ""
    stack = Stack()

    for char in expression:
        if char.isalnum():
            output += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() is not None and stack.peek() != '(':
                output += stack.pop()
            stack.pop()
        else:
            while (not stack.is_empty() and ranking(stack.peek()) >= ranking(char)):
                output += stack.pop()
            stack.push(char)

    while not stack.is_empty():
        output += stack.pop()

    return output

expression = input("Enter infix expression:")
print("Infix expression: ", expression)
print("Postfix expression: ", infix_to_postfix(expression))

if __name__ == '__main__':
    app.run(debug=True)
