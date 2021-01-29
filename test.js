const {PythonShell} = require('python-shell');
var pyshell = new PythonShell('test2.py');

// sends a message to the Python script via stdin
pyshell.send('hello');

pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
  
});
let j =0;
for(let i=0; i<10000000000;i++){
    j++;
}
pyshell.send('yeah');
pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
  });

// end the input stream and allow the process to exit
pyshell.end(function (err) {
  if (err) throw err;
  console.log('finished');
});