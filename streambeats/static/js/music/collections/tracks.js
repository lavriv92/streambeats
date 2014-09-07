define(['underscore', 'backbone', 
    '../models/track'], function(_, Backbone, Track) {
    
    var Tracks = Backbone.Collection.extend({
      url: '/api/tracks/tracks/',
      model: Track
    });

    return Tracks;
});
