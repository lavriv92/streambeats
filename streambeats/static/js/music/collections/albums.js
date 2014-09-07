define(['underscore', 'backbone',
    '../models/album'], function(_, Backbone, Album) {
  var Albums = Backbone.Collection.extend({
    url: '/api/tracks/albums/',
    model: Album
  });

  return Albums;
});
