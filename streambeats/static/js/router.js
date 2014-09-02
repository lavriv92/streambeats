define([
  'jquery',
  'underscore',
  'backbone',
  'core/views/index_view'
], function($, _, Backbone, IndexView) {
  var AppRouter = Backbone.Router.extend({
    routes: {
      '': 'index',
      'artists/': 'artists',
      'artists/:id/': 'artist_detail',
      'albums/': 'albums',
      'albums/:id/': 'album_detail'
    },

    index: function() {
      var index_view = new IndexView();
      index_view.render();
    },

    artists: function() {
       
    },

    albums: function() {
        
    },

    album_detail: function() {
    
    },

    artist_detail: function() {
    
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
