#!/usr/bin/node
const request = require('request');

urlTodos = process.argv[2]

request(urlTodos, function (error, response, body) {
    if (error) {
        console.error('error:', error);}
    const tasks = JSON.parse(body);

    let user_completed = {};
    for (let task of tasks) {
	if (task.completed) {
	    if (user_completed[task.userId]) {
		user_completed[task.userId] += 1
	    }
	    else {
		user_completed[task.userId] = 1
	    }
	}
    }

    console.log(user_completed);
});
