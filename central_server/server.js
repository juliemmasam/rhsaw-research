const dotenv = require("dotenv")
const mongoose = require("mongoose")
const express = require("express")

dotenv.config()
const DB_URI = process.env.DB_URI

const server = express()
const trains = require("./trains")
server.use('/trains', trains)

mongoose.connect(DB_URI, { useNewUrlParser: true, useUnifiedTopology: true})
.then((results) => {
    console.log("Connection to the database is complete")
    server.listen(3000, ()=>{
        console.log("The server is listening to requests")
    })    
})