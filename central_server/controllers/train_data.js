const mongoose = require("mongoose")

const LocSpeed = require("../models/loc_speed")

function addLocSpeedInfo(loc_data, res){
    var {train_id, loc_speed_data} = loc_data
    return "Train data addition"
}

function getLocSpeedData(query, res){
    var {train_id, start_time, end_time} = query
    return "Train location data"   
}

module.exports = {
    addLocSpeedInfo: addLocSpeedInfo, 
    getLocSpeedData: getLocSpeedData
}