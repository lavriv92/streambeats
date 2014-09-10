define(['underscore', 'backbone'], 
function(_, Backbone) {
  var Album = Backbone.Model.extend({
    url: function() {
      return '/api/tracks/albums/' + this.id; 
    } 
  });

  return Album;
});
