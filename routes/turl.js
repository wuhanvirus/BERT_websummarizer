var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function (req, res, next) {
    console.log('1');
    res.render('index.ejs', {});
});

router.post('/', function (req, res, next) {
    var t_url = req.body.text_url;        //  20자 이하면 그대로 반환하게
    request({
        method: 'POST',
        url: 'http://127.0.0.1:5000/turl',
        json: {
            "text": t_url
        }
    }, (error, response, body) => {
        console.log(error);
        if(body.error)
            res.render('index2.ejs', { plaint: t_url, sum: "입력한 URL에 문제가 있을 수 있습니다. \n확인 부탁드립니다.\n\nThere may be a problem with the URL you entered. Please check." });
        else if(body.sum.length)
            res.render('index2.ejs', { plaint: body.plain, sum: body.sum });
        else
            res.render('index2.ejs', { plaint: body.plain, sum: "텍스트가 짧거나, 문장 수가 너무 적습니다.\n\nShort text or too few sentences." });
    });
    // 값기다렸다가 내뱉게 ex (로딩등으로, 프론트엔드 로딩화면도 구현하자)
});
//홈페이지 새로고침 안되면서 할 수 있는 방법이 있나 찾아보자잇!
module.exports = router;