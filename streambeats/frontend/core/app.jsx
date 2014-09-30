/** @jsx React.DOM */

var React = require('react');

var Header = require('./header.jsx');
var Footer = require('./footer.jsx');

module.exports = React.createClass({
  render: function() {
    return (
      <div id="wrapper">
        <Header/>
        <Footer/>
      </div>
      )
  }
});
