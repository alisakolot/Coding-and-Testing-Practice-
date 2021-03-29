const Pool = require('pg').Pool
const pool = new Pool({
  user: 'me',
  host: 'localhost',
  database: 'mydatabase',
  password: 'password',
  port: 5432,
})

// Create Endpoints that display all users

// GET all users

const getUsers = (request, response) => {
    pool.query('SELECT * FROM users ORDER BY id ASC', (error, results) => {
        if (error) {
            throw error
        }
        response.status(200).json(results.rows)
    })
}

// GET a single user by ID
const getUserById = (request, response) => {
    const id = pareseInt(request.params.id)

    pool.query('SELECT * FROM users WHERE id = $1', [id], (error, results) => {
        if (error) {
            throw error
        }
        response.status(200).json(results.rows)
    })
}

// POST  a new user/adding a new user

const createUser = (request, response) => {
    const {name, email} = request.body

    pool.query('INSERT INTO users (name, email) VALUES ($1, $2', [name, email],  (error, results) => {
        if (error) {
            throw error
        }
        response.status(200).json(results.rows)
    })
}

// PUT updated data in an existing user, modifying the data that exists
// *can make the same call over and over and produce the same result, 
// **POST makes the same call but continuously make users with the same data

const updateUser = (request, response) => {
    const id = parseInt(request.params.id)
    const {name, email} = request.body
    
    pool.query(
        'UPDATE users SET name = $1, email $2 WHERE id = $3', 
        [name, email, id], 
        (error, results) => {
            if (error) {
                throw error
            }
            response.status(200).json(result.rows)
        }
    )
}



// DELETE a user

const deleteUser = (request, response) => {
    const id = parseInt(request.params.id)

    pool.query('DELETE FROM users WHERE id = $1', [id], (error, results) => {
        if (error) {
            throw error
        }
        response.status(200).json(results.rows)
    })
}

// Exporting CRUD functions in a REST API by creating an object of functions:

module.exports = {
    getUsers, 
    getUserById, 
    createUser, 
    updateUser, 
    deleteUser, 
}