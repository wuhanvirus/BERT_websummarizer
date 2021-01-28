const { PythonShell } = require('python-shell');
let options = {
    mode: 'text',
    pythonPath: '',
    pythonOptions: ['-u'],
    scriptPath: '',
    args: '최근 중국에서 폐 페스트 환자가 발생해 혹여나 우리나라에서도 전염 사례가 발생하지 않을까 걱정하는 사람들이 많다. 특히 올해 초 한국인 관광객도 예방적으로 격리되어 국내 유입에 대한 우려가 더욱 크다. 증상 발생 후 24시간 이내에 페스트균이 들어간 신체 부위의 국소 림프절 부위에 통증이 생긴다. 페스트의 치료에 사용할 수 있는 항생제는 겐타마이신, 스트렙토마이신, 독시사이클린, 레보플록사신 등이 있다.',
    encoding: 'utf8'
};
PythonShell.run(__dirname + '/test.py', options, function (err, results) {
    if (err) throw err;

    //받아온 메시지 전처리 과정
    let data = results[0].replace(`b\'`, '').replace(`\'`, '');
    let buff = Buffer.from(data, 'base64');
    let text = buff.toString('utf-8');
    console.log('text:', text);
});