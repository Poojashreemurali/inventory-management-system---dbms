from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data (replace with your actual data)
inventory_items = [
    {"id": 1, "name": "Laptop", "quantity": 10, "price": 1200},
    {"id": 2, "name": "Keyboard", "quantity": 20, "price": 30},
    {"id": 3, "name": "Mouse", "quantity": 15, "price": 15}
]

@app.route('/')
def index():
    return render_template('index.html', items=inventory_items)

@app.route('/add_item', methods=['POST'])
def add_item():
    # Get form data
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    
    # Add item to inventory_items (replace with your actual database operation)
    inventory_items.append({"id": len(inventory_items) + 1, "name": name, "quantity": quantity, "price": price})
    
    # Redirect to home page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
