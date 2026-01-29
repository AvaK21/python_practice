from flask import Flask, make_response, request

app = Flask(__name__)

#The data has previous to the function that uses it in the file
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]
@app.route("/")
def index():
    return "Hello World"

@app.route("/no_content")
def no_content():
    return ({"message":"No content found"}, 204)

@app.route("/exp")
def index_explicit():
    resp = make_response({"message":"This is a specific message it is important that you remember what you got for birthday last year!!"})
    resp.status_code = 200
    return resp

@app.route("/data")
def get_data():
    try:
        #Chick if 'data' exidts and has a length greater than 0
        if data and len(data) > 0:
            #Return a JSON reponse with a message indicating the length of the data
            return({"message":f"Data of length {len(data)} found"})
        else:
            #If data is empty, return a JSON response with a 500 internal server error status code
            return ({"message":"Data is empty"},500)
    except NameError:
        #Handle the case where 'data' not defined
        return({"message":"Data not found"},404)

@app.route("/name_search")
def name_search():
    query = request.args.get('q')


    if query is None:
        resp = make_response({"message":"Missing input"}, 400)
        resp.status_code = 400
        return resp
    #Check if the query parameter is present byt invalid (empty or numeric)
    elif query.strip() == "" or query.isdigit():
        return {"message":"Invalid input"}, 422
    
    #Iterate through the 'data' list to search fir the matching person
    for person in data:
        #Check is the query string is present in the person's first name (case-insensitive)   
        if query.lower() in person['first_name'].lower():
            return person, 200
    #if no matching person, return a JSON response with a message and a 404 Not Found
    resp = make_response({"message":"Person not found"})
    resp.status_code = 404
    return resp     

@app.get("/count")
def count():
    try:
        return {"message":f"Length of data is {len(data)}"}, 200
    except NameError:
        return {"message":"Data was not defined"}, 500

@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    for person in data:
        if str(id) == person['id']:
            return person, 200
    return ({"message":"That id doesn't match any person in the data on the server"}, 404)

@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    for person in data:
        if str(id) == person['id']:

            data.remove(person)
            return({"message":f"Person with id: {id} has been deleted"}, 200)
    return({"message":f"Person with id: {id} not found"}, 404)

@app.route("/person", methods=['POST'])
def add_by_uuid():
    #Get tje JSON fata from the incoming request
    new_person = request.get_json()

    if not new_person:
        return ({"message":"Person data not present to data"}, 422)
    try:
        data.append(new_person)
        return ({"message":"New person added"}, 200)
    except NameError:
        return ({"message":"Data not defined to add a person"}, 500)
@app.errorhandler(404)
def api_not_found(error):
    #A custom error handler for 404 Not Found errors
    #It is triggered whenever a 404 error occurs within the Flask application
    return ({"message":"API not found"}, 404)

@app.errorhandler(500)
def server_error(error):
    return({"message":"Internal server error (custom)"}, 500)
#-------------------
#Similarly you can add a global Error Handler for 500 (internal server error)  also.

# You can register a global error handler in Flask for any unhandled exceptions by using:
@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500

#-------------------
# You can deliberately raise an exception to test the global handler. Add the following route before your error handlers:

# @app.route("/test500")
# def test500():
#     raise Exception("Forced exception for testing")
#command: curl http://localhost:5000/test500

#--------------------
