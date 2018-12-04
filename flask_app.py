
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import xml_parsing

app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route("/")

def html_render():
   quote, author = xml_parsing.parsing()
   print(quote)
   print(author)
    #quote = "hi"
   return render_template('html_page.html', quote = quote, author = author)
    #return 'Welcome!!! Motivational Quote For You'

if __name__ == '__main__':
    app.run()
