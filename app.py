from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Дані про потяги і квитки
trains = [
    {"number": "123", "name": "Intercity", "origin": "Київ", "destination": "Львів", "departure_time": "2024-07-16 08:00", "arrival_time": "2024-07-16 12:00"},
    {"number": "456", "name": "Express", "origin": "Одеса", "destination": "Харків", "departure_time": "2024-07-16 10:00", "arrival_time": "2024-07-16 16:00"}
]

tickets = []

@app.route('/')
def list_trains():
    return render_template('list_trains.html', trains=trains)

@app.route('/buy', methods=['GET', 'POST'])
def buy_ticket():
    if request.method == 'POST':
        train_number = request.form['train_number']
        departure_time = request.form['departure_time']
        seat = request.form['seat']
        tickets.append({'train_number': train_number, 'departure_time': departure_time, 'seat': seat})
        return redirect(url_for('list_trains'))
    return render_template('buy_ticket.html', trains=trains)

if __name__ == '__main__':
    app.run(debug=True)
