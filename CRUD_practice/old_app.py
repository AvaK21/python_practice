# Import libraries
from flask import Flask, request, url_for, redirect, render_template


#Add to note to self the clone command: git clone
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id':1, 'date': '2023-06-01', 'amount': 100},
    {'id':2, 'date': '2023-06-02', 'amount': -200},
    {'id':3, 'date': '2023-06-03', 'amount': 300},
]
# Read operation
@app.route('/')
def get_transactions():

    return render_template('transactions.html', transactions = transactions)


# Create operation
@app.route('/add', methods =['GET','POST'])
def add_transaction():
    if request.method == 'POST':
        transaction = {
            'id' : len(transactions) + 1,
            'date' : request.form['date'],
            'amount' : float(request.form['amount'])
        }
        transactions.append(transaction)
        return redirect(url_for('get_transactions'))
    elif request.method == 'GET':
        return render_template('form.html')

# Update operation
@app.route('/edit/<int:transaction_id>', methods = ['GET','POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])
        for t in transactions:
            if t['id'] == transaction_id:
                t['date'] = date
                t['amount'] = amount
                break
        return redirect(url_for('get_transactions'))
    # for transaction in transactions:
    #     if transaction['id'] == transaction_id:
    #         return render_template('edit.html', transaction = transaction)

    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)

    return {"message": "Transaction not found so no editting"}, 404


# Delete operation

@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    for t in transactions:
        if t['id'] == transaction_id:
            transactions.remove(t)
            break
    return redirect(url_for("get_transactions"))
        

@app.route('/search', methods = ['GET', 'POST'])
def search_transactions():
    if request.method == 'POST':
        v_max = float(request.form['max_amount'])
        v_min = float(request.form['min_amount'])
        # list comprehension - [new_item for item in iterable if condition]
        filtered = [t for t in transactions if (v_min <= t['amount'] <= v_max)]
        return render_template('transactions.html', transactions = filtered)
    #line below has be added but not tested 
    return render_template('search.html')



# Run the Flask app - make sure it is the main script calling it, and not had been imported
#debug mode allows you to see the error message if there are any
if __name__ == '__main__':
    app.run(debug=True)

