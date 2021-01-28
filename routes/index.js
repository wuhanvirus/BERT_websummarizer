var express = require('express');
var router = express.Router();
const { PythonShell } = require('python-shell');
let options = {
  mode: 'text',
  pythonPath: '',
  pythonOptions: ['-u'],
  scriptPath: '',
  args: '',
  encoding: 'utf8'
};

/* GET home page. */
router.get('/', function (req, res, next) {
  res.render('index.ejs', {});
});

router.post('/', function (req, res, next) {
  options.args = req.body.plain;
  // var summ = '';
  console.log(options);
  // console.log(__dirname+'/../test.py');
  PythonShell.run(__dirname + '/../test.py', options, function (err, results) {
    if (err) throw err;

    //받아온 메시지 전처리 과정
    console.log(results[0]);
    let data = results[0].replace(`b\'`, '').replace(`\'`, '');
    let buff = Buffer.from(data, 'base64');
    let text = buff.toString('utf-8');
    // var summ = text;
    // console.log(summ);
    // 글자0 글자로 되면 원래 글자 그대로 내뱉게만들자잇
    // 값기다렸다가 내뱉게 ex (로딩등으로, 프론트엔드 로딩화면도 구현하자)
    res.render('index2.ejs', { plaint: req.body.plain, sum: text })
  });

  // res.render('index2.ejs', { plaint: req.body.plain, sum: sum2 })
});
//홈페이지 새로고침안되면서 할 수 있는 방법이 있나 찾아보자잇!
module.exports = router;