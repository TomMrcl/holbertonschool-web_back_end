# ES6 Basic

Ce dossier contient des exercices ES6 basiques (fonctions, const/let, arrow, spread, rest, etc.).

Fichiers inclus:

- `0-constants.js`
- `1-block-scoped.js`
- `2-arrow.js`
- `3-default-parameter.js`
- `4-rest-parameter.js`
- `5-spread-operator.js`
- `6-string-interpolation.js`
- `7-getBudgetObject.js`
- `8-getBudgetCurrentYear.js`
- `9-getFullBudget.js`
- `10-loops.js`
- `11-createEmployeesObject.js`
- `12-createReportObject.js`
ES6_basicES6_classes# ES6 Basic

## Description

This project covers the fundamentals of **ECMAScript 6 (ES2015)** — the major update to JavaScript that introduced modern syntax and features. Each task focuses on replacing older ES5 patterns with their cleaner ES6 equivalents.

## Learning Objectives

By the end of this project, you should be able to explain:

- What ES6 is and the new features it introduced
- The difference between `const`, `let`, and `var`
- Block-scoped variables and why they matter
- Arrow functions and how they handle `this`
- Default function parameters
- Rest and spread operators (`...`)
- Template literals (string interpolation)
- Object shorthand syntax and computed property names
- ES6 method properties
- `for...of` loops vs `for...in`

## Requirements

- Ubuntu 20.04 LTS
- Node.js `20.x.x`
- npm `9.x.x`
- Jest, Babel, ESLint (see setup below)

## Setup

```bash
# Install Node.js 20.x.x
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y

# Install project dependencies
npm install
```

## Scripts

| Command | Description |
|---|---|
| `npm run lint` | Run ESLint |
| `npm run check-lint` | Lint all JS files |
| `npm run dev` | Run a file with Babel |
| `npm test` | Run Jest tests |
| `npm run full-test` | Lint + Jest |

## Tasks

| File | Description |
|---|---|
| `0-constants.js` | Use `const` and `let` instead of `var` |
| `1-block-scoped.js` | Block-scoped variables to avoid hoisting issues |
| `2-arrow.js` | Rewrite function using arrow syntax |
| `3-default-parameter.js` | Use default parameter values |
| `4-rest-parameter.js` | Use rest syntax to count arguments |
| `5-spread-operator.js` | Concatenate arrays and string with spread |
| `6-string-interpolation.js` | Use template literals |
| `7-getBudgetObject.js` | Object property shorthand syntax |
| `8-getBudgetCurrentYear.js` | Computed property names |
| `9-getFullBudget.js` | ES6 method properties |
| `10-loops.js` | Replace `for...in` with `for...of` |
| `11-createEmployeesObject.js` | Create an object with a dynamic key |
| `12-createReportObject.js` | Build a report object with a method property |

## Author

Holberton School — Web Back End track
