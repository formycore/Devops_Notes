<<<<<<< HEAD
var request = require('supertest');
var app = require('../index.js');
describe('GET /will', function() {
    it('respond with hello world', function(done) {
        request(app).get('/will').expect('{ "response": "Hello World" }', done);
    });
=======
var request = require('supertest');
var app = require('../index.js');
describe('GET /will', function() {
    it('respond with hello world', function(done) {
        request(app).get('/will').expect('{ "response": "Hello World" }', done);
    });
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
});