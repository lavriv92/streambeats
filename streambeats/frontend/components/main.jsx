/** @jsx React.DOM */


var Backbone = require('backbone');
Backbone.$ = require('jquery');
var React = require('react');
var App = require('./core/app.jsx');

React.renderComponent(<App />, document.body);
