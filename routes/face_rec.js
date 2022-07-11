const express = require('express')
const {spawn} = require("child_process");
const router = express.Router()

router.get('/', (req, res)=>{
    res.send('face focus!');
})

router.get('/check', (req,res)=>{
    console.log('AI server is run')
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python',["/Users/js/Desktop/Work/Sinor/Sinor_AI/face_rec/main.py"]);
    pythonProcess.stdout.on('data', (data) => {
        // Do something with the data returned from python script
        console.log(data.toString());
        res.write(data)
        res.end('<<< Done >>>>')
    });
})

module.exports = router