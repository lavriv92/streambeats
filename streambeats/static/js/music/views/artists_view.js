define(['jquery', 'underscore', 'backbone', 
    '../collections/artists',
    'text!templates/artists.html'], function($, _, Backbone, Artists, t) {
  var ArtistsView = Backbone.View.extend({
    el: $('#ui-view'),
    collection: new Artists(),
    template: _.template(t),

    initialize: function() {
      this.collection.fetch();
    },

    render: function() {
      this.$el.html(t);
    }
  });

  return ArtistsView;
});
