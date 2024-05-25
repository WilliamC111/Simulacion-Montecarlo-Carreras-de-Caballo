from flask import Flask, render_template, request, redirect, url_for
from horse import Horse
from simulation import Simulation

app = Flask(__name__)
simulation = None

@app.route('/')
def index():
    return render_template('carga.html')

@app.route('/carga_indice', methods=['POST'])
def carga_indice():
    global simulation
    if request.method == 'POST':
        number_race = int(request.form['inputNumber'])
        simulation = Simulation(number_race=number_race)
        return redirect(url_for('simulation_results'))

@app.route('/simulation_results')
def simulation_results():
    global simulation
    if simulation:
        races = simulation.get_list_race()
        horses = races[0].get_horses() if races else []
        return render_template('simulacion.html', horses=horses)
    else:
        return "No se ha inicializado la simulación."

@app.route('/show_results', methods=['POST'])
def show_results():
    global simulation
    if simulation:
        races = simulation.get_list_race()
        return render_template('table.html', races=races)
    else:
        return "No se ha inicializado la simulación."

@app.route('/table_calculate')
def table_calculate():
    global simulation
    if simulation:
        winners = simulation.get_winner_for_race()
        wins_by_breed = simulation.count_wins_by_race()
        wins_by_age = simulation.count_wins_by_age()
        top_horses = simulation.get_podio()
        all_horses = simulation.horses  # Obtener todos los caballos de la simulación

        return render_template('table.html', horses=all_horses, races=simulation.get_list_race(), winners=winners, wins_by_breed=wins_by_breed, wins_by_age=wins_by_age, top_horses=top_horses)
    else:
        return "No se ha inicializado la simulación."

@app.route('/bar_chart')
def bar_chart():
    global simulation
    if simulation:
        winners_by_horse = {}
        for race in simulation.get_list_race():
            winner = race.get_winner()
            if winner:
                horse_name = winner.get_name()
                if horse_name in winners_by_horse:
                    winners_by_horse[horse_name] += 1
                else:
                    winners_by_horse[horse_name] = 1
        return render_template('bar_chart.html', winners_by_horse=winners_by_horse)
    else:
        return "No se ha inicializado la simulación."

if __name__ == '__main__':
    app.run(debug=True)
