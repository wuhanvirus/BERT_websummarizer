from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
from flask_restful import reqparse
from summarizer import Summarizer
import base64
from goose3 import Goose
from goose3.text import StopWordsKorean 

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록
model = Summarizer()
g_e = Goose()
g_k = Goose({ 'stopwords_class' : StopWordsKorean })

class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('text', type=str)
            parser.add_argument('line', type=bool)
            # parser.add_argument('email', type=str)
            # parser.add_argument('user_name', type=str)
            # parser.add_argument('password', type=str)
            args = parser.parse_args()
            _text = args['text']
            _threeswitch = args['line']

            if _threeswitch:
                result = model(_text, num_sentences=3)
            else:
                result = model(_text)
            
            summary = "".join(result)
            # _userEmail = args['email']
            # _userName = args['user_name']
            # _userPassword = args['password']
            return {
                'text': summary
            }
        except Exception as e:
            return {'error': str(e)}

class CreateUser2(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('text', type=str)
            
            args = parser.parse_args()
            t_url = args['text']
            # print("py"+t_url)
            article = g_e.extract(url=t_url)
            result = article.cleaned_text
            if len(result) == 0 or len(result) < len(article.title):
                article = g_k.extract(url=t_url)
                result = article.cleaned_text
            
            tmp = model(result)
            summary = "".join(tmp)

            return {
                'plain': result,
                'sum': summary
            }
        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/fapi')
api.add_resource(CreateUser2, '/turl')

if __name__ == '__main__':
    app.run(debug=True)