define([
    'underscore',
    'backbone'
], function(_, Backbone) {
  var CurrentUser = Backbone.Model.extend({
    url: '/account/users/current'
  });
});
