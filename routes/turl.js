var express = require('express');
var router = express.Router();
var request = require('request');
var tr = require('../textrank');

/* GET home page. */
router.get('/', function (req, res, next) {
    res.render('index.ejs', {});
});

router.post('/', function (req, res, next) {
    var t_url = req.body.text_url;        //  20자 이하면 그대로 반환하게
    var textrank;
    request({
        method: 'POST',
        url: 'http://127.0.0.1:5000/turl',
        json: {
            "text": t_url
        }
    }, (error, response, body) => {
        console.log(error);
        if(body.error)
            res.render('index2.ejs', { plaint: t_url, sum: "죄송합니다. 입력한 URL에서 본문을 찾지 못했습니다.\n\nSorry, the body was not found at the URL you entered." });
        else if(body.plain.length)
        {
            var textrank = new tr(body.plain);
            var sum = textrank.getSummarizedThreeText()
            console.log(body.plain);
            console.log(sum);
            if(sum)
                res.render('index2.ejs', { plaint: body.plain, sum: sum });
            else
                res.render('index2.ejs', { plaint: body.plain, sum: "텍스트의 길이 혹은 문장의 수가 부적합합니다.\n\nThe length of the text or the number of sentences is invalid." });
        }
        else
            res.render('index2.ejs', { plaint: body.plain, sum: "죄송합니다. 입력한 URL에서 본문을 찾지 못했습니다.\n\nSorry, the body was not found at the URL you entered." });
    });
    // 값기다렸다가 내뱉게 ex (로딩등으로, 프론트엔드 로딩화면도 구현하자)
});
//홈페이지 새로고침 안되면서 할 수 있는 방법이 있나 찾아보자잇!
module.exports = router;