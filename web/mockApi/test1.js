function testMock1(app) {
    app.get("/mock/api/news1", function (req, res) {
        res.json({
            name: "jack"
        });
    });
}

module.exports = [testMock1];