App.Router = Backbone.Router.extend({
    routes: {
        '': 'index',
        'test': 'test'
    },

    'index': function () {
        console.log('putin huilo');
    },

    test: function () {
        console.log('test');
    }
});

var router = new App.Router();
Backbone.history.start();