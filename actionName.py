from actionNameTypes import actionNameArgs, SampleOutput
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/actionName', methods=['POST'])
def actionNameHandler():
  args = actionNameArgs.from_request(request.get_json())
  print(args)
  # business logic here
  return SampleOutput().to_json()

if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')
