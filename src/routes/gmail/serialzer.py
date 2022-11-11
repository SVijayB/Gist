def Message_to_text(MessagePart):
    pass


def HeaderParser(GmailHeader):
    # Subject Date from
    res = {}
    for Header in GmailHeader:
        try:

            if Header["name"] == "From":
                res["from"] = Header["value"]
            elif Header["name"] == "Subject":
                res["Subject"] = Header["value"]
            elif Header["name"] == "Date":
                res["Date"] = Header["value"]

        except KeyError:
            pass

    return res
