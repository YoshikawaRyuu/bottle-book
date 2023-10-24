'''
ログイン
ログアウト
の処理を扱う
'''
from bottle import Bottle, jinja2_template as template,\
    request, redirect
from bottle import response
import routes
from models import connection, BookUser
from utils.session import Session
from utils.auth import Auth
import urllib.parse as urlpar

#リダイレクトするパス
REDIRECT_AFTER_LOGIN  = '/list'
REDIRECT_AFTER_LOGOFF = '/'

app = routes.app

@app.route('/')
def index():
    #ログイン前
    #ログイン時にエラーがあれば、error引数に内容がセット
    err_msg = request.query.error
    if err_msg is None:
        err_msg = None
        #pass
        #err_msg = urlpar.unquote(err_msg)
    return template('login.html', error=err_msg)
