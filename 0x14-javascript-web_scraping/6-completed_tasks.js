#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./6-completed_tasks.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasks = {};

  tasks.forEach((task) => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 0;
      }
      completedTasks[task.userId]++;
    }
  });

  console.log(completedTasks);
});
