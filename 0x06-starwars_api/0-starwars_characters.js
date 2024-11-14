#!/usr/bin/node
// To query the starwars api of holberton

const request = require('request');
const argv = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
const charURL = [];

request(url, function (err, res, body) {
  if (!err & res.statusCode === 200) {
    body = JSON.parse(body);
    // Query all character urls
    body.characters.forEach((char) => {
      // Save them as promises to fulfil after getting all
      const promise = new Promise((resolve) =>
        request(char, function (err, res, body) {
          if (!err & res.statusCode === 200) {
            body = JSON.parse(body);
            resolve(body.name);
          }
        })
      );
      // Save the romise in a list
      charURL.push(promise);
    });
  }
  // Run all promise using promise.all
  Promise.all(charURL).then((value) => {
    value.forEach((name) => {
      console.log(name);
    });
  });
});
