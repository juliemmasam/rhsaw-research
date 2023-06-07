const express = require("express")
const server = express()

const trains = require("./trains")

server.use('/trains', trains)

server.listen(3000, ()=>{
    console.log("The server is listening to requests")
})
