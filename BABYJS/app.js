const vm = require('vm');
const path = require("path");
const express = require('express');
const pug = require('pug');

const app = express()

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.get('/', function(req, res, next){
    let result = '';
    const code = req.query.code;

    if(code && code.length < 200){
        try {
            const result = vm.runInNewContext(code, {}, { timeout: 100 });
        } catch(e) {
            result = "err";
        }
    } else {
            result = "no code";
    }
    
    res.render("index", {"title": "Hello BABYJS", result});
});

module.exports = app;