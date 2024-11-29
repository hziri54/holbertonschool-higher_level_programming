from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data():
    """Lire les données à partir du fichier JSON."""
    with open('products.json') as f:
        return json.load(f)

def read_csv_data():
    """Lire les données à partir du fichier CSV."""
    products = []
    with open('products.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convertir les données en format adéquat
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')  # Paramètre source (json ou csv)
    product_id = request.args.get('id', type=int)  # Paramètre optionnel id

    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        return render_template('product_display.html', error="Wrong source")

    # Si un id est spécifié, filtrer par id
    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
