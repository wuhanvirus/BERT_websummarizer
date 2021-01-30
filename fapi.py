from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
from flask_restful import reqparse
from summarizer import Summarizer
import base64

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록
model = Summarizer()

class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('text', type=str)
            # parser.add_argument('email', type=str)
            # parser.add_argument('user_name', type=str)
            # parser.add_argument('password', type=str)
            args = parser.parse_args()
            _text = args['text']
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

api.add_resource(CreateUser, '/fapi')

if __name__ == '__main__':
    app.run(debug=True)