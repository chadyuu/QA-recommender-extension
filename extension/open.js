chrome.tabs.query(
	{ active: true, lastFocusedWindow: true },
	tabs => {
		current_url = tabs[0].url
		window.open("questions.html/?current_url=" + current_url, "_blank")
	});
