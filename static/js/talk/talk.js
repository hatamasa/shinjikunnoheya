$(function() {
  $('#question_form').submit(function() {
    event.preventDefault();

    now = new Date();
    timestamp = now.toLocaleString();

    question = $('#question').val();
    message(question, timestamp, 'q_box');
    $.ajax({
      type : 'POST',
      url : '/api/talk/',
      datatype : "JSON",
      data : JSON.stringify({
        'question' : question
      }),
      success : function(data) {
        message(data.answer, data.timestamp, 'a_box');
      }
    });

    $('#question').val("");

    $('body').delay(100).animate({
      scrollTop: $(document).height()
    },1500);

    return false;
  });
});

function message(msg, timestamp, q_or_a) {
  box = $('<div></div>', {
    class : q_or_a
  });
  text = $('<div></div>').attr('class', 'text');
  text.append($('<p></p>').text(msg));
  text.append($('<span></span>').text(timestamp));
  box.append(text);
  if (q_or_a == 'a_box') {
    box.append($('<img>').attr({src : "/static/images/shinji.png",
                              alt : "シンジ君"}));
  }

  $('#talk').append(box);
  let target = document.getElementById("talk");
  $('html,body').animate({scrollTop: target.scrollHeight},'slow');
}
