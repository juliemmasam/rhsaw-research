const mongoose = require("mongoose")
const Schema = mongoose.Schema, ObjectId = Schema.ObjectId

const LocSpeedSchema = new Schema({
    _id: ObjectId,
    train_id: Number, 
    location: {
        latitude: Number, 
        longitude: Number, 
    }, 
    speed: Number, 
    timestamp: String
})

const LocSpeed = mongoose.model("loc_speed", LocSpeedSchema)

module.exports = LocSpeed