#!/usr/bin/node
// To query the starwars api of holberton

const request = require('request');
const argv = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
const charURL = [];

request(url, function (err, res, body) {
  if (!err & res.statusCode === 200) {
    body = JSON.parse(body);
    body.characters.forEach((char) => {
      const promise = new Promise((resolve) =>
        request(char, function (err, res, body) {
          if (!err & res.statusCode === 200) {
            body = JSON.parse(body);
            resolve(body.name);
          }
        })
      );
      charURL.push(promise);
    });
  }
  Promise.all(charURL).then((value) => {
    value.forEach((name) => {
      console.log(name);
    });
  });
});
