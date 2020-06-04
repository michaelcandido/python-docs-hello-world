from airtable import Airtable
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

AIRTABLE_KEY = 'keyIiyOZTJ7kdkOth'

app = Flask(__name__)
queries_tbl = Airtable(AIRTABLE_KEY, 'Queries')
feed_tbl = Airtable(AIRTABLE_KEY, 'FeedEntries')

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/get-feed')
def get_feed():
    pass

@app.route('/update-queries', methods=['POST'])
def update_queries():
    data = request.json
    if 'queries' not in data:
        raise BadRequest('missing queries property')
    
    query_ids = queries_tbl.get_all(fields='Query')
    queries_tbl.batch_delete(query_ids)

    query_records = [{'Query': q} for q in data['queries']]
    queries_tbl.batch_insert(query_records)
    return 'Success'