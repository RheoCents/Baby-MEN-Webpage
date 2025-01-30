from flask import Flask, request, jsonify, render_template
from labexercise.remove_first_n_characters_from_a_string import *
from labexercise import linklist
from labexercise.Sorthing import *
from labexercise.GraphFunctions import Graph
from labexercise.stack import infix_to_postfix
from templates import *

app = Flask(__name__)
linked_list = linklist.LinkedList()
submitted_inputs_list = []
g = Graph()

g.add_edge("Taft Avenue", "Magallanes")
g.add_edge("Magallanes", "Ayala")
g.add_edge("Ayala", "Buendia")
g.add_edge("Buendia", "Guadalupe")
g.add_edge("Guadalupe", "Boni")
g.add_edge("Boni", "Shaw Boulevard")
g.add_edge("Shaw Boulevard", "Ortigas")
g.add_edge("Ortigas", "Santolan MRT")
g.add_edge("Santolan MRT","Araneta Center - Cubao")
g.add_edge("Araneta Center - Cubao", "Kamuning")
g.add_edge("Kamuning", "Quezon Avenue")
g.add_edge("Quezon Avenue", "North Avenue")

# LRT 2
g.add_edge("Recto", "Legarda")
g.add_edge("Legarda", "Pureza")
g.add_edge("Pureza", "V. Mapa")
g.add_edge("V. Mapa", "J. Ruiz")
g.add_edge("J. Ruiz", "Gilmore")
g.add_edge("Gilmore", "Betty Go Belmonte")
g.add_edge("Betty Go Belmonte", "Araneta Center - Cubao")
g.add_edge("Araneta Center - Cubao", "Anonas")
g.add_edge("Anonas", "Katipunan")
g.add_edge("Katipunan", "Santolan LRT")
g.add_edge("Santolan LRT", "Marikina")
g.add_edge("Marikina", "Antipolo")

# LRT 1
g.add_edge("Dr. Santos", "Ninoy Aquino")
g.add_edge("Ninoy Aquino", "PITX")
g.add_edge("PITX", "MIA")
g.add_edge("MIA", "Redemptorist")
g.add_edge("Redemptorist", "Baclaran")
g.add_edge("Baclaran", "EDSA")
g.add_edge("EDSA", "Libertad")
g.add_edge("Libertad", "Gil Puyat")
g.add_edge("Gil Puyat", "Vito Cruz")
g.add_edge("Vito Cruz", "Quirino")
g.add_edge("Quirino", "Pedro Gil")
g.add_edge("Pedro Gil", "United Nations")
g.add_edge("United Nations", "Central Terminal")
g.add_edge("Central Terminal", "Carriedo")
g.add_edge("Carriedo", "Doroteo Jose")
g.add_edge("Doroteo Jose", "Bambang")
g.add_edge("Bambang", "Tayuman")
g.add_edge("Tayuman", "Blumentrit")
g.add_edge("Blumentrit", "Abad Santos")
g.add_edge("Abad Santos", "R. Papa")
g.add_edge("R. Papa", "5th Avenue")
g.add_edge("5th Avenue", "Monumento")
g.add_edge("Monumento", "Balintawak")
g.add_edge("Balintawak", "Roosevelt")


#Connecting Terminals
g.add_edge("Taft Avenue", "EDSA")
g.add_edge("Doroteo Jose", "Recto")

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
    return render_template('stack.html')  

@app.route('/work3')
def work3():
    return render_template('queue.html') 

@app.route('/work4')
def work4():
    return render_template('lrtpath.html')

@app.route('/work5')
def work5():
    return render_template('sort.html')

@app.route('/work7')
def work7():
    return render_template('word_eater.html') 

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

@app.route('/sort', methods=['POST'])
def sort_array():
    data = request.json.get('array', [])
    sorter = Sortingsort()
    for item in data:
        sorter.add_data(item)
    sorted_list = sorter.bubble_sort()
    return jsonify(sorted_list)

@app.route('/word_eater', methods=['GET', 'POST'])
def word_eater():
    result_word = ""
    original_word = ""  # Variable to hold the original word
    if request.method == 'POST':
        original_word = request.form.get('input_word', '')
        if original_word:
            random_amount_to_be_eaten = random.randint(1, len(original_word))
            result_word = original_word[random_amount_to_be_eaten:]
    
    return render_template('word_eater.html', result_word=result_word, original_word=original_word)

@app.route('/linkedlist')
def linkedlist_page():
    return render_template(
        'linkedlist.html',
        linked_list_items=linked_list.list_LinkedList(),
        submitted_inputs=submitted_inputs_list
    )

@app.route('/add_remove', methods=['POST'])
def add_remove():
    data = request.form.get('data', '')
    action = request.form.get('action')


    if data:
      if action == 'add_start':
        linked_list.insert_at_beginning(data)
        submitted_inputs_list.append(data)
      elif action == 'add_end':
        linked_list.insert_at_end(data)
        submitted_inputs_list.append(data)
      elif action == 'remove_start':
        linked_list.remove_at_beginning()
      elif action == 'remove_end':
        linked_list.remove_at_end()
    else:
        if action == 'remove_start':
            linked_list.remove_at_beginning()
        elif action == 'remove_end':
            linked_list.remove_at_end()
        
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
        'stack.html',
        infix_expression=infix_expression,
        postfix_expression=postfix_expression,
        steps=steps_list
    )

@app.route('/work4', methods=['POST'])
def find_path():
    data = request.get_json()
    start = data['start']
    end = data['end']
    
    print(f"Start: {start}, End: {end}")
    print(g.vert_dict) # Log the start and end values

    if start not in g.vert_dict or end not in g.vert_dict:
        print(f"Invalid start or end: {start}, {end}")
        return jsonify([])  # Return an empty list if invalid
    else:           
        paths = g.find_paths(start, end)
        print("Found paths:", paths)  # Log the found paths
        return jsonify(paths)


if __name__ == "__main__":
    app.run(debug=True)