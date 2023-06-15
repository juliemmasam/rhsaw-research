const mongoose = require("mongoose")
const Schema = mongoose.Schema

const LocSpeedSchema = new Schema({
    train_id: Number,
    loc_speed: [
        {
            location: {
                latitude: Number, 
                longitude: Number, 
            }, 
            speed: Number, 
            timestamp: String
        }
    ] 
}, {timestamps: true})

const LocSpeed = mongoose.model("loc_speed", LocSpeedSchema)

module.exports = LocSpeed