const express = require('express')
const app = express()

an = 0

app.get('/', function (req, res) {
    res.header('Access-Control-Allow-Origin', '*');
    res.end("Hello World!");
    an += 1
    console.log(an);
});
app.listen(1234, function () {
    console.log('Server app listening on port 1234!')
})
