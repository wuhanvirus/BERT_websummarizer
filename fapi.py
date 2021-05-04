from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
from flask_restful import reqparse
from summarizer import Summarizer
import base64
from goose3 import Goose
from goose3.text import StopWordsKorean
# from flask_cors import CORS

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
# CORS(app)
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
<<<<<<< HEAD
=======
            # parser.add_argument('email', type=str)
            # parser.add_argument('user_name', type=str)
            # parser.add_argument('password', type=str)
>>>>>>> d371e5a441c0761b6195a60b5e932c047b881e9a
            args = parser.parse_args()
            _text = args['text']
            _threeswitch = args['line']

            if _threeswitch:
                result = model(_text, max_length=450, num_sentences=3)
            else:
                result = model(_text, max_length=450)
            
            summary = "".join(result)
<<<<<<< HEAD
=======
            # _userEmail = args['email']
            # _userName = args['user_name']
            # _userPassword = args['password']
>>>>>>> d371e5a441c0761b6195a60b5e932c047b881e9a
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
            article = g_e.extract(url=t_url)
            result = article.cleaned_text
            if len(result) == 0 or len(result) < len(article.title):
                article = g_k.extract(url=t_url)
                result = article.cleaned_text
            
            tmp = model(result, max_length=450)
            summary = "".join(tmp)
<<<<<<< HEAD
            print(summary)
=======
>>>>>>> d371e5a441c0761b6195a60b5e932c047b881e9a
            return {
                'plain': result,
                'sum': summary
            }
        except Exception as e:
            return {'error': str(e)}

<<<<<<< HEAD
#   for chrome extensions
=======
>>>>>>> d371e5a441c0761b6195a60b5e932c047b881e9a
# class CreateUser3(Resource):
#     def post(self):
#         try:
#             parser = reqparse.RequestParser()
#             parser.add_argument('text', type=str)
#             parser.add_argument('text2', type=str)
#             parser.add_argument('text3', type=str)
#             parser.add_argument('text4', type=str)
#             parser.add_argument('text5', type=str)
#             parser.add_argument('text6', type=str)
#             parser.add_argument('text7', type=str)
#             parser.add_argument('text8', type=str)
#             parser.add_argument('text9', type=str)
#             parser.add_argument('text10', type=str)
            
#             t_url=[]
#             summary = []

#             args = parser.parse_args()
#             t_url.append(args['text'])
#             t_url.append(args['text2'])
#             t_url.append(args['text3'])
#             t_url.append(args['text4'])
#             t_url.append(args['text5'])
#             t_url.append(args['text6'])
#             t_url.append(args['text7'])
#             t_url.append(args['text8'])
#             t_url.append(args['text9'])
#             t_url.append(args['text10'])
            
#             for i in t_url:
#                 article = g_e.extract(url=i)
#                 result = article.cleaned_text
#                 if len(result) == 0 or len(result) < len(article.title):
#                     article = g_k.extract(url=i)
#                     result = article.cleaned_text
                
#                 tmp = model(result, max_length=450)
#                 summary.append("".join(tmp))

#             return {
#                 'sum': summary[0],
#                 'sum2': summary[1],
#                 'sum3': summary[2],
#                 'sum4': summary[3],
#                 'sum5': summary[4],
#                 'sum6': summary[5],
#                 'sum7': summary[6],
#                 'sum8': summary[7],
#                 'sum9': summary[8],
#                 'sum10': summary[9]
#             }
#         except Exception as e:
#             return {'error': str(e)}

api.add_resource(CreateUser, '/fapi')
api.add_resource(CreateUser2, '/turl')
# api.add_resource(CreateUser3, '/gturl')

if __name__ == '__main__':
    app.run(debug=True)