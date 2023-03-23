# #pip install PyGithub
import base64
import pandas as pd
import requests
from github import Github
import io
import mimetypes
import os



def upload_to_github(token, repo_name, file_path, file_name, commit_message):
    g = Github(token)
    print('ok1')
    repo = g.get_repo(repo_name)
    print('ok2')

    # with open(file_path, 'rb') as file:
    #     content = base64.b64encode(file.read()).decode('utf-8')
    with open(file_path, 'rb') as file:
        content = file.read()
        repo.create_file(os.path.basename(file_path), commit_message, content)

    print('ok3')

    # repo.create_file(file_name, commit_message, content)
   
    

def download_arquivo_excel(token, repo_name, file_name):
    
    g = Github(token)
    repo = g.get_repo(repo_name)
    print('----------------------------ok1')
    # path = 'caminho/para/arquivo.xlsx'
    path = 'stats-23_03_00_13.xlsx'
    file_content = repo.get_contents(path).content
    print('----------------------------ok2')
    decoded_content = base64.b64decode(file_content)
    print('----------------------------ok3')

    df = pd.read_excel(io.BytesIO(decoded_content))
    print('----------------------------ok4')
    print(df.head())

def ler_arquivo_excel(repo_name, file_name):
    url = f"https://github.com/{repo_name}/blob/main/{file_name}?raw=true"
    df = pd.read_excel(url, engine='openpyxl')

    print(df)

token = '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'
repo_name = 'joaomendescf/stats-fut'
file_path = 'dados_stats_inicio.xlsx'
file_name = 'dados_stats_inicio.xlsx'
commit_message = 'Adicionando arquivo stats-23_03_00_13'
branch = 'main'

def listar_repositorios(token):
    my_git = Github(token)
    for repo in my_git.get_user().get_repos():
        print(repo.name)

def listar_arquivos_repositorio(repositorio):
    my_git = Github(token)
    repo = my_git.get_repo(f'joaomendescf/{repositorio}')
    contents = repo.get_contents('')
    for content_file in contents:
        print(content_file)

# listar_repositorios()
# listar_arquivos_repositorio('stats-fut')
upload_to_github(token, repo_name, file_path, file_name, commit_message)
# download_arquivo_excel(token, repo_name, file_name)

ler_arquivo_excel(repo_name, file_name)


