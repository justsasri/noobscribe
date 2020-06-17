// SCSS or SASS here
require('./scss/main.scss');

// Images
require('./img/logo.png');

// Fonts

// Javascripts

var $ = require('jquery');
window.$ = $;

require('popper.js');
require('bootstrap');

$(document).ready(
  function() {
    $('[data-toggle="tooltip"]').tooltip()
  }
);