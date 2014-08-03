define([
  'jquery',
  'underscore',
  'backbone',
  'core/views/index_view'
], function($, _, Backbone, IndexView) {
  var AppRouter = Backbone.Router.extend({
    routes: {
      '': 'index'
    },

    index: function() {
      var index_view = new IndexView();
      index_view.render();
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
