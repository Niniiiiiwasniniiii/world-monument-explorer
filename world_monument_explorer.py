import math 
import random 
def calculate_distance(lat1, lon1, lat2, lon2):


    earth_radius = 6371

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius * c


def find_nearest_monument(lat, lon):

    nearest = None
    shortest = float("inf")

    for monument in MONUMENTS:

        distance = calculate_distance(
            lat,
            lon,
            monument["lat"],
            monument["lon"],
        )

        if distance < shortest:
            shortest = distance
            nearest = monument

    return nearest, round(shortest, 2)


def random_monument():
    return random.choice(MONUMENTS)


def search_monument(name):

    name = name.lower()

    for monument in MONUMENTS:

        if monument["name"].lower() == name:
            return monument

    return None
#history 
MONUMENTS = [
    {
        "name": 'eiffel tower',
        "country": 'france',
        'lat' : 48.8584,
        'lon': 2.2945,
        'history' : "built in 18889 as the entrance arch for the world's fair in paris, the eiffel tower was meant to stand for only 20 years. parisians hated it at first, calling it an eyesore, but it became the most iconic symbol of france.",
        "facts": ['1, it grows about 15 cm taller in summer heat because of iron expansion!'
        '2. it was the tallest man-made structure in the world for 41 years'
        '3. it is repainted every 7 years using 60 tonnes of paint.']
    },
    {
        'name': 'great pyramid of giza',
        'country' : 'egypt',
        'lat' : 29.9792,
        'lon': 31.1342,
        'history' : 'built around 2560 BC as a tomb for pharaoh khufu, this is the oldest of the seven wonders of the ancient world and the only one still standing today.',
        'facts' : ['1. it was the tallest structure on earth for almost 3,800 years'
                   '2. it is made of about 2.3 million stone blocks.'
                   '3. its sides are almost perfectly aligned to true north']

    },
    {
        'name' : 'taj mahal',
        'country' : 'india',
        'lat' : 27.1751,
        'lon' : 78.0421,
        'history': "emperor shah jahan built this white marble structure mausoleum in the 1600s in memory of his on of many wivves mumtaz mahal. it took  20,000 workers roughly 20 years to finish",
        'facts' : ['1. the marble changes color throughout the day, pink at dawn, white at noon, golden at night'
                   "2. it is perfectly symmetrical except for shah jahan's tomb inside"
                   '3. it is a UNESCO heritage site visited by millions every year.']
    },
    {
        'name': 'great wall of china',
        'country' : "china",
        'lat': 40.4319,
        'lon' : 116.5704,
        'history' : ' built and rebuilt over centuries (starting more than 2000 years ago) to protect chinese from invasions, the wallstretches across the country.s northern borders.',
         'facts' : ['1. it is not actually visible from space from the naked eye its actually a myth!'
                    '2. its total length, including all branches, is over 21,000 km,'
                    '3. sticky rice was used in the mortar of some sections to make it stronger.']
    },
    {
        'name' : "machu pichu",
        'country' : 'peru',
        'lat' : -13.1631,
        'lon' : -72.5450,
        'history' : 'this is the 15th-century incan citdel sits high in the andes mountains. it was likely a royal estate and was unknown to the world outside until 1911.',
        'facts' : ['1.it was built without any mortar, stones fit perfectly. '
                   '2. it sits 2.430 meters above sea level.'
                   '3. its exact original purpose is still debated by historians.']
    },
    {
        'name': "statue of liberty",
        'country' : 'united states of america',
        'lat' : 40.6892,
        'lon' : -74.0445,
        'history' : "A gift from france to the US in 1886, this sopper statue represents libertas, the roman goddess of freedom, and welcomed millions of immigrants arriving by sea.",
        'facts' : ["1. Its made of copper only as thick as two stacked pennies."
           " 2. It turned green over time due to natural oxidation."
            "3. The torch was originally open to visitors but closed to the public since 1916."]
    },
     {
        "name": "Colosseum",
        "country": "Italy",
        "lat": 41.8902,
        "lon": 12.4922,
        "history": "Completed in 80 CE, this massive amphitheater in Rome hosted gladiator battles, animal hunts, and public spectacles for up to 80,000 spectators.",
        "facts": [
            "1. It had a retractable awning system operated by sailors.",
            "2. The floor could be flooded for mock naval battles.",
            "3. Underground tunnels called the hypogeum held animals and gladiators before shows."
        ]
    },
     {
        "name": "Christ the Redeemer",
        "country": "Brazil",
        "lat": -22.9519,
        "lon": -43.2105,
        "history": "Completed in 1931 atop Corcovado Mountain in Rio de Janeiro, this Art Deco statue of Jesus Christ has become a symbol of Brazilian identity and Christianity worldwide.",
        "facts": [
            "1. It's struck by lightning several times a year due to its height.",
            "2. It stands 30 meters tall, not counting its 8-meter pedestal.",
            "3. It's one of the New 7 Wonders of the World."
        ]
    },
     {
        "name": "Petra",
        "country": "Jordan",
        "lat": 30.3285,
        "lon": 35.4444,
        "history": "Carved directly into rose-colored rock cliffs over 2,000 years ago, Petra was the capital of the Nabataean kingdom and a major trading hub along ancient caravan routes.",
        "facts": [
            "1. It stayed hidden from the Western world until 1812.",
            "2. Its most famous building, the Treasury, was carved entirely from the top down.",
            "3. It's nicknamed the 'Rose City' for the color of its stone."
        ]
    },
      {
        "name": "Stonehenge",
        "country": "United Kingdom",
        "lat": 51.1789,
        "lon": -1.8262,
        "history": "This prehistoric stone circle in England was built in stages starting around 3000 BCE. Nobody knows for certain why it was built — theories range from a burial site to an ancient calendar.",
        "facts": [
            "1. Some stones were transported from over 200 km away.",
            "2. It's aligned with the sunrise on the summer solstice.",
            "3. It's older than the Great Pyramid of Giza."
        ]
    },
      {
        "name": "Stonehenge",
        "country": "United Kingdom",
        "lat": 51.1789,
        "lon": -1.8262,
        "history": "This prehistoric stone circle in England was built in stages starting around 3000 BCE. Nobody knows for certain why it was built — theories range from a burial site to an ancient calendar.",
        "facts": [
            "1. Some stones were transported from over 200 km away.",
            "2. It's aligned with the sunrise on the summer solstice.",
            "3. It's older than the Great Pyramid of Giza."
        ]
    },
     {
        "name": "Sydney Opera House",
        "country": "Australia",
        "lat": -33.8568,
        "lon": 151.2153,
        "history": "Opened in 1973 after 14 years of construction, its sail-like shells were designed by Danish architect Jørn Utzon and remain one of the most recognizable buildings on Earth.",
        "facts": [
            "1. It has over one million roof tiles.",
            "2. It hosts more than 1,800 performances every year.",
            "3. It's a UNESCO World Heritage Site, despite being less than 50 years old when listed."
        ]
    },
     {
        "name": "Big Ben & Houses of Parliament",
        "country": "United Kingdom",
        "lat": 51.5007,
        "lon": -0.1246,
        "history": "'Big Ben' is technically the nickname of the giant bell inside the clock tower, completed in 1859, that stands beside the UK's Houses of Parliament.",
        "facts": [
            "1. The clock is famous for its accuracy, adjusted using old penny coins on the pendulum.",
            "2, The tower leans slightly, about 46 cm at the top.",
            "3. The bell's chime has been broadcast on BBC radio since 1923."
        ]
    },
    {
        "name": "Sagrada Família",
        "country": "Spain",
        "lat": 41.4036,
        "lon": 2.1744,
        "history": "Architect Antoni Gaudí began this extraordinary basilica in Barcelona in 1882, and it's still under construction today, funded almost entirely by visitor donations.",
        "facts": [
            "1. Gaudí knew he wouldn't live to see it finished, and he was right.",
            "2. It's expected to finally be completed around 2026, roughly 144 years after starting.",
            "3. Its towers represent Jesus, Mary, and the twelve apostles."
        ]
    },
    {
        "name": "Chichén Itzá",
        "country": "Mexico",
        "lat": 20.6843,
        "lon": -88.5678,
        "history": "A major city of the ancient Maya civilization, Chichén Itzá flourished between 600 and 1200 CE, its pyramid El Castillo built as a temple to the god Kukulcán.",
        "facts": [
            "1. On the equinox, a shadow forms that looks like a snake slithering down the pyramid steps.",
            "2. Clapping at the base of the pyramid creates an echo that sounds like a bird chirp.",
            "3. The pyramid has exactly 365 steps — one for each day of the year."
        ]
    },
    {
        "name": "Acropolis of Athens",
        "country": "Greece",
        "lat": 37.9715,
        "lon": 23.7267,
        "history": "This ancient citadel sits atop a rocky hill in Athens and contains the Parthenon, a temple built in the 5th century BCE to honor the goddess Athena.",
        "facts": [
            "1. The Parthenon's columns bulge slightly in the middle to look perfectly straight from a distance.",
            "2. It has almost no perfectly straight lines — everything is subtly curved.",
            "3. It once held a massive gold-and-ivory statue of Athena, now lost."
        ]
    },
    {
        "name": "Neuschwanstein Castle",
        "country": "Germany",
        "lat": 47.5576,
        "lon": 10.7498,
        "history": "Commissioned in 1869 by the reclusive King Ludwig II of Bavaria as a private retreat, this fairytale castle inspired Disney's Sleeping Beauty Castle.",
        "facts": [
            "1. Ludwig II lived there for less than 6 months before his death.",
            "2. It was never actually finished as originally planned.",
            "3. It has modern conveniences for its time, like running water on every floor."
        ]
    },
    {
        "name": "Mount Rushmore",
        "country": "USA",
        "lat": 43.8791,
        "lon": -103.4591,
        "history": "Carved between 1927 and 1941, this granite sculpture in South Dakota depicts four U.S. presidents: Washington, Jefferson, Roosevelt, and Lincoln.",
        "facts": [
            "1. Each face is about 18 meters tall — as tall as a six-story building.",
            "2. It was carved using dynamite for about 90% of the rock removal.",
            "3. It stands on land considered sacred by the Lakota Sioux."
        ]
    },
    {
        "name": "Golden Gate Bridge",
        "country": "USA",
        "lat": 37.8199,
        "lon": -122.4783,
        "history": "Opened in 1937, this suspension bridge connects San Francisco to Marin County and was, at the time, the longest and tallest suspension bridge in the world.",
        "facts": [
            "1. Its color, 'International Orange', was chosen to stand out in San Francisco's frequent fog.",
            "2. It's repainted continuously — the maintenance never really stops.",
            "3. The bridge sways up to 8 meters in strong winds by design."
        ]
    },
    {
        "name": "Burj Khalifa",
        "country": "United Arab Emirates",
        "lat": 25.1972,
        "lon": 55.2744,
        "history": "Opened in 2010 in Dubai, the Burj Khalifa is currently the tallest building ever constructed, a modern engineering marvel inspired by desert flowers and Islamic architecture.",
        "facts": [
            "1, It stands 828 meters tall — nearly twice the height of the Empire State Building.",
            "2. On a clear day, you can see the sunset twice by riding the elevator back up.",
            "3. It has over 900 apartments and its own private lounge on the 148th floor."
        ]
    },
    {
        "name": "Red Square & Kremlin",
        "country": "Russia",
        "lat": 55.7539,
        "lon": 37.6208,
        "history": "The heart of Moscow since the 15th century, the Kremlin is a fortified complex containing palaces and cathedrals, right beside the historic Red Square and colorful St. Basil's Cathedral.",
        "facts": [
            "1. 'Red Square' isn't named for communism — 'red' in old Russian also meant 'beautiful'.",
            "2. St. Basil's Cathedral has nine differently designed domes.",
            "3. The Kremlin walls stretch for 2.25 km around the complex."
        ]
    },
    {
        "name": "Forbidden City",
        "country": "China",
        "lat": 39.9163,
        "lon": 116.3972,
        "history": "Home to Chinese emperors for almost 500 years, this palace complex in Beijing was completed in 1420 and housed 24 emperors of the Ming and Qing dynasties.",
        "facts": [
            "1. It contains 980 surviving buildings.",
            "2. Commoners were forbidden from entering — hence its name.",
            "3. It's said to have 9,999 rooms, just short of the mythical 10,000 belonging to heaven."
        ]
    },
    {
        "name": "Great Mosque of Mecca",
        "country": "Saudi Arabia",
        "lat": 21.4225,
        "lon": 39.8262,
        "history": "Surrounding the Kaaba, Islam's holiest site, this mosque is the largest in the world and the destination of the annual Hajj pilgrimage.",
        "facts": [
            "1. It can hold over 2 million worshippers during Hajj.",
            "2. The Kaaba at its center predates Islam itself.",
            "3. Muslims around the world face this direction during daily prayers."
        ]
    },
    {
        "name": "St. Peter's Basilica",
        "country": "Vatican City",
        "lat": 41.9022,
        "lon": 12.4539,
        "history": "Built over the traditional burial site of Saint Peter, this Renaissance basilica took over a century to build and remains one of the largest churches on Earth.",
        "facts": [
            "1. Its dome was designed by Michelangelo, who never saw it completed.",
            "2. It can hold roughly 60,000 people inside.",
            "3. It sits at the center of the smallest country in the world."
        ]
    },
    {
        "name": "Leaning Tower of Pisa",
        "country": "Italy",
        "lat": 43.7230,
        "lon": 10.3966,
        "history": "Construction began in 1173 as a bell tower, but the soft ground beneath it caused it to start tilting before it was even finished.",
        "facts": [
            "1. It currently leans about 4 degrees from vertical.",
            "2, Engineers straightened it slightly in the 1990s to keep it from collapsing.",
            "3.Galileo is said to have used it for gravity experiments (though this may be a legend)."
        ]
    },
    {
        "name": "Hagia Sophia",
        "country": "Turkey",
        "lat": 41.0086,
        "lon": 28.9802,
        "history": "Built in 537 CE as a Christian cathedral, converted into a mosque in 1453, then a museum, and back to a mosque again in 2020 — its history mirrors the many empires that ruled Istanbul.",
        "facts": [
            "1. Its massive dome was an engineering marvel for over a thousand years.",
            "2. It contains stunning mosaics from both its Christian and Islamic history side by side.",
            "3. It was the largest cathedral in the world for nearly 1,000 years."
        ]
    },
    {
        "name": "Victoria Falls",
        "country": "Zambia / Zimbabwe",
        "lat": -17.9243,
        "lon": 25.8572,
        "history": "Known locally as 'Mosi-oa-Tunya' ('The Smoke That Thunders'), this is one of the largest waterfalls in the world, formed where the Zambezi River plunges into a deep gorge.",
        "facts": [
            "1. Its spray can be seen from up to 30 km away.",
            "2. It's more than twice the height of Niagara Falls.",
            "3. You can swim in the natural 'Devil's Pool' right at the edge during dry season."
        ]
    },
    {
        "name": "Uluru",
        "country": "Australia",
        "lat": -25.3444,
        "lon": 131.0369,
        "history": "This massive sandstone rock formation in the Australian outback is sacred to the Anangu people, who have lived in the region for tens of thousands of years.",
        "facts": [
            "1. It changes color dramatically at sunrise and sunset, often glowing red.",
            "2. Most of its bulk is actually hidden underground.",
            "3. Climbing it was permanently banned in 2019 out of respect for Anangu culture."
        ]
    },
    {
        "name": "Moai of Easter Island",
        "country": "Chile",
        "lat": -27.1127,
        "lon": -109.3497,
        "history": "Carved by the Rapa Nui people between 1250 and 1500 CE, these nearly 1,000 giant stone statues represent ancestors and were placed facing inland to watch over villages.",
        "facts": [
            "1. Some statues are over 9 meters tall and weigh up to 82 tonnes.",
            "2. Most have full bodies buried underground — only heads are visible today.",
            "3. How they were moved without modern machinery is still debated by researchers."
        ]
    },
    {
        "name": "Niagara Falls",
        "country": "Canada / USA",
        "lat": 43.0962,
        "lon": -79.0377,
        "history": "Formed roughly 12,000 years ago at the end of the last Ice Age, this group of three waterfalls sits on the border between Canada and the United States.",
        "facts": [
            "1. Over 3,100 tonnes of water flow over the falls every second.",
            "2. It's slowly eroding backward, about 30 cm per year.",
            "3. Barrel-riding daredevils have gone over the falls since 1901."
        ]
    },
    {
        "name": "Grand Canyon",
        "country": "USA",
        "lat": 36.1069,
        "lon": -112.1129,
        "history": "Carved by the Colorado River over roughly 5–6 million years, this immense gorge exposes nearly 2 billion years of Earth's geological history in its layered rock walls.",
        "facts": [
            "1. It's up to 29 km wide and 1.8 km deep.",
            "2. It's home to distinct ecosystems that change with elevation.",
            "3. It's been continuously inhabited by Native American communities for over 10,000 years."
        ]
    },
    {
        "name": "Alhambra",
        "country": "Spain",
        "lat": 37.1761,
        "lon": -3.5881,
        "history": "This stunning palace and fortress complex in Granada was built mainly in the 1300s by Moorish rulers, showcasing exquisite Islamic art and architecture.",
        "facts": [
            "1. Its name means 'The Red One' in Arabic, from the color of its walls at sunset.",
            "2. Its intricate tile and stucco patterns are based entirely on geometry — no images of people.",
            "3. It inspired composers, poets, and artists across Europe for centuries."
        ]
    },
    {
        "name": "Notre-Dame Cathedral",
        "country": "France",
        "lat": 48.8530,
        "lon": 2.3499,
        "history": "Completed in 1345 after nearly 200 years of construction, this Gothic masterpiece in Paris survived revolutions and wars before a major fire in 2019 sparked a global restoration effort.",
        "facts": [
            "1. Its flying buttresses were groundbreaking engineering for their time.",
            "2. It houses relics believed by some to include the Crown of Thorns.",
            "3. It reopened to the public in December 2024 after painstaking restoration."
        ]
    },
    {
        "name": "Brandenburg Gate",
        "country": "Germany",
        "lat": 52.5163,
        "lon": 13.3777,
        "history": "Built in the 1790s as a city gate, this neoclassical monument in Berlin became a powerful symbol of division during the Cold War and reunification when the Berlin Wall fell in 1989.",
        "facts": [
            "1. It was closed off entirely during the Cold War, sitting right in the death strip.",
            "2. Its bronze chariot statue was stolen by Napoleon in 1806 and later returned.",
            "3. Crowds gathered here to celebrate when Germany reunified."
        ]
    },
    {
        "name": "Himeji Castle",
        "country": "Japan",
        "lat": 34.8394,
        "lon": 134.6939,
        "history": "Nicknamed the 'White Heron Castle' for its brilliant white exterior, this castle dates to the 1300s with major expansions in 1609, and is Japan's best-preserved original castle.",
        "facts": [
            "1. It survived both WWII bombings and earthquakes largely intact.",
            "2. Its maze-like paths were designed to confuse invading armies.",
            "3. It's one of Japan's first UNESCO World Heritage Sites."
        ]
    },
    {
        "name": "Borobudur",
        "country": "Indonesia",
        "lat": -7.6079,
        "lon": 110.2038,
        "history": "Built in the 9th century, this is the largest Buddhist temple in the world, its structure representing the Buddhist path from earthly desire to enlightenment.",
        "facts": [
            "1. It has 2,672 relief panels and 504 Buddha statues.",
            "2. It was hidden under volcanic ash and jungle for centuries before rediscovery.",
            "3. Pilgrims walk clockwise through its levels as a form of meditation."
        ]
    },
    {
        "name": "Potala Palace",
        "country": "China (Tibet)",
        "lat": 29.6558,
        "lon": 91.1177,
        "history": "Once the winter home of the Dalai Lama, this palace in Lhasa sits at over 3,700 meters elevation and was built starting in the 7th century, with major additions in the 1600s.",
        "facts": [
            "1. It has over 1,000 rooms across 13 stories.",
            "2. It's one of the highest ancient palaces in the world.",
            "3. Its name comes from a mythical mountain in Buddhist belief."
        ]
    },
    {
        "name": "Rock-Hewn Churches of Lalibela",
        "country": "Ethiopia",
        "lat": 12.0316,
        "lon": 39.0473,
        "history": "Carved directly downward out of solid volcanic rock in the 12th and 13th centuries, these eleven churches were built to create a 'New Jerusalem' for Ethiopian Christians.",
        "facts": [
            "1. Each church was carved from a single block of rock, top to bottom.",
            "2. They're still active places of worship today, centuries later.",
            "3. Tunnels and trenches connect the churches underground."
        ]
    }

]
    