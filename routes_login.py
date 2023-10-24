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

@app.route('/login', method='POST')
def login():
    #ログイン処理、POSTのみ受付
    user_id = request.forms.decode().get('user_id')
    passwd = request.forms.decode().get('passwd')
    
    user = connection.query(BookUser.user_id).filter\
        (BookUser.user_id == user_id,\
            BookUser.passwd == passwd,\
                BookUser.delFlg == False).scalar()
    print(user)
    if user is not None:
        #認証成功
        auth = Auth()
        auth.add_auth(user)
        redirect(REDIRECT_AFTER_LOGIN)
    else:
        #認証失敗
        err_msg = urlpar.quote('認証に失敗しました')
        redirect(REDIRECT_AFTER_LOGOFF + '?error' + err_msg)
        
@app.route('/logout', method=['GET','POST'])
def logout():
    #ログオフ
    auth = Auth()
    auth.del_auth()
    redirect(REDIRECT_AFTER_LOGOFF)