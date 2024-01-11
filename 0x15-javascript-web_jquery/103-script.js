document.addEventListener('DOMContentLoaded', function () {
  $('#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      $('#btn_translate').click();
    }
  });

  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
