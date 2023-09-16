from flask import Flask, jsonify
#from gevent.pywsgi import WSGIServer

app = Flask(__name__)

# seeing all the entries    
@app.route("/get", methods=['GET'])
def get_all_aplications():
    """ Essa função retorna todas aplicações"""
    aplications = [{'nome':'Site','status':'ON'},{'nome':'App','status':'OFF'},{'nome':'Login','status':'UNINSTABLE'}]
    list_aplications = []
    for item in aplications:
        aplications_dict  = {
            "nome": item['nome'],
            "status": item['status']
            }

        list_aplications.append(aplications_dict)

    return jsonify({'applications':list_aplications})

@app.route("/save", methods=['POST'])
def create_aplication():
    """ Essa função salva uma nova aplicação"""
    message = {'status':'Aplicação cadastrada com sucesso'}

    return jsonify(message)

@app.route("/update/", methods=['PATCH'])
def updating_aplication():
    """ Essa função atualiza uma aplicação"""
    message = {'status':'Aplicação atualizada com sucesso'}

    return jsonify(message)

@app.route("/delete/", methods=['DELETE'])
def deleting_aplication():
    """ Essa função deleta uma aplicação"""

    message = {'status':'Aplicação deletada com sucesso'}

    return jsonify(message)


if __name__ == '__main__':
    # Debug/Development
     app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()