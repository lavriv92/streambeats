/** @jsx React.DOM */

var React = require('react');

var Header = require('./header.jsx');
var Footer = require('./footer.jsx');
var Router = require('./router.jsx');

module.exports = React.createClass({
  render: function() {
    return (
      <div id="wrapper">
        <Header/>
        <Router />
        <Footer/>
      </div>
      )
  }
});
