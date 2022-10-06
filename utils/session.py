import bottle
from beaker.middleware import SessionMiddleware
'''
セッション管理クラス
beakerセッションを作成する
'''
class Session():
    '''
    コンストラクタ
    '''
    def __init__(self):
        self.session_opt = {
            'session.type': 'file',
            'session.cookie_expires': True,
            'session.data_dir': './tmp',
            'session.auto': True
        }

    '''
    セッションを作る
    セッション開始時にappを指定する
    '''
    def create_session(self, app):
        apps = SessionMiddleware(app, self.session_opt)
        return apps

    '''
    セッションの値を取得する
    '''
    def get_session(self, key):
        session = bottle.request.environ.get('beaker.session')
        if key not in session:
            return None
        return session[key]

    '''
    セッションに値をセットする
    '''
    def set_session(self, key, value):
        session = bottle.request.environ.get('beaker.session')
        session[key] = value
        session.save()

    '''
    セッションの値を削除する
    '''
    def del_session(self, key):
        session = bottle.request.environ.get('beaker.session')
        del session[key]
        session.save()

    '''
    セッションをクリアする
    '''
    def clear_session():
        session = bottle.request.environ.get('beaker.session')
        session.delete()