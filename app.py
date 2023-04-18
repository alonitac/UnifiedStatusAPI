from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/status', methods=['GET'])
def get_status():
    # TODO fetch data from the db...
    # TODO arrange the data in the defined scheme

    example_output = {
        "targets": [
            {
                "name": "github",
                "endpoint": "https://www.githubstatus.com/api/v2/status.json",
                "type": "REST",
                "services": [
                    {
                        "name": "pages",
                        "lastTimestamp": "",
                        "status": "OK",
                        "dimensions": {
                            "region": "us-east-1"
                        }
                    }
                ]
            }
        ]
    }
    return jsonify(example_output)


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
