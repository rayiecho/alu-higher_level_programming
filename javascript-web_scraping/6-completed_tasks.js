#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const completed = {};
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        if (completed[todos[i].userId] === undefined) {
          completed[todos[i].userId] = 1;
        } else {
          completed[todos[i].userId]++;
        }
      }
    }
    console.log(completed);
  }
});
