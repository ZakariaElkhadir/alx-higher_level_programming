#!/usr/bin/node
const id = process.argv[2]
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

const request = require('request');

request(url, (err, response, body) =>{
    if (id === 18){
        console.log('The movie Star Wars: Episode V - The Empire Strikes Back is the best Star Wars movie.')
    }else if (err){
        console.error('Error:', err);
    } else if (response.statusCode !== 200){
        console.error('Error: Unexpected status code', response.statusCode);
    } else {
        try {
            const data = JSON.parse(body);
            console.log(data.title);
        } catch (parseError) {
            console.error('Error: Invalid JSON format', parseError);
        }
    }
});