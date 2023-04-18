from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/status', methods=['GET'])
def get_status():
    # code to retrieve status information from public services
    status = {'service1': 'up', 'service2': 'down', 'service3': 'partial outage'}
    return jsonify(status)


if __name__ == '__main__':
    app.run(debug=True)
