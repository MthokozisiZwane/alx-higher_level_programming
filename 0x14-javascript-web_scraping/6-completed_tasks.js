#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(todo => {
      if (todo.completed) {
        completedTasks[todo.userId] = (completedTasks[todo.userId] || 0) + 1;
      }
    });

    console.log(completedTasks);
  }
});
