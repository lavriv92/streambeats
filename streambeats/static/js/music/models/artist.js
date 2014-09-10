define(['underscore', 'backbone'], 
function(_, Backbone) {
  var Artist = Backbone.Model.extend({
    url: function() {
      return '/api/tracks/artists/' + this.id;
    }
  });
  return Artist;
});
