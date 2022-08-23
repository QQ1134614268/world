function testMock(app) {
    app.get("/mock/api/news", function (req, res) {
        res.json({
            name: "tom"
        });
    });
}

function testPostMock(app) {
    app.post("/mock/api/news", function (req, res) {
        console.log(req.body);
        setTimeout(function () {
            res.json({
                code: 0,
                data: "success",
                desc: ""
            });
        }, 500);
    });
}

module.exports = [testMock, testPostMock];