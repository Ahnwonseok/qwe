const express = require('express')
const {spawn} = require("child_process");
const router = express.Router()

router.get('/', (req, res)=>{
    res.send('recommend_re focus!');
})


module.exports = router