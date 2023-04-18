from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/status', methods=['GET'])
def get_status():
    # code to retrieve status information from public services
    status = {'service1': 'up', 'service2': 'down', 'service3': 'partial outage'}
    return jsonify(status)


@app.route('/api/alert', methods=['POST'])
def post_alert():
    # code to receive and process alerts from monitoring systems
    alert = request.get_json()
    # send alert notification to appropriate channels (e.g. email, Slack, PagerDuty)
    return jsonify({'message': 'Alert received'})


if __name__ == '__main__':
    app.run(debug=True)