var collapsibles = $(".list-collapse");
for (var i = 0; i < collapsibles.length; i++)
	{var collapsible = collapsibles[i];
	$(collapsible).addClass("collapse-off");
	var x = collapsible.getElementsByTagName('a')[0];
	$(x).click(collapse);}
function collapse()
	{var y = this.parentNode;
	if($(y).hasClass("collapse-off"))
		{$(y).removeClass();
		$(y).addClass("collapse-on");}
	else
		{$(y).removeClass();
		$(y).addClass("collapse-off");}}
