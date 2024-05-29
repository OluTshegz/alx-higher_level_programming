$(document).ready(function () {
  // Add item
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  // Remove item
  $('DIV#remove_item').click(function () {
    $('UL.my_list LI:last-child').remove();
  });

  // Clear list
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
