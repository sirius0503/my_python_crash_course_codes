cities = {
    'tokyo':{
        'country' : 'japan',
        'population' : 35000000 ,
        'fact' :'The cherry blossom is the national symbol of Japan. These \
trees flower for one or two weeks a year starting in April. This \
period is known as Hanami, the long standing tradition of \
welcoming spring. This festival is about appreciating the \
temporary beauty of nature.'
            },
    'prague': {
        'country' :'czech republic',
        'population' : 1260000 ,
        'fact' :'Czechoslovakia declared their independence on October 28 \
1918,with Prague becoming its new capital',
            },
    'seoul': {
        'country' : 'south korea',
        'population': 10000000 ,
        'fact' :' In 1945, Korea gained its independence from Japan and the \
city was renamed Seoul. In 1949, the city separated from Gyeonggi \
Province and it became a "special city." In 1950 however, North \
Korean troops occupied the city during the Korean War and the \
entire city was nearly destroyed. On March 14, 1951, United \
Nations forces took control of Seoul and since then, the city \
has rebuilt and grown considerably.',
               },
        }
               

for city ,value in cities.items() :
    print("\nCity : " + city.title() )
    print("\nCountry: " + value['country'].title())
    print("\nPopulation: " + str(value['population']))
    print("\nFact: " + value['fact'])
    print("\n\n")
