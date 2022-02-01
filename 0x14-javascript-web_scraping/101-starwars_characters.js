#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, async function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  for (const character of data.characters) {
    await new Promise(function (resolve, reject) {
      request(character, function (error, response, body) {
        if (error) {
          reject(error);
          return;
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
