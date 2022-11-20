""" from flask import Flask, render_template
import urllib.request, json
import os

site = Flask(__name__)                    #yorwihgoihjoi4tjgrnvoienwglksdnmggklerwn
@site.route("/url")                          #wityauioreghiewhjoigrhjioetjfioeqjfioenw

def html():
    return "<p>Index</p>"

if __name__ == "frong.py":                #ryu98qur39cmqu90uexq0u039rjdoiwejfioewfr
    site.run(debug = True)

@site.route("/")
def get_index():
    url = "https://lec-hacks-project.kavya12k.repl.co/".format(os.environ.get("TMDB_API_KEY"))

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template ("index.html", index=dict["results"])


@site.route("/index")
def get_index_list():
    url = "https://lec-hacks-project.kavya12k.repl.co/".format(os.environ.get("TMDB_API_KEY"))

    response = urllib.request.urlopen(url)
    index = response.read()
    dict = json.loads(index)

    index = []

    for ind in dict["results"]:
        ind = {
            "title": ind["title"],
            "overview": ind["overview"],
        }
        
        index.append(ind)

    return {"results": index} """

from flask import Flask, render_template, url_for, request, redirect
import frong as frong

site = Flask (__name__)

@site.route('/')
def index():
    return render_template('index.html')

@site.route('/', methods=["POST"])
def hello():
    enter_phrase = request.form["phrase"]

    output = "you are " + enter_phrase
    return redirect(url_for('hello'))
     
@site.get('/rate')
def rate():
    text = request.args.get("text")
    print(text)
    rating = frong.main(text)
    print("\n\n", rating)
    return  render_template('index.html', rating = rating)

@site.put('/')
def contact():
    return render_template('index.html')
 
if __name__ == "__main__":
    site.run(debug=True)
