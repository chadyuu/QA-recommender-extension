url = 'http://127.0.0.1:5000/get'

chrome.tabs.query(
	{ active: true, lastFocusedWindow: true },
	tabs => {
		current_url = tabs[0].url
		$.ajax({
			url: url,
			context: document.body,
			data: {
				link: current_url
			},
		}).done(function (data) {
			i = 0
			data.forEach(question_id => {
				if (!current_url.includes("/" + question_id + "/") & i < 3) {
					$("#data").append("<li><a href='https://stackoverflow.com/questions/" + question_id + "/'>" + question_id + "</a></li>");
					i += 1
				}
			});
		});
	}
);