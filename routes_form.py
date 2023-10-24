'''
フォーム関係の画面遷移
'''
from bottle import Bottle, jinja2_template as template,\
    request, redirect
from bottle import response
import routes
from models import connection, Books
from utils.util import Utils
from utils.auth import Auth

#routesからappを読み込む
app = routes.app
auth = Auth()

#登録フォームを処理する
@app.route('/add', method=['GET','POST'])
def add():
    #認証確認
    auth.check_login()
    registId = ""
    form = {}
    kind = "登録"
    if request.method == 'GET':
        #id指定された場合
        #編集画面
        if request.query.get('id') is not None:
            book = connection.query(Books).filter\
                (Books.id_==request.query.get('id')).first()
            form['name'] = book.name
            form['volume'] = book.volume
            form['author'] = book.author
            form['publisher'] = book.publisher
            form['memo'] = book.memo
            registId = book.id_
            
