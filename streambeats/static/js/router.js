define(['jquery', 'underscore', 'backbone','core/views/index_view',
    'music/views/tracks_view', 'music/views/albums_view',
    'music/views/artists_view', 'account/views/edit_view',
    'music/views/artist_item', 'music/views/album_item',
    'music/models/album',
    'music/models/artist'
], function($, _, Backbone, 
  IndexView, TracksView, AlbumsView, 
  ArtistsView, AccountEditView, ArtistItem, AlbumItem, Album, Artist) {  
    var AppRouter = Backbone.Router.extend({
    routes: {
      '': 'index',
      'artists/': 'artists',
      'artists/:id/': 'artist_detail',
      'albums/': 'albums',
      'albums/:id/': 'album_detail',
      'artists/:id/': 'artist_detail',
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

    artist_detail: function(id) {
      var artist = new Artist({id: id});
      artist.fetch();
      var artist_item = new ArtistItem({model: artist});
      artist_item.render();
    },

    album_detail: function(id) {
      var album = new Album({id: id});
      album.fetch();
      album_item = new AlbumItem({model: album});
      album_item.render();
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
