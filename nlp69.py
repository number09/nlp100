from flask import Flask
from flask import request
import pymongo

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    site_html = '''
    <html>
        <body>
            <form method="post" action="/">
                <input type="text" name="name">
                <input type="text" name="aliase">
                <input type="text" name="tag">
                <input type="submit" value="send">
            </form>
            {0}
        </body>
    </html>
    
    
    '''

    if request.method == 'POST':
        result = search(request)


    return site_html.format(result)


def search(request):

    searchkey = []
    res = ''

    if request.form['aliase']:
        searchkey.append({'aliases.name': request.form['aliase'].strip()})

    if request.form['name']:
        searchkey.append({'name': request.form['name'].strip()})

    if request.form['tag']:
        searchkey.append({'tags.value': request.form['tag'].strip()})

    client = pymongo.MongoClient()
    nlp_db = client.nlp
    collection = nlp_db.nlpcollection

    result = collection.find({'$and': searchkey})
    for post in result:
       res = res + str(post) + '<br>'

    return res
