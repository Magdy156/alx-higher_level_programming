$(document).ready(() => {
  function translate () {
    $('DIV#hello').empty();
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + lang,
      success: (data) => {
        $('DIV#hello').append(data.hello);
      }
    });
  }
  $('INPUT#btn_translate').click(() => {
    translate();
  });
  $('INPUT#language_code').keypress((ele) => {
    const key = ele.which;
    if (key === 13) {
      translate();
    }
  });
});
