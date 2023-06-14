const express = require("express")
const router = express()

router.use((req, res, next) => {
    next()
})

router.use(express.json())

router.route("/:id")
    .get((req, res) => {
        res.send(`The get request for train ${req.params.id} was issued`)
    })
    .post((req, res) => {
        console.log(req.body)
        res.send(`The post request for train ${req.params.id} was issued`)
    })

module.exports = router