define([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {
  var AppRouter = Backbone.Router.extend({
    routes: {
      '': 'index',
      'test': 'test'
    },

    index: function() {
      console.log('index');
    },

    test: function() {
      console.log('test');
    }
  });

  var initialize = function() {
    var app_router = new AppRouter();
    Backbone.history.start();
  };

  return {
    initialize: initialize
  };
});
