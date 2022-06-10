class Mytube(dict):
    """
        Universe is where everything is and happen
    """
    # attrs: []
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)


    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def get_itags( self ):
        pass

    def download( self ):
        # self.current = self.universe.objects['youtube'](self.link).streams.filter( only_audio = True )
        self.current = self.universe.objects['playlist'](self.link)
        for video in self.current.videos:
            # print(video.streams)
            print('downloading : {} with url : {}'.format(video.title, video.watch_url))
            # print(video.streams.filter(type='audio').order_by('abr').asc().first())
            video.streams.\
            filter(type='audio').\
            order_by('abr').\
            asc().\
            first().\
            download()


        # >>> print(f'Downloading: {p.title}')
# Downloading: Python Tutorial for Beginers (For Absolute Beginners)
        # for video in p.videos:
        #     video.streams.first().download()
        # self.current = self.universe.objects['playlist'](self.link)
        # video = self.current[]
        # for thing in self.current:
        #     print(thing)
        # print(self.current.audios)

        # for video in self.current.videos:
        #     print(video.streams.first())

        #     video.streams.first().download()




        # self.current.first().download()
        # print(type(self.current))
        # print(type(self.current.filter( only_audio = True )))
