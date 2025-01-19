from flask import Flask, render_template, request
from labexercise import linklist, stack
from labexercise.stack import infix_to_postfix
from templates import *

app = Flask(__name__)
linked_list = linklist.LinkedList()
submitted_inputs_list = []

@app.route('/')
def index():    
    return render_template('upload.html')

@app.route('/works')
def work():
    return render_template('works.html')

@app.route('/work1')
def work1():
    return render_template('linkedlist.html')  

@app.route('/work2')
def work2():
    return render_template('convert.html')  

@app.route('/work6')
def work6():
    return render_template('word-eater.html') 

@app.route('/work4')
def work4():
    return render_template('lrtpath.html')

@app.route('/contactus')
def contactus():
    return render_template('contact.html')

@app.route('/aboutus')
def aboutus():    
    return render_template('about_us.html') 

@app.route('/babyboyleader')
def leader():    
    return render_template('babyboy_leader.html') 

@app.route('/babyboy1')
def mem1():    
    return render_template('babyboy_1.html') 

@app.route('/babyboy2')
def mem2():    
    return render_template('babyboy_2.html') 

@app.route('/babyboy3')
def mem3():    
    return render_template('babyboy_3.html') 

@app.route('/babyboy4')
def mem4():    
    return render_template('babyboy_4.html') 

@app.route('/babyboy5')
def mem5():    
    return render_template('babyboy_5.html') 

@app.route('/babyboy6')
def mem6():    
    return render_template('babyboy_6.html')

@app.route('/linkedlist')
def linkedlist_page():
    return render_template(
        'linkedlist.html',
        linked_list_items=linked_list.list_LinkedList(),
        submitted_inputs=submitted_inputs_list
    )

@app.route('/add1', methods=['POST'])
def insert_end():
    data = request.form.get('data', '')
    if data:
        linked_list.insert_at_end(data) 
        submitted_inputs_list.append(data) 
    return render_template(
        'linkedlist.html',
        linked_list_items=linked_list.list_LinkedList(),
        submitted_inputs=submitted_inputs_list
    )

@app.route('/add2', methods=['POST'])
def insert_beginning():
    data = request.form.get('data', '')
    if data:
        linked_list.insert_at_beginning(data) 
        submitted_inputs_list.append(data) 
    return render_template(
        'linkedlist.html',
        linked_list_items=linked_list.list_LinkedList(),
        submitted_inputs=submitted_inputs_list
    )

@app.route('/remove_at_beginning', methods=['POST'])
def remove_at_beginning():
    linked_list.remove_at_beginning()
    return render_template(
        'linkedlist.html',
        linked_list_items=linked_list.list_LinkedList(),
        submitted_inputs=submitted_inputs_list
    )

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