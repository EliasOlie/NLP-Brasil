from github import Github
import os

def make_issue(token, title, body):

    g = Github(token)

    repo = g.get_repo("EliasOlie/NLP-Brasil")
    label = repo.get_label("phrase")
    repo.create_issue(title=title, body=body, labels=[label])