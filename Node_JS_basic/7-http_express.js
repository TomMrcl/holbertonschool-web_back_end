const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];
  const output = ['This is the list of our students'];

  countStudents(databasePath)
    .then(() => {
      res.send(output.join('\n'));
    })
    .catch((err) => {
      output.push(err.message);
      res.send(output.join('\n'));
    });
});

app.listen(1245);

module.exports = app;
