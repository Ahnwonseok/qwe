const express = require('express')
const {spawn} = require("child_process");
const router = express.Router()

router.get('/', (req, res)=>{
    res.send('chatbot focus!');
})

module.exports = router