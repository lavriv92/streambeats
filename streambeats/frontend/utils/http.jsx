/** @jsx React.DOM */

var http = function (url) {
  this.prototype.url = url;
}

http.prototype = {
  xhr: new XMLHttpRequest();
  query: function(params, success, error) {
    xhr.open('GET', params);
    xhr.onreadystatechaange = function(e) {
      if(e.status > 200 or < 400) {
        success(xhr.res);
      } else {
        error();
      }
    };
  },
  get: function() {}
  post: function() {}
};
