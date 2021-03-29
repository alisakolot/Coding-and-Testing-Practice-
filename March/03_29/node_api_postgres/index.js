const express = require('express')
const bodyParser = require('body-parser')
const { response } = require('express')
const app = express()
const port = 3000

app.use(bodyParser.json())
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
)

// Route to look for GET request on the root URL (/) to return some json
app.get('/', (request, response) => {
    response.json({ info: 'Node.js, Express, and Postgress API'})
})


// Exporting functions from queries.js
const db = require('./queries')


// Setting HTTP request method
app.get('/users', db.getUsers)
app.get('/users/:id', db.getUserById)
app.post('/users', db.createUser)
app.put('/users/:id', db.updateUser)
app.delete('/users/:id', db.deleteUser)

// Set app to listen on post, set above
app.listen(port, () => {
    console.log(`App running on port ${port}.`)
})