var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const helmet = require("helmet");
const favicon = require('express-favicon');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var turlRouter = require('./routes/turl');

var app = express();
app.use(
  helmet.contentSecurityPolicy({
      directives: {
          defaultSrc: ["'self'", 'https://ka-f.fontawesome.com', 'https://fonts.gstatic.com'],
          scriptSrc: ["'self'", 'https://ka-f.fontawesome.com',"https://kit.fontawesome.com",], //kit추가, unsafe지움
          styleSrc: ["'self'","'unsafe-inline'", 'https://cdn.jsdelivr.net/','https://ka-f.fontawesome.com', 'https://fonts.googleapis.com'], //unsafe필요, jsdelivr추가
          connectSrc: ["'self'", 'https://ka-f.fontawesome.com'],
          reportUri: '/report-violation',   // endpoint to get violation reports
      },
      reportOnly: false,  // true for nonblocking mode, just to see violations
      safari5: false
}));
app.use(helmet.dnsPrefetchControl());
app.use(helmet.expectCt());
app.use(helmet.frameguard());
app.use(helmet.hidePoweredBy());
app.use(helmet.hsts());
app.use(helmet.ieNoOpen());
app.use(helmet.noSniff());
app.use(helmet.permittedCrossDomainPolicies());
app.use(helmet.referrerPolicy());
app.use(helmet.xssFilter());
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(favicon(__dirname + '/public/favicon.ico'));

app.use('/', indexRouter);
//app.use('/', express.static('public'));
app.use('/users', usersRouter);
app.use('/turl', turlRouter);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};
  // console.log(req);
  // render the error page
  res.status(err.status || 500);
  res.render('error',{errmsg:err.message, errurl:req.url, errnum: err.status});
});

module.exports = app;