define(['jquery', 'underscore', 'backbone', 
    '../collections/artists',
    'text!templates/artists.html'], function($, _, Backbone, Artists, t) {
  var ArtistsView = Backbone.View.extend({
    el: $('#ui-view'),
    template: _.template(t),

    render: function() {
      this.$el.html(t);
    }
  });

  return ArtistsView;
});
