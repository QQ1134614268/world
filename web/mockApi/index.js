const fs = require("fs");
const path = __dirname;
const files = fs.readdirSync(path + "/mockList");
const mockList = [];
files.forEach(function (filename) {
    let model = require(path + "/mockList/" + filename);
    mockList.push(...model);
});

function handleMock(app) {
    mockList.forEach(func => {
        func(app);
    });
}

module.exports = handleMock;