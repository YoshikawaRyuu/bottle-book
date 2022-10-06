import bottle
import urllib.parse as urlpar

class Auth():
    #認証キー
    AUTH_KEY = 'user_id'
    #Beakerセッション名
    BEAKER_SESSION_NAME = 'beaker.session'
    #認証エラーメッセージ
    ERROR_MSG_FOR_AUTH  = '認証されていません'
    '''
    コンストラクタ
    '''
    def __init__(self):
        pass
    '''
    認証セッションを追加
    '''
    def add_auth(self, user_id):
        session = bottle.request.environ.get(self.BEAKER_SESSION_NAME)
        session[self.AUTH_KEY] = user_id
        session.save()
    '''
    認証セッションを削除
    '''
    def del_auth(self):
        session = bottle.request.environ.get(self.BEAKER_SESSION_NAME)
        del session[self.AUTH_KEY]
        session.save()
    '''
    認証チェック
    '''
    def check_auth(self):
        session = bottle.request.environ.get(self.BEAKER_SESSION_NAME)
        if self.AUTH_KEY in session:
            return True
        else:
            return False
    '''
    認証していない
    ログイン画面に飛ばす
    '''
    def check_login(self):
        flg = self.check_auth()
        if flg == False:
            err_msg = urlpar.quote(self.ERROR_MSG_FOR_AUTH)
            bottle.redirect('/?error=' + err_msg)        