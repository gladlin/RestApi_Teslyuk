from flask import Flask, request, jsonify

app = Flask(__name__)  # будет помогать создавать API порты


@app.route('/hello_world', methods=['GET'])
def sayHelloWorld():
    data = {  # словарь с данными, которые будут возвращены
        1: "Hello World"
    }
    return jsonify(data)


@app.route('/users/', methods=['GET'])
def returnUserInfo():
    id = request.args.get("id")
    users = {
        1: {
            "name": "Alex",
            "age": 25
        },
        2: {
            "name": "Max",
            "age": 28
        },
        3: {
            "name": "Egor",
            "age": 15
        }
    }
    data = users[int(id)]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
