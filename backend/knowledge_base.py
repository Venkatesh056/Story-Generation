# Tamil Nadu Historical and Mythological Knowledge Base
"""
Comprehensive Tamil Nadu knowledge base for historical and mythological stories
Includes Tamil kings, queens, freedom fighters, epics, deities, and cultural elements
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class TamilEntity:
    """Represents a Tamil historical or mythological entity"""
    name: str
    type: str  # king, queen, freedom_fighter, deity, epic_character, place
    era: str
    region: str
    short_bio: str
    known_for: List[str]
    associated_places: List[str]
    festivals: List[str]
    keywords: List[str]
    story_seeds: List[str]

@dataclass
class TamilPlace:
    """Represents a Tamil Nadu place with historical/mythological significance"""
    name: str
    type: str  # city, temple, fort, battlefield, river, mountain
    district: str
    description: str
    main_legend: str
    historical_significance: str
    associated_entities: List[str]
    festivals: List[str]

# Tamil Nadu Historical Entities Database
TAMIL_HISTORICAL_ENTITIES = {
    # Tamil Kings & Dynasties
    "raja_raja_chola": TamilEntity(
        name="Raja Raja Chola I",
        type="king",
        era="Chola Empire (985-1014 CE)",
        region="Thanjavur",
        short_bio="Greatest Chola emperor who built the magnificent Brihadeeswarar Temple",
        known_for=["Brihadeeswarar Temple", "Naval expeditions", "Administrative reforms", "Patron of arts"],
        associated_places=["Thanjavur", "Gangaikonda Cholapuram", "Sri Lanka", "Maldives"],
        festivals=["Chithirai Festival", "Brihadeeswarar Temple Festival"],
        keywords=["Chola", "Temple", "Architecture", "Navy", "Administration", "Thanjavur"],
        story_seeds=[
            "The king who dreamed of building a temple that touched the sky",
            "A ruler whose ships sailed across the seas to spread Tamil culture",
            "The emperor who carved his victories in stone and bronze"
        ]
    ),
    
    "rajendra_chola": TamilEntity(
        name="Rajendra Chola I",
        type="king",
        era="Chola Empire (1014-1044 CE)",
        region="Gangaikonda Cholapuram",
        short_bio="Son of Raja Raja Chola, extended empire to Ganges and Southeast Asia",
        known_for=["Gangaikonda Cholapuram", "Conquest of Ganges", "Southeast Asian expeditions"],
        associated_places=["Gangaikonda Cholapuram", "Bengal", "Srivijaya", "Kedah"],
        festivals=["Chola Victory Festival"],
        keywords=["Chola", "Conquest", "Ganges", "Victory", "Empire", "Naval"],
        story_seeds=[
            "The prince who brought the sacred Ganges water to Tamil Nadu",
            "A king whose elephants marched from Cauvery to Ganges",
            "The emperor who made the whole world know Tamil valor"
        ]
    ),
    
    "karikala_chola": TamilEntity(
        name="Karikala Chola",
        type="king",
        era="Early Chola Period (1st-2nd Century CE)",
        region="Uraiyur",
        short_bio="Legendary early Chola king who built the Grand Anicut on Cauvery",
        known_for=["Grand Anicut", "Cauvery management", "Battle of Venni", "Trade development"],
        associated_places=["Uraiyur", "Cauvery River", "Venni", "Puhar"],
        festivals=["Cauvery Festival", "Pongal"],
        keywords=["Chola", "Cauvery", "Dam", "Agriculture", "Trade", "Engineering"],
        story_seeds=[
            "The king who tamed the mighty Cauvery river for his people",
            "A ruler who turned desert lands into fertile fields",
            "The emperor whose engineering marvels still serve Tamil Nadu"
        ]
    ),

    # Tamil Freedom Fighters
    "veerapandiya_kattabomman": TamilEntity(
        name="Veerapandiya Kattabomman",
        type="freedom_fighter",
        era="Polygar Wars (1760-1799)",
        region="Panchalankurichi",
        short_bio="Brave Polygar chieftain who defied British East India Company",
        known_for=["Resistance to British", "Panchalankurichi Fort", "Polygar confederation"],
        associated_places=["Panchalankurichi", "Tirunelveli", "Kayathar"],
        festivals=["Kattabomman Memorial Day"],
        keywords=["Freedom", "British", "Fort", "Courage", "Resistance", "Polygar"],
        story_seeds=[
            "The brave chieftain who refused to bow before foreign rulers",
            "A warrior whose fort became a symbol of Tamil pride",
            "The hero who united Tamil warriors against injustice"
        ]
    ),
    
    "dheeran_chinnamalai": TamilEntity(
        name="Dheeran Chinnamalai",
        type="freedom_fighter",
        era="Polygar Wars (1756-1805)",
        region="Kongu Nadu",
        short_bio="Kongu chieftain who fought against British and Tipu Sultan",
        known_for=["Guerrilla warfare", "Kongu resistance", "Anti-British campaigns"],
        associated_places=["Erode", "Coimbatore", "Odanilai", "Sankagiri"],
        festivals=["Chinnamalai Memorial Day"],
        keywords=["Kongu", "Guerrilla", "British", "Tipu", "Resistance", "Warrior"],
        story_seeds=[
            "The Kongu warrior who fought on two fronts for Tamil freedom",
            "A chieftain whose guerrilla tactics puzzled mighty armies",
            "The hero who chose death over surrender to foreign rule"
        ]
    ),
    
    "puli_thevar": TamilEntity(
        name="Puli Thevar",
        type="freedom_fighter",
        era="Carnatic Wars (1715-1767)",
        region="Nelkattumseval",
        short_bio="First Polygar to resist British expansion in South India",
        known_for=["First resistance to British", "Polygar wars pioneer", "Nelkattumseval fort"],
        associated_places=["Nelkattumseval", "Sankarankovil", "Tenkasi"],
        festivals=["Puli Thevar Day"],
        keywords=["First", "Resistance", "Polygar", "British", "Pioneer", "Fort"],
        story_seeds=[
            "The first Tamil warrior to say 'No' to British expansion",
            "A tiger-hearted chief who showed the path of resistance",
            "The pioneer who lit the flame of Tamil freedom struggle"
        ]
    ),
    
    "rani_velu_nachiyar": TamilEntity(
        name="Rani Velu Nachiyar",
        type="queen",
        era="18th Century (1730-1796)",
        region="Sivaganga",
        short_bio="First Indian queen to fight against British, known as Veeramangai",
        known_for=["First queen to fight British", "Guerrilla warfare", "Women warriors", "Sivaganga kingdom"],
        associated_places=["Sivaganga", "Dindigul", "Madurai", "Virudhunagar"],
        festivals=["Veeramangai Day", "Women's Day celebrations"],
        keywords=["Queen", "Veeramangai", "British", "Courage", "Women", "Sivaganga"],
        story_seeds=[
            "The queen who trained women warriors to fight for freedom",
            "A brave mother who reclaimed her kingdom from foreign invaders",
            "The first Indian queen who dared to challenge the British Empire"
        ]
    ),
    
    "marudhu_brothers": TamilEntity(
        name="Marudhu Brothers",
        type="freedom_fighter",
        era="Polygar Wars (1783-1801)",
        region="Sivaganga",
        short_bio="Periya Marudhu and Chinna Marudhu, loyal commanders of Sivaganga",
        known_for=["Loyalty to Rani Velu Nachiyar", "Guerrilla warfare", "Proclamation against British"],
        associated_places=["Sivaganga", "Kalayarkoil", "Tiruppathur"],
        festivals=["Marudhu Brothers Memorial Day"],
        keywords=["Brothers", "Loyalty", "Guerrilla", "Sivaganga", "Proclamation", "Unity"],
        story_seeds=[
            "Two brothers whose loyalty to their queen became legendary",
            "Warriors who wrote the first proclamation of independence",
            "Brothers who showed that unity can defeat any enemy"
        ]
    ),

    # Tamil Mythological Figures
    "kannagi": TamilEntity(
        name="Kannagi",
        type="epic_character",
        era="Sangam Period (2nd Century CE)",
        region="Madurai",
        short_bio="Heroine of Silappatikaram, symbol of chastity and justice",
        known_for=["Silappatikaram epic", "Justice for husband", "Burning of Madurai", "Chastity"],
        associated_places=["Madurai", "Puhar", "Vanji"],
        festivals=["Kannagi Festival", "Silappatikaram Day"],
        keywords=["Justice", "Chastity", "Silappatikaram", "Madurai", "Truth", "Dharma"],
        story_seeds=[
            "The devoted wife who proved that truth always triumphs",
            "A woman whose righteous anger shook the foundations of injustice",
            "The eternal symbol of a woman's strength and virtue"
        ]
    ),
    
    "manimekalai": TamilEntity(
        name="Manimekalai",
        type="epic_character",
        era="Post-Sangam Period (6th Century CE)",
        region="Puhar",
        short_bio="Heroine of Manimekalai epic, daughter of Madhavi, Buddhist saint",
        known_for=["Manimekalai epic", "Buddhist teachings", "Compassion", "Renunciation"],
        associated_places=["Puhar", "Kanchipuram", "Nagapattinam"],
        festivals=["Buddha Purnima", "Manimekalai Day"],
        keywords=["Buddhism", "Compassion", "Renunciation", "Wisdom", "Service", "Dharma"],
        story_seeds=[
            "The dancer's daughter who chose the path of compassion",
            "A princess who found true wealth in serving others",
            "The saint who taught that love conquers all desires"
        ]
    ),
    
    "thiruvalluvar": TamilEntity(
        name="Thiruvalluvar",
        type="saint_poet",
        era="Classical Period (1st Century BCE - 5th Century CE)",
        region="Mylapore",
        short_bio="Great Tamil poet and philosopher, author of Thirukkural",
        known_for=["Thirukkural", "Universal ethics", "Moral philosophy", "Tamil literature"],
        associated_places=["Mylapore", "Kanyakumari", "Madurai"],
        festivals=["Thiruvalluvar Day", "Tamil New Year"],
        keywords=["Thirukkural", "Ethics", "Wisdom", "Philosophy", "Virtue", "Universal"],
        story_seeds=[
            "The weaver-poet whose words became eternal wisdom",
            "A saint whose teachings guide humanity across all faiths",
            "The philosopher who captured life's truths in simple couplets"
        ]
    ),
    
    "kovalan": TamilEntity(
        name="Kovalan",
        type="epic_character",
        era="Sangam Period (2nd Century CE)",
        region="Puhar",
        short_bio="Hero of Silappatikaram, merchant prince and husband of Kannagi",
        known_for=["Silappatikaram epic", "Tragic fate", "Love story with Madhavi"],
        associated_places=["Puhar", "Madurai", "Vanji"],
        festivals=["Silappatikaram Day"],
        keywords=["Love", "Tragedy", "Merchant", "Silappatikaram", "Fate", "Redemption"],
        story_seeds=[
            "The merchant prince whose love story became an eternal epic",
            "A man who learned the true value of loyalty through loss",
            "The tragic hero whose story teaches about consequences"
        ]
    ),

    # Tamil Deities
    "murugan": TamilEntity(
        name="Murugan",
        type="deity",
        era="Eternal",
        region="Tamil Nadu",
        short_bio="Tamil God of War, son of Shiva, patron deity of Tamil Nadu",
        known_for=["Vel (spear)", "Peacock mount", "Six faces", "Palani temple", "Thiruchendur"],
        associated_places=["Palani", "Thiruchendur", "Swamimalai", "Pazhamudircholai", "Thirupparamkunram", "Thiruthani"],
        festivals=["Thaipusam", "Skanda Sashti", "Panguni Uthiram"],
        keywords=["Murugan", "Vel", "Peacock", "War", "Victory", "Tamil", "Devotion"],
        story_seeds=[
            "The young god who defeated the mighty demon Surapadman",
            "The divine child who chose Tamil devotees over Sanskrit scholars",
            "The warrior god whose vel protects all Tamil lands"
        ]
    ),
    
    "mariamman": TamilEntity(
        name="Mariamman",
        type="deity",
        era="Eternal",
        region="Tamil Nadu",
        short_bio="Village goddess of rain, fertility, and disease prevention",
        known_for=["Rain goddess", "Village protector", "Disease prevention", "Fertility"],
        associated_places=["Samayapuram", "Uraiyur", "Villages across Tamil Nadu"],
        festivals=["Mariamman Festival", "Aadi Perukku", "Village festivals"],
        keywords=["Rain", "Village", "Protection", "Fertility", "Goddess", "Mother"],
        story_seeds=[
            "The village mother who brings rain to drought-stricken lands",
            "The protective goddess who shields villages from disease",
            "The divine mother whose blessings ensure good harvests"
        ]
    ),
    
    "ayyanar": TamilEntity(
        name="Ayyanar",
        type="deity",
        era="Eternal",
        region="Tamil Nadu",
        short_bio="Village guardian deity, protector of boundaries and villages",
        known_for=["Village guardian", "Boundary protection", "Horse mount", "Night patrol"],
        associated_places=["Village boundaries", "Forests", "Rural Tamil Nadu"],
        festivals=["Ayyanar Festival", "Village protection ceremonies"],
        keywords=["Guardian", "Village", "Protection", "Horse", "Boundary", "Night"],
        story_seeds=[
            "The guardian god who patrols village boundaries on his white horse",
            "The protector deity who keeps evil spirits away from villages",
            "The divine sentinel whose vigilance ensures peaceful sleep"
        ]
    ),
    
    "meenakshi": TamilEntity(
        name="Meenakshi",
        type="deity",
        era="Eternal",
        region="Madurai",
        short_bio="Fish-eyed goddess, consort of Sundareswarar, patron of Madurai",
        known_for=["Meenakshi Temple", "Fish-shaped eyes", "Warrior goddess", "Divine marriage"],
        associated_places=["Madurai", "Meenakshi Amman Temple"],
        festivals=["Chithirai Thiruvizha", "Meenakshi Tirukalyanam", "Navarathri"],
        keywords=["Meenakshi", "Madurai", "Temple", "Marriage", "Goddess", "Fish", "Eyes"],
        story_seeds=[
            "The warrior princess who became the beloved goddess of Madurai",
            "The divine queen whose marriage celebration lasts for days",
            "The fish-eyed goddess who protects her devotees like a mother"
        ]
    ),

    # Additional Tamil Saints and Poets
    "appar": TamilEntity(
        name="Appar",
        type="saint_poet",
        era="7th Century CE",
        region="Tamil Nadu",
        short_bio="One of the four great Saiva saints, composer of Tevaram",
        known_for=["Tevaram hymns", "Saiva devotion", "Temple songs", "Spiritual poetry"],
        associated_places=["Tiruvaduthurai", "Chidambaram", "Saiva temples"],
        festivals=["Appar Jayanti", "Tevaram Festival"],
        keywords=["Saint", "Tevaram", "Saiva", "Devotion", "Poetry", "Temple"],
        story_seeds=[
            "The saint whose songs made stones dance with devotion",
            "A poet whose hymns echo in every Siva temple",
            "The devotee who found God in every grain of sand"
        ]
    ),
    
    "sambandar": TamilEntity(
        name="Sambandar",
        type="saint_poet",
        era="7th Century CE",
        region="Tamil Nadu",
        short_bio="Child saint and composer of Tevaram, one of the four great Saiva saints",
        known_for=["Child saint", "Tevaram hymns", "Miracles", "Saiva devotion"],
        associated_places=["Sirkazhi", "Saiva temples across Tamil Nadu"],
        festivals=["Sambandar Jayanti", "Tevaram Festival"],
        keywords=["Child", "Saint", "Tevaram", "Miracle", "Saiva", "Devotion"],
        story_seeds=[
            "The child saint who sang his way to God's heart",
            "A young devotee whose voice could move mountains",
            "The miracle child who proved that age is no barrier to devotion"
        ]
    ),
    
    "andal": TamilEntity(
        name="Andal",
        type="saint_poet",
        era="8th Century CE",
        region="Srivilliputhur",
        short_bio="Only female Alvar saint, composed Tiruppavai and Nachiyar Tirumozhi",
        known_for=["Tiruppavai", "Nachiyar Tirumozhi", "Vaishnava devotion", "Female saint"],
        associated_places=["Srivilliputhur", "Srirangam", "Vaishnava temples"],
        festivals=["Andal Jayanti", "Tiruppavai Festival", "Margazhi celebrations"],
        keywords=["Saint", "Andal", "Tiruppavai", "Vaishnava", "Devotion", "Female"],
        story_seeds=[
            "The girl who dreamed of marrying Lord Vishnu",
            "A young saint whose songs wake up the divine",
            "The devotee who showed that love knows no boundaries"
        ]
    )
}

# Tamil Nadu Places Database
TAMIL_PLACES = {
    "madurai": TamilPlace(
        name="Madurai",
        type="city",
        district="Madurai",
        description="Ancient city known as Athens of the East, famous for Meenakshi Temple",
        main_legend="City where Meenakshi and Sundareswarar got married, witnessed by all gods",
        historical_significance="Capital of Pandya kingdom, center of Tamil literature and culture",
        associated_entities=["Meenakshi", "Sundareswarar", "Pandya Kings", "Kannagi"],
        festivals=["Chithirai Thiruvizha", "Float Festival", "Navarathri"]
    ),
    
    "thanjavur": TamilPlace(
        name="Thanjavur",
        type="city",
        district="Thanjavur",
        description="Cultural capital of Tamil Nadu, home to Brihadeeswarar Temple",
        main_legend="City built by Chola emperors as their capital and center of art",
        historical_significance="Capital of Chola Empire, UNESCO World Heritage site",
        associated_entities=["Raja Raja Chola", "Rajendra Chola", "Chola Dynasty"],
        festivals=["Brihadeeswarar Temple Festival", "Dance Festival", "Chola Heritage Festival"]
    ),
    
    "palani": TamilPlace(
        name="Palani",
        type="temple",
        district="Dindigul",
        description="Sacred hill temple of Lord Murugan, one of six abodes",
        main_legend="Place where Murugan chose to live after losing the fruit of wisdom contest",
        historical_significance="Ancient temple mentioned in Sangam literature",
        associated_entities=["Murugan", "Bogar Siddhar"],
        festivals=["Thaipusam", "Panguni Uthiram", "Thai Poosam"]
    ),
    
    "panchalankurichi": TamilPlace(
        name="Panchalankurichi",
        type="fort",
        district="Tirunelveli",
        description="Historic fort of Veerapandiya Kattabomman",
        main_legend="Fort where the brave Polygar chief defied the British Empire",
        historical_significance="Symbol of Tamil resistance against British colonialism",
        associated_entities=["Veerapandiya Kattabomman"],
        festivals=["Kattabomman Memorial Day", "Freedom Fighters Day"]
    ),
    
    "sivaganga": TamilPlace(
        name="Sivaganga",
        type="fort",
        district="Sivaganga",
        description="Historic kingdom of Rani Velu Nachiyar and Marudhu Brothers",
        main_legend="Kingdom where the first Indian queen fought against British rule",
        historical_significance="Center of Tamil resistance, ruled by brave queen and loyal commanders",
        associated_entities=["Rani Velu Nachiyar", "Marudhu Brothers"],
        festivals=["Veeramangai Day", "Marudhu Brothers Memorial"]
    ),
    
    "chidambaram": TamilPlace(
        name="Chidambaram",
        type="temple",
        district="Cuddalore",
        description="Sacred temple of Nataraja, cosmic dancer Shiva",
        main_legend="Place where Shiva performed the cosmic dance of creation",
        historical_significance="One of the Pancha Bhoota Sthalams, center of Saiva philosophy",
        associated_entities=["Nataraja", "Shiva", "Saiva Saints"],
        festivals=["Natyanjali", "Arudra Darshan", "Margazhi Festival"]
    ),
    
    "rameswaram": TamilPlace(
        name="Rameswaram",
        type="temple",
        district="Ramanathapuram",
        description="Sacred island temple, one of the Char Dham pilgrimage sites",
        main_legend="Place where Rama worshipped Shiva before crossing to Lanka",
        historical_significance="One of the holiest pilgrimage sites, connects Ramayana to Tamil Nadu",
        associated_entities=["Rama", "Hanuman", "Ramayana"],
        festivals=["Rama Navami", "Hanuman Jayanti", "Maha Shivaratri"]
    )
}

# Tamil Story Types and Keywords
TAMIL_STORY_TYPES = {
    "tamil_history_royal": {
        "keywords": ["Chola", "Pandya", "Chera", "King", "Queen", "Empire", "Temple", "Architecture"],
        "themes": ["good governance", "architecture", "trade", "cultural patronage", "justice"],
        "age_variants": {
            "kids": "Stories of wise kings who built beautiful temples and helped their people",
            "adults": "Detailed accounts of political strategy, architectural marvels, and cultural achievements"
        },
        "festivals": ["Chithirai Festival", "Heritage Day", "Temple Festivals"]
    },
    
    "tamil_freedom_fighters": {
        "keywords": ["Kattabomman", "Velu Nachiyar", "Marudhu", "British", "Freedom", "Courage", "Fort"],
        "themes": ["resistance", "sacrifice", "patriotism", "unity", "courage"],
        "age_variants": {
            "kids": "Stories of brave heroes who protected their homeland from bullies",
            "adults": "Historical accounts of strategic resistance and sacrifice for freedom"
        },
        "festivals": ["Independence Day", "Freedom Fighters Day", "Martyrs Day"]
    },
    
    "tamil_epics": {
        "keywords": ["Silappatikaram", "Kannagi", "Kovalan", "Justice", "Truth", "Dharma"],
        "themes": ["justice", "truth", "dharma", "love", "consequences", "virtue"],
        "age_variants": {
            "kids": "Stories about the importance of truth and standing up for what's right",
            "adults": "Complex narratives about justice, love, and moral consequences"
        },
        "festivals": ["Silappatikaram Day", "Tamil Literature Day"]
    },
    
    "tamil_devotional": {
        "keywords": ["Murugan", "Meenakshi", "Palani", "Madurai", "Devotion", "Temple", "Festival"],
        "themes": ["devotion", "faith", "divine grace", "temple traditions", "festivals"],
        "age_variants": {
            "kids": "Stories of gods who love and protect their devotees",
            "adults": "Deep spiritual narratives about divine grace and temple traditions"
        },
        "festivals": ["Thaipusam", "Chithirai Thiruvizha", "Skanda Sashti"]
    }
}

# Tamil Keywords Database (extends existing mythology keywords)
TAMIL_KEYWORDS = {
    "tamil_kings": [
        "Raja Raja Chola", "Rajendra Chola", "Karikala Chola", "Rajaraja", "Rajendra",
        "Chola", "Pandya", "Chera", "Pallava", "Neduncheliyan", "Mudukudumi",
        "Kulottunga", "Aditya Chola", "Parantaka", "Sundara Chola", "Uttama Chola"
    ],
    "tamil_queens": [
        "Rani Velu Nachiyar", "Veeramangai", "Meenakshi", "Kundavai", "Sembiyan Mahadevi"
    ],
    "tamil_heroes": [
        "Veerapandiya Kattabomman", "Kattabomman", "Marudhu Brothers", "Periya Marudhu", 
        "Chinna Marudhu", "Dheeran Chinnamalai", "Puli Thevar", "Oomathurai",
        "Velu Nachiyar", "Veeramangai", "Polygar", "Freedom Fighter", "Warrior"
    ],
    "tamil_epics": [
        "Silappatikaram", "Manimekalai", "Kannagi", "Kovalan", "Madhavi", "Purananuru",
        "Akananuru", "Sangam", "Tolkappiyam", "Thirukkural", "Thiruvalluvar",
        "Kambaramayanam", "Kambar", "Periya Puranam", "Nayanmars", "Alvars"
    ],
    "tamil_deities": [
        "Murugan", "Meenakshi", "Sundareswarar", "Nataraja", "Mariamman", "Ayyanar",
        "Kartikeya", "Skanda", "Subrahmanya", "Valli", "Devasena", "Andal"
    ],
    "tamil_saints": [
        "Appar", "Sambandar", "Sundarar", "Manikkavasagar", "Andal", "Periyalvar",
        "Nammalvar", "Thirumangai Alvar", "Kulasekara Alvar"
    ],
    "tamil_places": [
        "Madurai", "Thanjavur", "Palani", "Thiruchendur", "Chidambaram", "Rameswaram",
        "Kanyakumari", "Panchalankurichi", "Sivaganga", "Gangaikonda Cholapuram"
    ],
    "tamil_symbols": [
        "Vel", "Peacock", "Rooster", "Tiger", "Fish", "Lotus", "Conch", "Drum",
        "Trishul", "Chakra", "Bow", "Spear", "Anklet", "Silappathikaram"
    ],
    "tamil_festivals": [
        "Thaipusam", "Chithirai Thiruvizha", "Meenakshi Tirukalyanam", "Skanda Sashti",
        "Panguni Uthiram", "Aadi Perukku", "Karthigai Deepam", "Thai Pusam", "Pongal"
    ],
    "tamil_arts": [
        "Bharatanatyam", "Tanjore Painting", "Bronze Sculpture", "Temple Architecture",
        "Chola Art", "Dravidian Style", "Gopuram", "Mandapa"
    ]
}

# Tamil Art Styles (extends existing art styles)
TAMIL_ART_STYLES = {
    "chola_bronze": "Chola bronze sculpture style, elegant poses, divine expressions, intricate details",
    "dravidian_temple": "Dravidian temple architecture, towering gopurams, intricate carvings, stone sculptures",
    "tanjore_traditional": "Traditional Tanjore painting, rich colors, gold foil work, divine themes, gem inlays",
    "tamil_folk": "Tamil folk art style, bright colors, village themes, traditional motifs, storytelling art",
    "sangam_classical": "Classical Sangam period art, elegant simplicity, natural themes, poetic visualization"
}

# Tamil Story Templates
TAMIL_STORY_TEMPLATES = {
    "kids_tamil_king": """
    Long ago in beautiful Tamil Nadu, there lived a wise king named {king_name} in the city of {place}. 
    He loved his people very much and wanted to make their lives happy and peaceful.
    
    One day, the king noticed that {problem}. The people were worried and didn't know what to do.
    The kind king thought carefully and came up with a wonderful plan.
    
    {solution_description}
    
    The people were so happy! They celebrated with music, dance, and delicious food.
    From that day on, everyone remembered the wise king who {moral_lesson}.
    
    And that's why we still celebrate {festival} to remember this great king!
    """,
    
    "kids_tamil_hero": """
    In the land of Tamil Nadu, there lived a brave hero named {hero_name}.
    {hero_name} loved their homeland and all the people who lived there.
    
    One day, some mean bullies from far away came to trouble the peaceful villages.
    They wanted to take away the people's happiness and freedom.
    
    But {hero_name} was very brave! With the help of friends and family,
    they stood up to the bullies and said, "You cannot hurt our people!"
    
    {heroic_action}
    
    The bullies realized they were wrong and went away. All the villages celebrated
    with colorful festivals, and everyone learned that {moral_lesson}.
    
    We still remember {hero_name} during {festival} and tell stories of their courage!
    """,
    
    "adult_tamil_history": """
    In the golden age of Tamil civilization, during the {era}, the great {ruler_name} 
    ruled from the magnificent city of {capital}. This was a time when Tamil culture, 
    art, and architecture reached unprecedented heights.
    
    {historical_context}
    
    The challenge that faced {ruler_name} was {main_conflict}. The stakes were high,
    for the very future of Tamil civilization hung in the balance.
    
    Drawing upon the ancient wisdom of Tamil literature and the counsel of learned ministers,
    {ruler_name} devised a strategy that would {solution_approach}.
    
    {detailed_resolution}
    
    The success of this endeavor not only secured the immediate prosperity of the kingdom
    but also established traditions that continue to enrich Tamil culture today.
    The festival of {festival} commemorates this great achievement, reminding us that
    {philosophical_moral}.
    
    Thus, the legacy of {ruler_name} lives on in the temples, literature, and traditions
    of Tamil Nadu, inspiring generations to uphold the values of {core_values}.
    """
}

def get_tamil_entity(name: str) -> Optional[TamilEntity]:
    """Get Tamil entity by name"""
    return TAMIL_HISTORICAL_ENTITIES.get(name.lower().replace(" ", "_"))

def get_tamil_place(name: str) -> Optional[TamilPlace]:
    """Get Tamil place by name"""
    return TAMIL_PLACES.get(name.lower().replace(" ", "_"))

def detect_tamil_keywords(keywords: List[str]) -> Dict[str, List[str]]:
    """Detect Tamil-specific keywords and categorize them"""
    tamil_matches = {}
    
    for category, tamil_words in TAMIL_KEYWORDS.items():
        matches = []
        for keyword in keywords:
            for tamil_word in tamil_words:
                if keyword.lower() in tamil_word.lower() or tamil_word.lower() in keyword.lower():
                    matches.append(tamil_word)
        if matches:
            tamil_matches[category] = matches
    
    return tamil_matches

def suggest_tamil_keywords(existing_keywords: List[str]) -> List[str]:
    """Suggest related Tamil keywords based on existing ones"""
    suggestions = []
    tamil_matches = detect_tamil_keywords(existing_keywords)
    
    # Add related keywords based on detected categories
    if "tamil_kings" in tamil_matches:
        suggestions.extend(["Temple", "Architecture", "Cauvery", "Empire"])
    if "tamil_heroes" in tamil_matches:
        suggestions.extend(["Freedom", "Courage", "Fort", "British"])
    if "tamil_deities" in tamil_matches:
        suggestions.extend(["Temple", "Festival", "Devotion", "Miracle"])
    if "tamil_epics" in tamil_matches:
        suggestions.extend(["Justice", "Truth", "Dharma", "Love"])
    
    return list(set(suggestions))[:5]

def get_tamil_story_type(keywords: List[str]) -> str:
    """Determine Tamil story type based on keywords"""
    tamil_matches = detect_tamil_keywords(keywords)
    
    if "tamil_kings" in tamil_matches or "tamil_queens" in tamil_matches:
        return "tamil_history_royal"
    elif "tamil_heroes" in tamil_matches:
        return "tamil_freedom_fighters"
    elif "tamil_epics" in tamil_matches:
        return "tamil_epics"
    elif "tamil_deities" in tamil_matches:
        return "tamil_devotional"
    else:
        return "general_tamil"

def get_tamil_festival(keywords: List[str], story_type: str) -> str:
    """Get appropriate Tamil festival based on keywords and story type"""
    tamil_matches = detect_tamil_keywords(keywords)
    
    # Direct festival matches
    if "tamil_festivals" in tamil_matches:
        return tamil_matches["tamil_festivals"][0]
    
    # Story type based festivals
    festival_mapping = {
        "tamil_history_royal": "Chithirai Festival",
        "tamil_freedom_fighters": "Independence Day",
        "tamil_epics": "Tamil Literature Day",
        "tamil_devotional": "Thaipusam"
    }
    
    return festival_mapping.get(story_type, "Pongal")

# Export all Tamil knowledge for integration
__all__ = [
    'TamilEntity', 'TamilPlace', 'TAMIL_HISTORICAL_ENTITIES', 'TAMIL_PLACES',
    'TAMIL_STORY_TYPES', 'TAMIL_KEYWORDS', 'TAMIL_ART_STYLES', 'TAMIL_STORY_TEMPLATES',
    'get_tamil_entity', 'get_tamil_place', 'detect_tamil_keywords', 
    'suggest_tamil_keywords', 'get_tamil_story_type', 'get_tamil_festival'
]