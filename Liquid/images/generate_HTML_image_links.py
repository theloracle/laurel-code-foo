while 1:
    color = raw_input("Color?: ")
    end = int(raw_input("# of imgs?: "))

    for x in range(1, end):
        print '<li>Bot'+str(x)+'</li>'
        print '<a href="images/'+color+str(x)+'.jpg" rel="lightbox['+color+']"title="Bot'+str(x)+'">'
        print '<img src="images/'+color+str(x)+'.jpg" rel="lightbox" height=50% width= 50%/></a>'
    y = raw_input("Done?: ")
    if y == "y":
        break
