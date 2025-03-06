from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'AI Engineer',
    'location': 'Abu Dhabi, UAE',
    'salary':' 20000 AED'
  },
  {
    'id': 2,
    'title': 'AI Developer',
    'location': 'Dubai, UAE',
    'salary':' 19000 AED'
  },
  {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Abu Dhabi, UAE',
    'salary':' 25000 AED'
  },
  {
    'id': 4,
    'title': 'Project Manager',
    'location': 'Milan, Italy',
  },
]

@app.route("/")
def hello_lawati():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
