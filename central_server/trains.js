const LocSpeed = require("./models/loc_speed")
const publish = require("./msbroker/publisher")
const express = require("express")
const router = express()

router.use(express.json())

router.route("/new_train")
    .post((req, res) => {
        const loc_speed_data = new LocSpeed({
            train_id: req.body.train_id, 
            loc_speed: []
        }) 
        
        loc_speed_data.save()
        .then((result) => res.send(result))
        .catch((err) => console.log(err))
    })


router.route("/loc_speed_data/:id")
    .get((req, res) => {
        res.send(`The get request for train ${req.params.id} was issued`)
    })
    .post((req, res) => {  
        LocSpeed.updateOne(
            { train_id: req.body.train_id }, 
            { $push: { loc_speed: req.body.data } }
        )
        .then((result) => res.send(result.acknowledged))
        .catch((err) => console.log(err))

        // Publish to message broker
        publish.broadcast_locspeed(req.body.train_id)
    })

module.exports = router