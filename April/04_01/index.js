// Connect to a database, create a Client Object with usernames/ports
// "pg" is the node library name
const {Client} = require("pg")

// to create new client you need to create an adj obj
// port 5432 is default for psql
const client = new Client({
    user: "al",
    password: "",
    host: "alisakolot", 
    port: 5432,
    database: "mydatabase"
})

// promises
// finally ends the connection 
client.connect()
.then(() => console.log("Connected Succesfuly!"))
.then(() => client.query("select * from employees"))

.catch(e => console.log)
.finally(() => client.end())