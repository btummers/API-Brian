from flask import * #flask = python web framework
import json, time

app = Flask (__name__) #creating the flask app with the project __name__

@app.route('/', methods=['GET']) #endpoint
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Pagina Laden Succesvol!', 'Timestamp': time.time()} 
    json_dump = json.dumps(data_set) # line 8 + 9 returns text as json

    return json_dump #return data as a json file 

    #when line 6 gets called, it will create the data on line 8 with the current timestamp, 
    #and then it will return the data into a data file (line 11)

@app.route('/user/', methods=['GET']) 
def request_page():
    user_query = str(request.args.get('user')) #/user/?user=Brian

    data_set = {'Page': 'Request', 'Message': f'Request for {user_query}', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

 #if the user requests a query in the link of the page (see line 18) it'll change the message to "Request for {user_query}" 

if __name__ == '__main__':
    app.run(port=7777) #run the app on port 7777 (5000 is default)
