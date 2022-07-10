const express = require('express')
const {spawn} = require("child_process");
const app = express()

let data_ = null

app.set('port', 8000)

app.get('/', (req, res)=>{
    console.time('ai test')
    console.log('api is run')
    console.log(data_)
    console.timeEnd('ai test')
    res.end('end!')
})

app.listen(8000, ()=>{
    console.log('server is run')
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python',["/Users/js/Desktop/Work/Sinor/Sinor_AI/face_rec/main.py"]);
    pythonProcess.stdout.on('data', (data) => {
        // Do something with the data returned from python script
        console.log(data.toString());
        data_ = data.toString()
    });

})