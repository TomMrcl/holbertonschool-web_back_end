const fs = require('fs');

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    const fields = {};
    for (const student of students) {
      const parts = student.split(',');
      const field = parts[3];
      const firstName = parts[0];
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    }
    resolve(fields);
  });
});

module.exports = readDatabase;
