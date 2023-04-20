(function() {
  'use strict';

  // Get all menu links and attach click event listener
  var menuLinks = document.querySelectorAll('.menu-link');
  for (var i = 0; i < menuLinks.length; i++) {
    menuLinks[i].addEventListener('click', function(event) {
      event.preventDefault();
      var menuUrl = this.getAttribute('href');
      fetch(menuUrl)
        .then(response => response.text())
        .then(data => {
          // Replace current content with menu page content
          var content = document.getElementById('content');
          content.innerHTML = data;
        });
    });
  }

})();
