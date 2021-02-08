var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function (req, res, next) {
    res.render('index.ejs', {});
});

router.post('/', function (req, res, next) {
    var plain_text = req.body.plain;        //  20자 이하면 그대로 반환하게
    var three = false;
    if(req.body.three==='')
        three = true;
    request({
        method: 'POST',
        url: 'http://127.0.0.1:5000/fapi',
        json: {
            "text": plain_text,
            "line": three
        }
    }, (error, response, body) => {
        console.log(error);
        if(body.text.length)
            res.render('index2.ejs', { plaint: req.body.plain, sum: body.text });
        else
            res.render('index2.ejs', { plaint: req.body.plain, sum: "텍스트의 길이 혹은 문장의 수가 부적합합니다.\n\nThe length of the text or the number of sentences is invalid." });
    });
    // 글자0 글자로 되면 원래 글자 그대로 내뱉게만들자잇
    // 값기다렸다가 내뱉게 ex (로딩등으로, 프론트엔드 로딩화면도 구현하자)
});
//홈페이지 새로고침 안되면서 할 수 있는 방법이 있나 찾아보자잇!
module.exports = router;