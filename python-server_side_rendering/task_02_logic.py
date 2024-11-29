from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    # Ouvrir et charger le fichier JSON
    with open('items.json') as f:
        data = json.load(f)
    
    # Extraire la liste des items du fichier JSON
    items_list = data['items']
    
    # Passer les items à la template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
