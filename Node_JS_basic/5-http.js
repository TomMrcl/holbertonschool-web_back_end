const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/students') {
    const databasePath = process.argv[2];
    const outputLines = ['This is the list of our students'];
    countStudents(databasePath)
      .then(() => {
        res.end(outputLines.join('\n'));
      })
      .catch((err) => {
        outputLines.push(err.message);
        res.end(outputLines.join('\n'));
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
