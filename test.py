from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
from flask_restful import reqparse
# from summarizer import Summarizer
import base64
from goose3 import Goose
from goose3.text import StopWordsKorean
# from flask_cors import CORS

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록
g_e = Goose()
g_k = Goose({ 'stopwords_class' : StopWordsKorean })

class CreateUser2(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('text', type=str)
            
            args = parser.parse_args()
            t_url = args['text']
            article = g_e.extract(url=t_url)
            result = article.cleaned_text
            if len(result) == 0 or len(result) < len(article.title):
                article = g_k.extract(url=t_url)
                result = article.cleaned_text
            print(result)
            return {
                'plain': result
            }
        except Exception as e:
             return {'error': "123"}

api.add_resource(CreateUser2, '/turl')

if __name__ == '__main__':
    app.run(debug=True)