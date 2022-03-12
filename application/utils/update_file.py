from github import Github
import json

def update_review_file(token: str,path:str, content:str, branch: str='main'):
    g = Github(token)
    repo = g.get_repo("EliasOlie/NLP-Brasil")
    sha = repo.get_contents(path=path).sha

    try:
        with open('./processamento/intents_review.json', 'r+', encoding='utf-8') as json_file:
            dados:dict = json.load(json_file)
    except FileNotFoundError:
        with open('backend/processamento/intents_review.json', 'r+', encoding='utf-8') as json_file:
            dados:dict = json.load(json_file)
    
    dados.update(content)

    try:
        repo.update_file(path=path, message="Uploaded to review", content=json.dumps(dados, ensure_ascii=False), sha=sha)
        print("Done!")
    except Exception as e:
        print(e)
