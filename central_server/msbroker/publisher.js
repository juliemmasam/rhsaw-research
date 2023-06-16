const amqp = require("amqplib/callback_api")
const dotenv = require("dotenv")
dotenv.config()

const BROKER_URI = process.env.BROKER_URI

function broadcast_locspeed(loc_speed_data){
    amqp.connect(BROKER_URI, (conn_err, connection) => {
        if (conn_err){
            throw conn_err
        }

        connection.createChannel((chan_err, channel) => {
            if(chan_err){
                throw chan_err
            }

            const exchange = "train_locspeed"

            channel.assertExchange(exchange, "fanout", {durable: false})
            channel.publish(exchange, '', Buffer.from(loc_speed_data))
            console.log(`Sent the data ${loc_speed_data}`)

            setTimeout(() => {
                connection.close();
            }, 500)
        })
    })
}

module.exports = broadcast_locspeed