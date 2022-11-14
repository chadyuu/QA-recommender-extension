url = 'http://127.0.0.1:5000/get'

chrome.tabs.query(
	{ active: true, lastFocusedWindow: true },
	tabs => {
		$.ajax({
			url: url,
			context: document.body,
			data: {
				link: tabs[0].url
			},
		}).done(function (data) {
			data.forEach(question_id => {
				$("#data").append("<li><a href='https://stackoverflow.com/questions/" + question_id + "/'>" + question_id + "</a></li>");
			});
		});
	}
);