define(['jquery', 'underscore', 'backbone','core/views/index_view',
    'music/views/tracks_view', 'music/views/albums_view',
    'music/views/artists_view', 'account/views/edit_view'
], function($, _, Backbone, 
  IndexView, TracksView, AlbumsView, ArtistsView, AccountEditView) {  
    var AppRouter = Backbone.Router.extend({
    routes: {
      '': 'index',
      'artists/': 'artists',
      'artists/:id/': 'artist_detail',
      'albums/': 'albums',
      'albums/:id/': 'album_detail',
      'account/edit/': 'edit_account'
    },

    index: function() {
      var index_view = new IndexView();
      index_view.render();
    },

    artists: function() {
      var artists_view = new ArtistsView();
      artists_view.render();
    },

    albums: function() {
      var albums_view = new AlbumsView();
      albums_view.render();
    },

    album_detail: function() {
    
    },

    artist_detail: function() {
    
    },

    edit_account: function() {
      var edit_view = new AccountEditView();
      edit_view.render();
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
