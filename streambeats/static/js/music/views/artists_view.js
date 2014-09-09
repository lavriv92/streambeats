define(['jquery', 'underscore', 'backbone', 
    '../collections/artists',
    'text!templates/artists.html'], 
    function($, _, Backbone, Artists, t) {
  var ArtistsView = Backbone.View.extend({
    el: '#ui-view',
    collection: new Artists(),
    template: _.template(t),

    initialize: function() {
      this.collection.fetch();  
      this.collection.bind('all', this.render, this);
      return this;
    },

    render: function() {
      var $el = $(this.el);
      $el.html(this.template({'artists': this.collection.toJSON()}));

      return this;
    }
  });

  return ArtistsView;
});
