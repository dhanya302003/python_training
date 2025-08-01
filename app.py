from flask import Flask ,render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
    
@app.route('/myname')
def printMyname():
    return"your name"

@app.route('/home')
def loadHomeHtml():
    return render_template("home.html")

@app.route('/about')
def loadaboutHtml():
    return render_template("about.html")

@app.route('/contact')
def loadcontactHtml():
    return render_template("contact.html")



if __name__ == '__main__':
    app.run()
    