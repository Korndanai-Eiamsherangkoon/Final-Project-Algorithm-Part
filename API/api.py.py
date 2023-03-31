from collections import deque
import datetime
#from flask import Flask, request, jsonify
# from prettytable import PrettyTable

#app = Flask(__name__)

# @app.route('/api', methods=['GET'])
# def getnameageid():
#     name = request.args.get('name')
#     age = request.args.get('age')
#     id = request.args.get('id')
#     d = {'name': name, 'age': age, 'id': id}
#     return jsonify(d)

if __name__ == "__main__":
    app.run()

def generate_items():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char1 = "A"
    i = 1
    while True:
        yield f"{char1}{str(i).zfill(2)}"
        i += 1
        if i == 100:
            char1_index = alphabet.index(char1)
            char1_index += 1
            if char1_index == len(alphabet):
                char1_index = 0
                # reset values to A01 at the start of each day
                if datetime.datetime.now().hour == 0:
                    char1 = "A"
                    i = 1
                else:
                    char1 = alphabet[char1_index]
                    i = 0
                    
class Queue:

    def __init__(self):
        self.queue = deque()
        self.tickets = generate_items()

    def add(self, appointment):
        appointment.ticket = next(self.tickets)
        self.queue.appendleft(appointment)

    def remove(self, doctor):
        appointments = [appointment for appointment in self.queue if appointment.doctor == doctor]
        if not appointments:
            print(f"No appointments found for doctor {doctor}.")
        else:
            appointment = appointments[-1]
            self.queue.remove(appointment)
            print(f"Removed appointment for patient with id {appointment.patient_id} for doctor {doctor}.")

    @app.route('/api', methods=['GET'])
    def walkin(self, patient_id, doctor):
        patient_id = request.args.get('id')
        doctor = request.args.get('drroom')

        current_datetime = datetime.datetime.now()
        appointment = Appointment(current_datetime, current_datetime, patient_id, doctor)
        self.add(appointment)
        print(f"Walk-in patient with id {patient_id} has been added to the queue for doctor {doctor}.")
queue = Queue()
class Appointment:
    def __init__(self, start_time, end_time, patient_id, doctor, ticket=None):
        self.start_time = start_time
        self.end_time = end_time
        self.patient_id = patient_id
        self.doctor = doctor
        self.ticket = ticket      



# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/api', methods=['GET', 'POST'])
# def returnascii():
#     name = request.args.get('name')
#     age = request.args.get('age')
#     id = request.args.get('id')
#     # if name is None or age is None or id is None:
#     #     return jsonify({'error': 'One or more query parameters are missing'})
#     d = {'name': name, 'age': age, 'id': id}
#     return jsonify(d)

# if __name__ == "__main__":
#     app.run()



# http://localhost:5000/api?name=John&age=30&id=123

# app = Flask(__name__)

# @app.route('/api', methods = ['GET'])
# def returnascii():
#     d = {}
#     inputchr = str(request.args['query'])
#     answer = str(inputchr)
#     d['output'] = answer
#     return d



# if __name__ =="__main__":
#     app.run()
queue.walkin(1005,"Dr. Jane")