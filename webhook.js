var https = require("follow-redirects").https;
var fs = require("fs");

var options = {
  method: "POST",
  hostname: "webhooks.amplify.eu-west-1.amazonaws.com",
  path: "/prod/webhooks?id=f27d6957-be49-4666-b708-f089573dc3fb&token=rdFnrsvjZk9qGmOj25WZMW6K9KmpmJLNy98kTfzFU&operation=startbuild",
  headers: {},
  maxRedirects: 20,
};

var req = https.request(options, function (res) {
  var chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function (chunk) {
    var body = Buffer.concat(chunks);
    console.log(body.toString());
  });

  res.on("error", function (error) {
    console.error(error);
  });
});

req.end();
