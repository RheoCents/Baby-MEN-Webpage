from flask import Flask, render_template, request
from labexercise import linklist, stack
from labexercise.stack import infix_to_postfix
from templates import *

app = Flask(__name__)

# Create a global LinkedList instance
linked_list = linklist.LinkedList()

# Global list to track submitted string/number inputs
submitted_inputs_list = []

# Route for homepage
@app.route('/')
def index():
    return render_template('upload.html')

# Route for Works
@app.route('/works')
def work():
    return render_template('works.html')

@app.route('/work1')
def work1():
    return render_template('linkedlist.html')  

@app.route('/work2')
def work2():
    return render_template('convert.html')  

@app.route('/work3')
def work3():
    return render_template('word-eater.html')  


# Route for linked list page
@app.route('/linkedlist')
def linkedlist_page():
    return render_template(
        'linkedlist.html',
        linked_list_items=linked_list.list_LinkedList(),
        submitted_inputs=submitted_inputs_list
    )

# Route to add a node to the linked list
@app.route('/add1', methods=['POST'])
def insert_end():
    data = request.form.get('data', '')
    if data:
        linked_list.insert_at_end(data)  # Add the data to the end of the linked list
        submitted_inputs_list.append(data)  # Track the submitted inputs
    return render_template(
        'linkedlist.html',
        linked_list_items=linked_list.list_LinkedList(),
        submitted_inputs=submitted_inputs_list
    )

@app.route('/add2', methods=['POST'])
def insert_beginning():
    data = request.form.get('data', '')
    if data:
        linked_list.insert_at_beginning(data)  # Add the data to the end of the linked list
        submitted_inputs_list.append(data)  # Track the submitted inputs
    return render_template(
        'linkedlist.html',
        linked_list_items=linked_list.list_LinkedList(),
        submitted_inputs=submitted_inputs_list
    )

# Route to remove a node from the beginning
@app.route('/remove_at_beginning', methods=['POST'])
def remove_at_beginning():
    linked_list.remove_at_beginning()
    return render_template(
        'linkedlist.html',
        linked_list_items=linked_list.list_LinkedList(),
        submitted_inputs=submitted_inputs_list
    )

# Route to remove a node from the end
@app.route('/remove_at_end', methods=['POST'])
def remove_at_end():
    linked_list.remove_at_end()
    return render_template(
        'linkedlist.html',
        linked_list_items=linked_list.list_LinkedList(),
        submitted_inputs=submitted_inputs_list
    )

@app.route('/work2', methods=['GET', 'POST'])
def convert_expression():
    postfix_expression = None
    infix_expression = None
    steps_list = []

    if request.method == 'POST':
        infix_expression = request.form['expression']  
        if infix_expression:
            postfix_expression, steps_list = infix_to_postfix(infix_expression)

    return render_template(
        'convert.html',
        infix_expression=infix_expression,
        postfix_expression=postfix_expression,
        steps=steps_list
    )

if __name__ == "__main__":
    app.run(debug=True)