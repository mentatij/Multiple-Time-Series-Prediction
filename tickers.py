tickers_dict = {'IXIC':('^IXIC', 'NASDAQ Composite'),
                #'NDX' :('^NDX',  'NASADAQ 100'),
                'BANK':('^BANK', 'NASDAQ Bank'),
                'NBI' :('^NBI',  'NASDAQ Biotechnology'),
                'IXCO':('^IXCO', 'NASDAQ Computer'),
                'IXHC':('^IXHC', 'NASDAQ HealthCare'),
                'INDS':('^INDS', 'NASDAQ Industrial'),
                'INSR':('^INSR', 'NASDAQ Insurance'),
                'OFIN':('^OFIN', 'NASDAQ Other Finance'),
                'IXTC':('^IXTC', 'NASDAQ Telecommunications'),
                'TRAN':('^TRAN', 'NASDAQ Transportation'),
                'DJI' :('^DJI',  'Dow Jones Industrial Average'),
                'NYA' :('^NYA',  'NYSE COMPOSITE (DJ)'),
              }

# Yahoo почему-то не выдает котировки по этим тикерам больше, чем на месяц назад : 
#{'^IXF' : 'NASDAQ Financial 100', '^NGX' : 'Nasdaq Next Generation 100', '^QNET': 'NASDAQ Internet', '^SPX' : 'S&P 500 INDEX'}