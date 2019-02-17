from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/app')
def map():
    return '<iframe width="100%" height="100%" frameborder="0" src="https://sp4356.carto.com/builder/03213329-6f03-42ae-a64e-78dde47fa554/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>'

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/lda')
def lda():
  return render_template('topicModelingVis.html')

if __name__ == "__main__":
	app.run(debug=True)
