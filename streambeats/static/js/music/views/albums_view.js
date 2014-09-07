define(['jquery', 'underscore', 'backbone',
    '../collections/albums'], function($, _, Backbone, Albums) {
  var AlbumsView = Backbone.View.extend({
    collection: new Albums(),
    self: this,

    initialize: function() {
      this.collection.fetch();
    }
  });

  return AlbumsView;
});
