var request = require('request')
request = request.defaults({jar: true})
var jar = request.jar()
var url = 'https://www.minds.com/api/v1/authenticate'
request.get({
    url: url,
    jar: jar
  },
  function(err, res, body) {
    request.post({
        url: url,
        jar: jar,
        form: {
          'username' : 'zippypippytippy',
          'password': 'Obama08*'
        },
        headers: { 'x-xsrf-token': jar.getCookies(url)[2].value }
      },
      function(err, res, body) {
        request.get({
            url: 'https://www.minds.com/api/v1/notifications/all',
            jar: jar,
            headers: { 'x-xsrf-token': jar.getCookies(url)[2].value }
          },
          function(err, res, body) {
            json = JSON.parse(body)
            console.dir(json.notifications[0], {depth: null, colors: true})
          });
      });
  }
);
