import requests
from flask import Flask, render_template, request
from gpt.qa import askGPT
from config import Config
from requests.auth import HTTPBasicAuth


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def post():
    question = request.form['question']
    # Perform action on the question
    answer = "This is your answer to the question: \n" + askGPT(question) 
    return answer

@app.route('/jira', methods=['GET'])
def jira():
    # Get the JQL query from the request parameters
    jql_query = request.args.get('jql')

    # Define the Jira API endpoint
    url = "https://gauraang.atlassian.net/rest/api/3/search"

    auth = HTTPBasicAuth(
        Config.JIRA_EMAIL, 
        Config.JIRA_API_KEY
    )
    


    # Define the Jira API headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Define the Jira API query parameters
    params = {
        "jql": 'project = TTO'
    }

    # Send the request to Jira
    response = requests.get(
        url, 
        headers=headers, 
        params=params, 
        auth=auth
        )

    # Return the Jira API response
    return response.json()

if __name__ == '__main__':
    app.run()
