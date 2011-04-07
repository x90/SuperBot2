"""Youtube plugin for querying videos from an IRC chatroom."""

from Hook import bindFunction, prefers
import re
import gdata.youtube.service

@prefers('Colors')
class YouTube(object):
    
    @bindFunction(message="!yt (?P<query>.*?) ?(?P<num>\d+)?$")
    def handle(self, target, query, response, num):
        
        print target,query,response,num
        yt_service = gdata.youtube.service.YouTubeService()
        vquery = gdata.youtube.service.YouTubeVideoQuery()
        vquery.vq = query
        vquery.orderby = 'relevance'
        vquery.racy = 'include'
        feed = yt_service.YouTubeQuery(vquery)

        if feed.entry:
            entry = feed.entry[int(num) if num else 0]
            d = {}
            d['total_results'] = len(feed) 
            d['rating_average'] = "%.2f" % float(entry.rating.average)
            d['rating_max'] = entry.rating.max
            d['num_raters'] =  entry.rating.num_raters
            d['view_count'] = entry.statistics.view_count

            d['title'] = entry.title.text

            tosay = "{title} | Avg Score: {rating_average}/{rating_max} | Views: {view_count} | Total Results: {total_results}".format(**d)
            print tosay
        else:
            tosay = "No results found for query. =("
        
        return response.say(target, tosay)

        


 
