$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    $('DIV#hello').empty();
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + lang,
      success: (data) => {
        $('DIV#hello').append(data.hello);
      }
    });
  });
});
