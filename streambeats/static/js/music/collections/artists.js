define(['underscore', 'backbone', 
    '../models/artist'], function(_, Backbone, Artist) {
  var Artists = Backbone.Collection.extend({
    url: '/api/tracks/artists',
    model: Artist
  });

  return Artists;
});
