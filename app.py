from re import DEBUG
from flask import Flask, render_template ,jsonify

app = Flask(__name__)

JOBS = [{
  'id ': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 1,00,000'
},
{
  'id ': 2,
  'title': 'Backend Engineer',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,00,000'
},
{
  'id ': 3,
  'title': 'Data Analyst',
  'location': 'Chennai, India',
  'salary': 'Rs. 12,00,000'
},{
  'id ': 4,
  'title':'Frontend Engineer',
  'location': 'Remote',
  'salary': 'Rs. $150,000'
},
]


@app.route('/')
def hello_jovian():
  return render_template('home.html',jobs=JOBS,company_name="Jovian")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)