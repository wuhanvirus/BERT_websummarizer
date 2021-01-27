var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index.ejs',{});
});

router.post('/',function(req, res, next){
  res.render('index2.ejs', { plaint : req.body.plain , sum : req.body.plain })
});
//홈페이지 새로고침안되면서 할 수 있는 방법이 있나 찾아보자잇!
module.exports = router;