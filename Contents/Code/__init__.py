TITLE = 'HLS Test'
PREFIX = '/video/hlstest'

####################################################################################################
def Start():

    ObjectContainer.title1 = TITLE
    
    HTTP.CacheTime = CACHE_1HOUR
    HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'

####################################################################################################
@handler(PREFIX, TITLE)
def MainMenu():

    oc = ObjectContainer()

    oc.add(
        VideoClipObject(
            url = 'http://devimages.apple.com.edgekey.net/streaming/examples/bipbop_16x9/bipbop_16x9_variant.m3u8',
            title = 'Sample - Including subtitles etc'
        )
    )
    
    oc.add(
        VideoClipObject(
            url = 'http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8',
            title = 'Sample - Plain'
        )
    )
    

    return oc
