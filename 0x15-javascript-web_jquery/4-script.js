$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    if ($('HEADER').hasClass('red')) {
      $('HEADER').removeClass('red').addClass('green');
    } else {
      $('HEADER').removeClass('green').addClass('red');
    }
  });
});
