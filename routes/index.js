var express = require('express');
var router = express.Router();
var request = require('request');
var tr = require('../textrank');

/* GET home page. */
router.get('/', function (req, res, next) {
    res.render('index.ejs', {});
});
router.post('/', function (req, res, next) {
    var plain_text = req.body.plain;        //  20자 이하면 그대로 반환하게
    var btn = false;
    var result_text = "";
    var beforePos = 0;
    var pos = 0;
    // 나중에 스택 이용해서 작은 따옴표까지 처리할 수 있을듯
    while(1)
    {
        let foundPos = plain_text.indexOf("\"", pos);
        btn = !btn;
        if (foundPos == -1) 
        {
            result_text += ((plain_text.substring(beforePos, plain_text.length)).replace(/([.?!])(\s*)/g, "$1\n")).replace(/\n+/g, "\n");
            break;
        }
        if(btn)
            result_text += ((plain_text.substring(beforePos, foundPos)).replace(/([.?!])(\s*)/g, "$1\n")).replace(/\n+/g, "\n");
        else
            result_text += "\"" + plain_text.substring(beforePos, foundPos) + "\""; 
        pos = foundPos + 1;
        beforePos = pos;    
    }
    // plain_text = plain_text.replace(/\.\s+/g, ".\n");
    // console.log (plain_text);
    console.log (result_text);
    // var textrank = new tr(plain_text);
    var textrank = new tr(result_text);
    var sum = textrank.getSummarizedThreeText()

    if(sum)
        res.render('index2.ejs', { plaint: req.body.plain, sum: sum});
    else
        res.render('index2.ejs', { plaint: req.body.plain, sum: "텍스트의 길이 혹은 문장의 수가 부적합합니다.\n\nThe length of the text or the number of sentences is invalid." });

    // 글자0 글자로 되면 원래 글자 그대로 내뱉게만들자잇
    // 값기다렸다가 내뱉게 ex (로딩등으로, 프론트엔드 로딩화면도 구현하자)
});
//홈페이지 새로고침 안되면서 할 수 있는 방법이 있나 찾아보자잇!
module.exports = router;