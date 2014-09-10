define(['jquery', 'underscore', 'backbone', '../models/artist',
    'text!templates/artist_item.html'], 
function($, _, Backbone, Artist, t) {
  var ArtistItem = Backbone.View.extend({
    el: $('#ui-view'),
    className: 'artist',
    template: _.template(t),

    initialize: function(id) {
      this.model.bind('all', this.render, this);
    },

    render: function() {
      var $el = $(this.el);
      $el.html(this.template({'artist': this.model.toJSON()}));
      return this;
    }
  });

  return ArtistItem;
});
