var count = 10;
var timer = setInterval(function () {
	if (count<=0) clearInterval(timer);
	count--;
  document.getElementsByClassName("composer_rich_textarea")[0].innerText="Hi";
$(".im_submit_send_label").trigger("mousedown");
},500);