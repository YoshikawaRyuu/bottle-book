'''
練習プログラム
'''
from bottle import Bottle,\
    jinja2_template as template,\
        static_file, request, redirect
        
from bottle import response, run, TEMPLATE_PATH
import psycopg2
import psycopg2.extras
import os

#DB接続情報
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'book_data'
DB_USER = 'book_userY'
DB_PASS = 'ryu0110'

def get_connection():
    '''
    データベースの接続を行う
    '''
    dsn = 'host={host} port={port} dbname={dbname} \
        user={user} password={password}'
    dsn = dsn.format(user=DB_USER, password=DB_PASS, \
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME)
    return psycopg2.connect(dsn)

#Bottleアプリ利用
app = Bottle()

TEMPLATE_PATH.append(os.path.abspath('user/views'))
@app.route('/', method=['GET', 'POST'])
def index():
    return "Hello World"

@app.route('/add', method=['GET','POST'])
def add():
    #ユーザー登録フォームのHTML
    form_html = """<html>
    <head>登録フォーム</head>
    <body>
    <form action="/add" method="post">
    ユーザーID:<input type="text" name="user_id" value="<!--user_id-->" /><br />
    パスワード:<input type="text" name="passwd" value="<!--passwd-->" /><br />
    email:<input type="text" name="email" value="<!--email-->" /><br />
    氏:<input type="text" name="user_shi" value="<!--user_shi-->" /><br />
    名:<input type="text" name="user_mei" value="<!--user_mei-->" /><br />
    <input type="submit" value="確認" name="text"/>
    </form>
    </body>
    </html>
    """
    #ユーザー登録 確認画面のHTML
    confirm_html = """<html>
    <head>確認</head>
    <body>
    <form action="/regist" method="post">
    ユーザーID:<!--user_id--><br />
    パスワード:<!--passwd--><br />
    email:<!--email--><br />
    氏:<!--user_shi--><br />
    名:<!--user_mei--><br />
    <input type="hidden" name="user_id" value="<!--user_id-->" />
    <input type="hidden" name="passwd" value="<!--passwd-->" />
    <input type="hidden" name="email" value="<!--email-->" />
    <input type="hidden" name="user_shi" value="<!--user_shi-->" />
    <input type="hidden" name="user_mei" value="<!--user_mei-->" />
    <input type="submit" value="back" name="next"/>&nbsp;&nbsp;
    <input type="submit" value="regist" name="next"/>
    </form>
    </body>
    </html>
    """
    #GETでアクセスされたら
    if request.method == 'GET' or request.forms.get('next') == 'back':
        return form_html.replace('<!--user_id-->', '').\
        replace('<!--passwd-->', '').\
        replace('<!--email-->', '').\
        replace('<!--user_shi-->', '').\
        replace('<!--user_mei-->', '')
    else:
        #POSTされたフォームの値を取得する
        form = {}
        form['user_id'] = request.forms.decode().get('user_id')
        form['passwd'] = request.forms.decode().get('passwd')
        form['email'] = request.forms.decode().get('email')
        form['user_shi'] = request.forms.decode().get('user_shi')
        form['user_mei'] = request.forms.decode().get('user_mei')
        
        if request.forms.get('next') == 'back':
            #戻る処理
            html = form_html
        else:
            #確認処理
            html = confirm_html
            
        #受け取った値を置換する
        #メソッドは重ね掛けできる
        return html.replace('<!--user_id-->', form['user_id']).\
        replace('<!--passwd-->', form['passwd']).\
        replace('<!--email-->', form['email']).\
        replace('<!--user_shi-->', form['user_shi']).\
        replace('<!--user_mei-->', form['user_mei'])
        
@app.route('/regist', method=["POST"])
def regist():
    if request.forms.get('next') == 'back':
        #確認画面から戻るボタンを押す
        #登録フォームに戻る
        response.status = 307
        response.set_header("Location", '/add')
        return response
    else:
        #フォームから値を取得する
        user_id = request.forms.decode().get('user_id')
        passwd = request.forms.decode().get('passwd')
        email = request.forms.decode().get('email')
        user_shi = request.forms.decode().get('user_shi')
        user_mei = request.forms.decode().get('user_mei')
        
        #SQLを記入する
        sql = """insert into book_user \
        (user_id, passwd, email, user_shi, user_mei, del) \
        values \
        (%(user_id)s, %(passwd)s, %(email)s, %(user_shi)s, %(user_mei)s, false)"""
        #入力する値の辞書を設定する
        val = {'user_id':user_id, 'passwd':passwd,\
            'email':email, 'user_shi':user_shi,\
            'user_mei':user_mei}
        with get_connection() as con:#データベースの接続を取得
            with con.cursor() as cur:#カーソルを取得
                cur.execute(sql, val)
            con.commit()
        redirect('/add')
                
@app.route('/user_list')
def user_list():
    sql = """SELECT user_id, email, user_shi, \
        user_mei FROM book_user \
        WHERE del = false \
        ORDER BY user_id ASC;"""
    with get_connection() as con:
        with con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            #dict型で受け取りたいので上記のようにオプション設定
            cur.execute(sql)
            rows = cur.fetchall()
            #下記の内包表記を挟む必要がある
            rows = [dict(row) for row in rows]
    return template('user_list.html', rows=rows)

if __name__ == '__main__':
    run(app=app, host='0.0.0.0', port=8889, reloader=True, debug=True)