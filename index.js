// PRO 100 - ATM Machine
const chalk = require('chalk');

console.log(chalk.greenBright("JavaScript: Running JavaScript File"))
console.log()

const argument = process.argv; 

const json = JSON.parse(argument[2].replaceAll("'", '"'))
console.log(json)
console.log()

const fs = require('fs');

const jsonString = JSON.stringify(json, null, 2);
const filePath = 'C:/Users/TayoYuva/Documents/Mine/Studies/White Hat JR/Project/C100/cred.json';

fs.writeFile(filePath, jsonString, 'utf-8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  } else {
    console.log(chalk.greenBright("Success:"), chalk.yellow('JavaScript: Data has been written to', filePath));
    console.log()
}
});
