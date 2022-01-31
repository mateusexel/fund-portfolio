const express = require('express');
const res = require('express/lib/response');
const app = express();
const { spawn } = require('child_process');
const { json } = require('express/lib/response');
const port = process.env.PORT || 3000
app.listen(port, () => console.log('listening at 3000'));
app.use(express.static('public'));
app.use(express.json({limit: '1mb'}))
// var output2 = require("./output2.json");
app.get('/api', (request, response) =>{
    // console.log('oioi')
    // res.send('oioi');
    response.json(output2);
    // console.log(output2)
} );

app.post('/apicnpj', (request, response) => {
    var jsonFile;
    const childPython = spawn('python', ['createjson.py', request.body.body])
    childPython.stdout.on('data', (data) => {
        jsonFile = JSON.parse(data)
    })
    
    childPython.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`)
    })
    childPython.on('close', (code) => {
        response.json(jsonFile);
        console.log(`child process exited whi code: ${code}`)
    })
    
    // var output2 = require("./output2.json");
    // console.log(request.body.body);
    // response.json(output2);


});