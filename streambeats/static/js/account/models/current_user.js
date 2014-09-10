define(['underscore', 'backbone'], 
function(_, Backbone) {
  
  var CurrentUser = Backbone.Model.extend({
    urlRoot: '/api/account/users/current',

    constructor: function() {
      Backbone.Model.apply(this, arguments);
      this.fetch();
    }
  });

  return CurrentUser;
});
