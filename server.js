// import
const express = require('express')
const morgan = require('morgan')
const cookieParser = require('cookie-parser')

const faceRouter = require('./routes/face_rec')
const recommendRouter = require('./routes/recommend_interest')
const chatBotRouter = require('./routes/chatbot')
const voiceRouter = require('./routes/voice')


// app setting
const app = express()

// server port 설정
app.set('port', 8000)

app.use(morgan('dev'))           // dev 용 서버 리셋

app.use('/face', faceRouter)            // 얼굴 인증 Router 연결
app.use('/recommend', recommendRouter)  // 관심사 추천 Router 연결
app.use('/chatbot', chatBotRouter)      // chatbot Router 연결
app.use('/voice, ', voiceRouter)        // 음성 인식 Router 연결

app.use(cookieParser())
app.use(express.json())
app.use(express.urlencoded({extended: true}))


// API 시작
// 처음 AI server 메인 페이지
app.get('/', (req, res)=>{
    res.send('AI Homepage')
})


// 지정된 URL 이 없을 경우
app.use((req,res, next)=>{
    res.status(404).send('Page is Not Found')
})

app.listen(8000, ()=>{
    console.log('AI server is Run!')

})