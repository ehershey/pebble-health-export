from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    data = request.form.get('data')

    time, steps, yaw,pitch,vmc,light,mask,heart = data.split(',')

    print(time, steps, mask)
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
