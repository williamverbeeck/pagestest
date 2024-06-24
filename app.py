import requests  
from flask import Flask, render_template, request  
  
app = Flask(__name__)  
  
@app.route('/', methods=['GET', 'POST'])  
def home():  
    # Fetch the list of repositories from the GitHub organization  
    org_url = "https://api.github.com/orgs/SEMICeu/repos"  
    response = requests.get(org_url)  
    if response.status_code == 200:  
        repos = response.json()  
        repo_names = [repo['name'] for repo in repos]  
    else:  
        repo_names = []  
  
    # Filter the repo list based on the search query  
    search_query = request.form.get('search', '')  
    if search_query:  
        repo_names = [repo for repo in repo_names if search_query.lower() in repo.lower()]  
  
    return render_template('index.html', repos=repo_names, search_query=search_query)  
  
if __name__ == '__main__':  
    app.run(debug=True)  
