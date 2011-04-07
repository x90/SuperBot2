from Hook import bindFunction
import re
#
#   This should contain handy chunks of code that plugins use
#   but have to write for each plugin separatly
#
class IRCArgs:
    
    nickRE = re.compile("^(?P<nick>.*)!.*$")

    def onEvent(self,event):
        m=self.nickRE.match(event["prefix"])
        if m!=None:
            event["nick"]=m.groupdict()["nick"]

        event["toMe"] = event["nickname"]==event["target"] #toMe = true|false depending on if it was sent to you

