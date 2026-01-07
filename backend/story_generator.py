"""
Tamil Story Generator - Elaborate Stories with Cultural Images
"""

import os
import sys
from typing import List, Dict, Optional
from dataclasses import dataclass

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from knowledge_base import (
    get_tamil_entity, get_tamil_place, detect_tamil_keywords,
    get_tamil_festival, TAMIL_HISTORICAL_ENTITIES
)

# Story-specific images - using Picsum for reliable loading
STORY_PAGE_IMAGES = {
    "raja raja chola": {
        "kids": [
            "https://picsum.photos/seed/palace1/800/500",
            "https://picsum.photos/seed/learning1/800/500",
            "https://picsum.photos/seed/temple1/800/500",
            "https://picsum.photos/seed/building1/800/500",
            "https://picsum.photos/seed/temple2/800/500",
            "https://picsum.photos/seed/nature1/800/500",
            "https://picsum.photos/seed/ships1/800/500",
            "https://picsum.photos/seed/legacy1/800/500",
        ],
        "adults": [
            "https://picsum.photos/seed/empire1/800/500",
            "https://picsum.photos/seed/naval1/800/500",
            "https://picsum.photos/seed/arts1/800/500",
            "https://picsum.photos/seed/council1/800/500",
            "https://picsum.photos/seed/engineer1/800/500",
            "https://picsum.photos/seed/culture1/800/500",
            "https://picsum.photos/seed/diplomat1/800/500",
            "https://picsum.photos/seed/heritage1/800/500",
        ]
    },
    "kattabomman": {
        "kids": [
            "https://picsum.photos/seed/fort1/800/500",
            "https://picsum.photos/seed/british1/800/500",
            "https://picsum.photos/seed/proud1/800/500",
            "https://picsum.photos/seed/battle1/800/500",
            "https://picsum.photos/seed/sacrifice1/800/500",
            "https://picsum.photos/seed/memorial1/800/500",
            "https://picsum.photos/seed/lessons1/800/500",
            "https://picsum.photos/seed/remember1/800/500",
        ],
        "adults": [
            "https://picsum.photos/seed/polygar1/800/500",
            "https://picsum.photos/seed/colonial1/800/500",
            "https://picsum.photos/seed/diplomacy1/800/500",
            "https://picsum.photos/seed/siege1/800/500",
            "https://picsum.photos/seed/betrayal1/800/500",
            "https://picsum.photos/seed/trial1/800/500",
            "https://picsum.photos/seed/freedom1/800/500",
            "https://picsum.photos/seed/history1/800/500",
        ]
    },
    "murugan": {
        "kids": [
            "https://picsum.photos/seed/divine1/800/500",
            "https://picsum.photos/seed/demon1/800/500",
            "https://picsum.photos/seed/weapon1/800/500",
            "https://picsum.photos/seed/battle2/800/500",
            "https://picsum.photos/seed/temples1/800/500",
            "https://picsum.photos/seed/tamil1/800/500",
            "https://picsum.photos/seed/teach1/800/500",
            "https://picsum.photos/seed/protect1/800/500",
        ],
        "adults": [
            "https://picsum.photos/seed/cosmos1/800/500",
            "https://picsum.photos/seed/sura1/800/500",
            "https://picsum.photos/seed/arupadai1/800/500",
            "https://picsum.photos/seed/sangam1/800/500",
            "https://picsum.photos/seed/philo1/800/500",
            "https://picsum.photos/seed/kavadi1/800/500",
            "https://picsum.photos/seed/identity1/800/500",
            "https://picsum.photos/seed/universal1/800/500",
        ]
    }
}

# Default images for different story themes
DEFAULT_STORY_IMAGES = {
    "introduction": "https://picsum.photos/seed/intro1/800/500",
    "learning": "https://picsum.photos/seed/learn1/800/500",
    "challenge": "https://picsum.photos/seed/challenge1/800/500",
    "journey": "https://picsum.photos/seed/journey1/800/500",
    "solution": "https://picsum.photos/seed/solution1/800/500",
    "success": "https://picsum.photos/seed/success1/800/500",
    "celebration": "https://picsum.photos/seed/celebrate1/800/500",
    "legacy": "https://picsum.photos/seed/legacy2/800/500",
}

DEFAULT_IMAGES = [
    "https://picsum.photos/seed/default1/800/500",
    "https://picsum.photos/seed/default2/800/500",
    "https://picsum.photos/seed/default3/800/500",
    "https://picsum.photos/seed/default4/800/500",
    "https://picsum.photos/seed/default5/800/500",
    "https://picsum.photos/seed/default6/800/500",
    "https://picsum.photos/seed/default7/800/500",
    "https://picsum.photos/seed/default8/800/500",
]

def get_story_images(keyword: str, age_group: str) -> List[str]:
    """Get story-specific images based on keyword and age group"""
    key = keyword.lower().strip()
    age = "kids" if age_group == "kids" else "adults"
    
    if key in STORY_PAGE_IMAGES and age in STORY_PAGE_IMAGES[key]:
        return STORY_PAGE_IMAGES[key][age]
    
    # Check partial match
    for k in STORY_PAGE_IMAGES:
        if k in key or key in k:
            if age in STORY_PAGE_IMAGES[k]:
                return STORY_PAGE_IMAGES[k][age]
    
    return DEFAULT_IMAGES


# Elaborate story templates for each keyword
STORY_TEMPLATES = {
    "raja raja chola": {
        "title": "Raja Raja Chola - The Great Emperor",
        "era": "985-1014 CE",
        "region": "Thanjavur, Tamil Nadu",
        "kids": [
            {
                "title": "A Prince is Born",
                "content": "Long, long ago, in the beautiful kingdom of the Cholas in South India, a special baby boy was born. His name was Arulmozhi Varman, but the world would come to know him as Raja Raja Chola - one of the greatest kings ever! His father was King Parantaka II, and from the very beginning, everyone could see that this little prince was destined for greatness. The palace was filled with joy, and the priests blessed the baby, saying he would bring glory to the Chola dynasty."
            },
            {
                "title": "Learning to be a King",
                "content": "As young Arulmozhi grew up, he learned many important things. He studied the ancient Tamil texts, learned to ride horses and elephants, and practiced sword fighting with the best warriors. But most importantly, he learned to be kind and fair to everyone. His teachers taught him that a good king must love his people like his own family. The young prince would often sneak out of the palace to play with the village children and understand how ordinary people lived."
            },
            {
                "title": "Becoming the King",
                "content": "When Arulmozhi became king, he took the grand title 'Raja Raja' which means 'King of Kings.' He was determined to make his kingdom the greatest in all of India! He gathered his wise ministers and brave generals and said, 'Together, we shall build a kingdom that people will remember for thousands of years!' The people cheered, for they knew their new king was special."
            },
            {
                "title": "Building the Great Temple",
                "content": "Raja Raja Chola had a magnificent dream - to build the biggest and most beautiful temple in the world! He called the best architects, sculptors, and artists from across the land. For years, thousands of workers carved huge stones and created beautiful sculptures. The king himself would visit the construction site every day, encouraging the workers and making sure everything was perfect. This temple would be dedicated to Lord Shiva."
            },
            {
                "title": "The Brihadeeswarar Temple",
                "content": "After many years of hard work, the temple was finally complete! It was called the Brihadeeswarar Temple, and it was absolutely magnificent. The main tower stood 216 feet tall - taller than any building anyone had ever seen! The dome at the top was carved from a single piece of granite weighing 80 tons. People came from far and wide just to see this wonder. Raja Raja Chola stood proudly, knowing he had created something that would last forever."
            },
            {
                "title": "A Kind and Just Ruler",
                "content": "Raja Raja Chola wasn't just a great builder - he was also a kind and fair king. He made sure that farmers had water for their crops by building canals and lakes. He reduced taxes for poor people and punished anyone who was cruel to others. He respected all religions and gave gifts to temples, churches, and mosques. The people loved their king because he truly cared about their happiness."
            },
            {
                "title": "The Mighty Navy",
                "content": "Raja Raja Chola built the most powerful navy in all of Asia! His ships sailed across the seas to Sri Lanka, the Maldives, and even to faraway lands in Southeast Asia. But he didn't just want to conquer - he wanted to trade and share Tamil culture with the world. Tamil merchants brought spices, silk, and precious gems, making the Chola kingdom very wealthy. The Chola flag flew proudly on ships across the Indian Ocean!"
            },
            {
                "title": "A Legacy Forever",
                "content": "Raja Raja Chola ruled for 29 glorious years. When he passed away, the entire kingdom mourned their beloved king. But his legacy lives on even today, more than 1000 years later! The Brihadeeswarar Temple still stands tall in Thanjavur, and millions of people visit it every year. Raja Raja Chola taught us that with hard work, kindness, and big dreams, we can create things that last forever. He remains one of the greatest kings in all of history!"
            }
        ],
        "adults": [
            {
                "title": "The Rise of an Emperor",
                "content": "In 985 CE, Arulmozhi Varman ascended the Chola throne, adopting the imperial title Rajaraja - 'King of Kings.' Born into the illustrious Chola dynasty, he inherited a kingdom with immense potential but facing significant challenges. The young monarch possessed a rare combination of military genius, administrative acumen, and cultural vision that would transform the Chola Empire into one of the most powerful maritime empires in Asian history. His coronation marked the beginning of what historians call the 'Golden Age of the Cholas.'"
            },
            {
                "title": "Military Conquests and Naval Supremacy",
                "content": "Raja Raja Chola's military campaigns were legendary in their scope and success. He systematically conquered the Pandya and Chera kingdoms, bringing the entire Tamil region under Chola control. His naval expeditions were even more remarkable - he captured Sri Lanka, the Maldive Islands, and established Chola influence across Southeast Asia. The Chola navy, with its advanced shipbuilding techniques and skilled sailors, dominated the Indian Ocean trade routes. His military strategy combined overwhelming force with diplomatic finesse, often incorporating defeated rulers into his administrative system."
            },
            {
                "title": "The Architectural Marvel of Thanjavur",
                "content": "Raja Raja Chola's most enduring legacy is the Brihadeeswarar Temple at Thanjavur, a UNESCO World Heritage Site. This architectural masterpiece, completed in 1010 CE, represents the pinnacle of Dravidian temple architecture. The vimana (temple tower) rises to 216 feet, crowned by a massive 80-ton granite capstone - an engineering feat that still puzzles modern architects. The temple complex covers 25 acres and features some of the finest Chola bronze sculptures and frescoes. The king personally supervised the construction, ensuring every detail met his exacting standards."
            },
            {
                "title": "Administrative Genius",
                "content": "Beyond his military and architectural achievements, Raja Raja Chola was a brilliant administrator. He conducted a comprehensive land survey of his empire, creating detailed records of agricultural land, irrigation systems, and tax assessments. These inscriptions, carved on temple walls, provide invaluable historical documentation. He reorganized the provincial administration, established an efficient revenue system, and created a network of local self-governing bodies. His administrative reforms ensured prosperity and stability throughout his vast empire."
            },
            {
                "title": "Patron of Arts and Culture",
                "content": "The Chola court under Raja Raja became a vibrant center of Tamil culture. He patronized poets, musicians, and scholars, leading to a renaissance in Tamil literature. The king commissioned the compilation of the Tevaram, sacred hymns of the Shaiva saints, preserving this invaluable literary heritage. Chola bronze casting reached its artistic zenith during his reign, producing masterpieces like the Nataraja that are now displayed in museums worldwide. Dance, music, and drama flourished under royal patronage."
            },
            {
                "title": "Religious Tolerance and Philanthropy",
                "content": "Despite being a devout Shaivite, Raja Raja Chola demonstrated remarkable religious tolerance. He made generous donations to Buddhist monasteries in Nagapattinam and supported Jain institutions. His inscriptions record gifts to various religious establishments regardless of faith. He established charitable institutions providing food, medicine, and education to the poor. This inclusive approach to governance earned him the love and loyalty of his diverse subjects and contributed to the social harmony of his empire."
            },
            {
                "title": "International Trade and Diplomacy",
                "content": "Raja Raja Chola transformed the Chola Empire into a major player in international trade. Tamil merchants, protected by the powerful Chola navy, established trading posts across Southeast Asia, influencing the cultures of present-day Indonesia, Malaysia, Thailand, and Cambodia. The empire traded in spices, textiles, gems, and precious metals. Diplomatic relations were maintained with China, the Srivijaya Empire, and the Abbasid Caliphate. The Chola influence on Southeast Asian art, architecture, and religion remains visible to this day."
            },
            {
                "title": "The Eternal Legacy",
                "content": "Raja Raja Chola passed away in 1014 CE after a reign of 29 years, leaving behind an empire at the height of its power and a legacy that transcends time. The Brihadeeswarar Temple stands as a testament to his vision, attracting millions of visitors annually. His administrative systems influenced governance in South India for centuries. The Chola bronzes are considered among the finest artistic achievements of medieval India. Raja Raja Chola exemplifies how enlightened leadership, combining military strength with cultural patronage and administrative efficiency, can create a civilization that endures through the ages."
            }
        ],
        "moral": "Great leaders build not just empires, but lasting legacies through wisdom, justice, and dedication to their people.",
        "facts": [
            "Raja Raja Chola built the Brihadeeswarar Temple with a 80-ton granite capstone at 216 feet height",
            "He created the most powerful navy in medieval Asia",
            "His land survey records are among the earliest detailed administrative documents in India",
            "The Chola Empire under him extended from Sri Lanka to Southeast Asia"
        ]
    },
}


# Add more story templates
STORY_TEMPLATES["kattabomman"] = {
    "title": "Veerapandiya Kattabomman - The Lion of Panchalankurichi",
    "era": "1760-1799 CE",
    "region": "Panchalankurichi, Tamil Nadu",
    "kids": [
        {"title": "The Brave Young Chief", "content": "In a small but proud kingdom called Panchalankurichi in Tamil Nadu, there lived a brave young man named Kattabomman. He became the chief of his people when he was very young. Kattabomman was tall, strong, and had eyes that sparkled with courage. He loved his land and his people more than anything else in the world. The villagers would say, 'Our Kattabomman is as brave as a lion!'"},
        {"title": "The British Arrive", "content": "During those times, the British from faraway England had come to India. They wanted to rule over all the Indian kingdoms and collect taxes from everyone. They sent their officers to Panchalankurichi and demanded that Kattabomman pay them money. But Kattabomman stood tall and said, 'This is my land! My ancestors ruled here for generations. I will not bow to foreigners!'"},
        {"title": "Standing Up for Freedom", "content": "The British were very angry that Kattabomman refused to obey them. They called him to their office in Ramanathapuram to scold him. But Kattabomman went there with his head held high. When the British officer insulted him, Kattabomman's eyes blazed with anger. He would not let anyone disrespect his honor or his people. He walked out proudly, ready to fight for freedom."},
        {"title": "The Battle Begins", "content": "The British sent a huge army to capture Kattabomman. But the brave chief was ready! He gathered his loyal warriors and prepared to defend his homeland. The battles were fierce. Kattabomman fought like a tiger, leading his men from the front. Even though the British had more soldiers and better weapons, Kattabomman's courage inspired his people to fight bravely."},
        {"title": "A Hero's Sacrifice", "content": "After many battles, Kattabomman was finally captured through treachery. The British decided to punish him to scare other Indian rulers. But even facing death, Kattabomman showed no fear. He stood proud and told the British, 'You may kill me, but you cannot kill the spirit of freedom in my people!' His bravery amazed even his enemies."},
        {"title": "The Spirit Lives On", "content": "Kattabomman became a martyr for Indian freedom on October 16, 1799. But his sacrifice was not in vain. His story inspired millions of Indians to fight for independence. Today, there is a grand memorial in Kayathar where people come to honor this great hero. Every year, on his death anniversary, thousands gather to remember the lion of Panchalankurichi."},
        {"title": "Lessons from Kattabomman", "content": "Kattabomman taught us that freedom is more precious than life itself. He showed that even a small kingdom can stand up against a mighty empire if its people have courage. He proved that true heroes fight not for themselves, but for their people and their land. His story reminds us to always stand up for what is right, no matter how difficult it may be."},
        {"title": "Remembered Forever", "content": "Today, Kattabomman is celebrated as one of India's greatest freedom fighters. Movies have been made about his life, songs are sung in his praise, and his statue stands tall in many places. He is proof that courage and love for one's country can make an ordinary person into an immortal hero. Veerapandiya Kattabomman - the name itself means 'brave warrior' - and he truly lived up to it!"}
    ],
    "adults": [
        {"title": "The Polygar of Panchalankurichi", "content": "Veerapandiya Kattabomman was born around 1760 into the Nayak dynasty that ruled Panchalankurichi, a small but strategically important palayam (feudal estate) in present-day Thoothukudi district. The Polygars were local chieftains who had established semi-autonomous rule during the decline of the Madurai Nayak kingdom. Kattabomman inherited the leadership at a young age and quickly proved himself a capable administrator and military leader, earning the fierce loyalty of his subjects."},
        {"title": "Resistance Against Colonial Taxation", "content": "The British East India Company, having established dominance over much of South India, demanded tribute from the Polygars. Kattabomman, unlike many of his contemporaries, refused to submit to what he considered illegitimate foreign authority. His defiance was rooted in a deep sense of sovereignty and honor. When summoned to Ramanathapuram in 1798 by the British Collector, he attended but refused to be humiliated, leading to a famous confrontation that nearly resulted in violence."},
        {"title": "The Diplomatic Struggle", "content": "Kattabomman attempted to build alliances with other Polygars, including Marudhu Pandiyar of Sivaganga, to present a united front against British expansion. He also sought to negotiate with the British from a position of strength rather than submission. However, the colonial administration, determined to establish absolute control, rejected any compromise. The British labeled him a rebel and began military preparations to crush his resistance."},
        {"title": "The Siege of Panchalankurichi", "content": "In 1799, the British launched a major military expedition against Panchalankurichi. Despite being vastly outnumbered and outgunned, Kattabomman's forces put up fierce resistance. The fort of Panchalankurichi, though not impregnable, was defended with extraordinary valor. The British suffered significant casualties before finally breaching the defenses. Kattabomman escaped the fallen fort, determined to continue the struggle."},
        {"title": "Betrayal and Capture", "content": "Seeking refuge with the Pudukottai Raja, Kattabomman was betrayed and handed over to the British. This act of treachery by a fellow Indian ruler remains one of the tragic aspects of the colonial period. Despite the betrayal, Kattabomman maintained his dignity and composure, refusing to show any sign of weakness before his captors."},
        {"title": "The Trial and Execution", "content": "The British conducted a summary trial at Kayathar, more a formality than a genuine legal proceeding. Kattabomman was sentenced to death by hanging. On October 16, 1799, he walked to the gallows with his head held high, reportedly telling the gathered crowd to continue the fight for freedom. His execution was meant to serve as a warning to other Indian rulers, but it had the opposite effect, turning him into a martyr and symbol of resistance."},
        {"title": "Legacy in the Freedom Movement", "content": "Kattabomman's resistance predated the 1857 uprising by nearly six decades, making him one of the earliest freedom fighters against British colonialism. His story was revived during the Indian independence movement, inspiring nationalists across the country. The 1959 Tamil film 'Veerapandiya Kattabomman' starring Sivaji Ganesan brought his story to millions, cementing his place in popular consciousness."},
        {"title": "Historical Significance", "content": "Kattabomman represents the spirit of resistance that existed throughout India against colonial rule. His refusal to compromise on sovereignty, his military courage, and his dignified acceptance of martyrdom embody the values that would later drive the Indian independence movement. The Kattabomman Memorial at Kayathar stands as a tribute to this remarkable leader. His life demonstrates that the struggle for Indian independence began not in 1857, but much earlier, in the hearts of brave individuals who refused to accept foreign domination."}
    ],
    "moral": "True courage means standing up for freedom and dignity, even against overwhelming odds.",
    "facts": [
        "Kattabomman was one of the earliest freedom fighters against British rule in India",
        "He was executed on October 16, 1799 at Kayathar",
        "The Kattabomman Memorial Fort is a major tourist attraction in Tamil Nadu",
        "His story inspired the famous 1959 Tamil film starring Sivaji Ganesan"
    ]
}


# Add Murugan story
STORY_TEMPLATES["murugan"] = {
    "title": "Lord Murugan - The Divine Warrior",
    "era": "Eternal - Hindu Mythology",
    "region": "Tamil Nadu, India",
    "kids": [
        {"title": "The Divine Child", "content": "In the heavenly abode of Mount Kailash, Lord Shiva and Goddess Parvati were blessed with a very special child. This divine baby had six faces and twelve arms! He was named Murugan, which means 'the beautiful one.' The gods and goddesses celebrated his birth with great joy, for they knew this child was destined to save the world from evil. Little Murugan's laughter echoed through the heavens like sweet music."},
        {"title": "The Demon's Terror", "content": "At that time, a terrible demon named Surapadman was causing great trouble. He had become so powerful that even the gods were afraid of him! Surapadman and his brothers conquered the heavens and made the gods their servants. The poor gods prayed to Lord Shiva for help. 'Only a child born of my power can defeat this demon,' said Lord Shiva. And so, young Murugan was chosen to be the savior."},
        {"title": "The Mighty Vel", "content": "Goddess Parvati gave her son a special weapon - the Vel, a divine spear that glowed with incredible power. This Vel was not just any weapon; it contained the energy of all the gods combined! When Murugan held the Vel, he felt the strength of the entire universe flowing through him. 'With this Vel,' said his mother, 'you will destroy evil and protect the good.'"},
        {"title": "The Great Battle", "content": "Young Murugan, riding his magnificent peacock, flew to battle the demons. The fight was fierce! Surapadman threw mountains and oceans at Murugan, but the brave god dodged them all. Finally, Murugan threw his powerful Vel at the demon. The Vel split Surapadman in two! But kind Murugan didn't destroy him completely - he transformed the demon into a peacock and a rooster, who became his loyal companions."},
        {"title": "The Six Abodes", "content": "After his victory, Lord Murugan chose six special places in Tamil Nadu as his homes. These are called the Arupadai Veedu - the six battle camps. Palani, Thiruchendur, Swamimalai, Thiruparankundram, Thiruthani, and Pazhamudircholai - each temple tells a different story of Murugan's adventures. Millions of devotees visit these temples every year to receive his blessings."},
        {"title": "The God of Tamil People", "content": "Lord Murugan became the most beloved god of the Tamil people. They call him by many loving names - Karthikeya, Skanda, Subramanya, and Arumugam (the six-faced one). During the festival of Thaipusam, devotees show their love by carrying kavadi and walking long distances to his temples. The chant 'Vel Vel Muruga' fills the air with devotion."},
        {"title": "Murugan's Teachings", "content": "Lord Murugan taught that courage and devotion can overcome any obstacle. He showed that even young people can do great things if they have faith and determination. He blessed the sage Agastya with the Tamil language, making him the patron of Tamil culture. Murugan represents the victory of good over evil, knowledge over ignorance, and light over darkness."},
        {"title": "The Eternal Protector", "content": "Even today, Lord Murugan watches over his devotees from his hill temples. When people face difficulties, they climb the steps to his shrine, and their troubles seem to melt away. The peacock, his vehicle, reminds us of beauty and grace. The Vel reminds us of the power of righteousness. Lord Murugan teaches us that with courage, faith, and a pure heart, we can overcome any challenge in life."}
    ],
    "adults": [
        {"title": "Origins in Hindu Cosmology", "content": "Lord Murugan, known as Kartikeya in North India and Skanda in Sanskrit texts, occupies a unique position in Hindu theology. According to the Skanda Purana, he was born from the third eye of Lord Shiva, his divine energy too powerful to be contained by any single mother. The six Krittikas (Pleiades stars) nursed him, giving him six faces. This cosmic origin establishes Murugan as the embodiment of divine martial energy, the commander of the celestial armies, and the god who bridges the gap between the transcendent and the immanent."},
        {"title": "The Surapadman Narrative", "content": "The central myth of Murugan involves his battle against the asura Surapadman, a demon who had obtained near-invincibility through severe penance. Surapadman's tyranny over the three worlds represents the cosmic imbalance that occurs when ego and desire go unchecked. Murugan's victory, achieved through the Vel (Shakti's gift), symbolizes the triumph of divine wisdom over demonic ignorance. The transformation of Surapadman into the peacock and rooster represents the redemptive aspect of divine justice."},
        {"title": "The Arupadai Veedu Tradition", "content": "The six abodes of Murugan in Tamil Nadu form a sacred geography that has shaped Tamil religious consciousness for millennia. Each temple - Thiruparankundram, Thiruchendur, Palani, Swamimalai, Thiruthani, and Pazhamudircholai - represents a different aspect of the deity and a different episode in his mythology. Pilgrimage to these sites, often undertaken on foot, is considered one of the most meritorious acts in Tamil Shaivism. The temples themselves are architectural marvels, with Palani and Thiruchendur attracting millions of devotees annually."},
        {"title": "Murugan in Sangam Literature", "content": "The worship of Murugan predates the arrival of Vedic religion in South India. Sangam literature (300 BCE - 300 CE) portrays Murugan as Seyon, the red god of the hills, associated with the kurinji landscape. This indigenous deity was later syncretized with the Vedic Skanda-Kartikeya. The Tirumurugaatruppadai by Nakkirar is one of the earliest and most beautiful devotional poems dedicated to Murugan, describing pilgrimages to his shrines and the ecstatic worship of his devotees."},
        {"title": "Philosophical Dimensions", "content": "In Tamil Shaiva Siddhanta philosophy, Murugan represents the guru principle - the divine teacher who leads souls from bondage to liberation. His six faces symbolize the five senses plus the mind, all directed toward the divine. The Vel represents jnana (wisdom) that pierces through maya (illusion). His peacock mount symbolizes the ego that must be controlled, while the serpent beneath represents kundalini energy. Thus, Murugan worship encompasses both bhakti (devotion) and jnana (knowledge) paths to liberation."},
        {"title": "The Kavadi Tradition", "content": "The practice of carrying kavadi - elaborate structures borne on the shoulders during festivals like Thaipusam - represents one of the most intense forms of devotional practice in Hinduism. Devotees undertake vows, observe strict austerities, and sometimes pierce their bodies with hooks and skewers as acts of penance and devotion. This tradition, particularly strong in Tamil Nadu, Malaysia, and Singapore, demonstrates the extraordinary depth of devotion that Murugan inspires in his followers."},
        {"title": "Murugan and Tamil Identity", "content": "Murugan is inseparably linked with Tamil cultural identity. He is called 'Tamil Kadavul' (God of Tamils) and is credited with teaching the Tamil language to the sage Agastya. The Kanda Shasti Kavasam, a powerful hymn composed by Devaraya Swamigal, is recited daily by millions of Tamils worldwide. Murugan temples serve as centers of Tamil cultural preservation, where classical music, dance, and literature continue to flourish. The deity thus represents not just religious devotion but cultural continuity."},
        {"title": "Universal Relevance", "content": "Beyond his specific Tamil context, Murugan embodies universal spiritual principles. His youth represents the eternal freshness of divine consciousness. His role as commander of the gods symbolizes the organized spiritual effort needed to overcome inner demons. His accessibility - he is known for granting boons readily to sincere devotees - makes him particularly beloved. In an age of uncertainty, Murugan's message of courage, devotion, and ultimate victory over evil continues to resonate with seekers across the world."}
    ],
    "moral": "With courage, devotion, and righteousness, we can overcome any obstacle in life.",
    "facts": [
        "Murugan has six sacred temples in Tamil Nadu called Arupadai Veedu",
        "Thaipusam is the major festival celebrating Lord Murugan",
        "The Vel (divine spear) is his primary weapon, representing wisdom",
        "He is considered the patron deity of Tamil language and culture"
    ]
}


def get_images_for_keyword(keyword: str) -> List[str]:
    """Get relevant images for a keyword"""
    key = keyword.lower().strip()
    if key in STORY_PAGE_IMAGES:
        return STORY_PAGE_IMAGES[key].get("kids", DEFAULT_IMAGES)
    for k in STORY_PAGE_IMAGES:
        if k in key or key in k:
            return STORY_PAGE_IMAGES[k].get("kids", DEFAULT_IMAGES)
    return DEFAULT_IMAGES

@dataclass
class StoryPage:
    page_number: int
    title: str
    content: str
    image_prompt: str
    image_url: str
    characters: List[str]
    location: str
    action: str

@dataclass
class TamilStoryData:
    title: str
    keywords: List[str]
    outline: str
    pages: List[StoryPage]
    moral: str
    age_group: str
    festival_connection: str
    region: str
    era: str
    story_type: str
    historical_context: str
    cultural_elements: List[str]
    language_style: str
    educational_facts: List[str]
    place_info: Optional[Dict[str, str]]
    total_pages: int

class TamilStoryGenerator:
    def __init__(self):
        pass
    
    def _get_image(self, images: List[str], index: int) -> str:
        return images[index % len(images)]
    
    def generate_tamil_story(self, keywords: List[str], age_group: str = "all") -> TamilStoryData:
        keyword = keywords[0].lower().strip() if keywords else "raja raja chola"
        display_keyword = keywords[0] if keywords else "Raja Raja Chola"
        
        # Get template if exists
        template = STORY_TEMPLATES.get(keyword)
        
        # Get story-specific images based on keyword AND age group
        images = get_story_images(display_keyword, age_group)
        
        if template:
            story_content = template["kids"] if age_group == "kids" else template["adults"]
            pages = []
            for i, page_data in enumerate(story_content):
                pages.append(StoryPage(
                    page_number=i + 1,
                    title=page_data["title"],
                    content=page_data["content"],
                    image_prompt=f"{display_keyword} - {page_data['title']}",
                    image_url=images[i] if i < len(images) else images[i % len(images)],
                    characters=[display_keyword],
                    location=template["region"],
                    action=page_data["title"]
                ))
            
            return TamilStoryData(
                title=template["title"],
                keywords=keywords,
                outline="Elaborate cultural story",
                pages=pages,
                moral=template["moral"],
                age_group=age_group,
                festival_connection="Pongal" if "chola" in keyword else "Thaipusam",
                region=template["region"],
                era=template["era"],
                story_type="historical" if "chola" in keyword or "kattabomman" in keyword else "mythology",
                historical_context=f"Story set during {template['era']}",
                cultural_elements=["Tamil Heritage", "Cultural Values", "Historical Significance"],
                language_style="elaborate",
                educational_facts=template["facts"],
                place_info={"name": template["region"], "significance": "Historical"},
                total_pages=len(pages)
            )
        
        # Default story generation for keywords without templates
        return self._generate_default_story(display_keyword, age_group, images)
    
    def _generate_default_story(self, keyword: str, age_group: str, images: List[str]) -> TamilStoryData:
        """Generate a default elaborate story for keywords without specific templates"""
        
        # Theme-based images for default stories
        theme_images = [
            DEFAULT_STORY_IMAGES["introduction"],  # Page 1
            DEFAULT_STORY_IMAGES["learning"],      # Page 2
            DEFAULT_STORY_IMAGES["challenge"],     # Page 3
            DEFAULT_STORY_IMAGES["journey"],       # Page 4
            DEFAULT_STORY_IMAGES["solution"],      # Page 5
            DEFAULT_STORY_IMAGES["success"],       # Page 6
            DEFAULT_STORY_IMAGES["celebration"],   # Page 7
            DEFAULT_STORY_IMAGES["legacy"],        # Page 8
        ]
        
        if age_group == "kids":
            pages_data = [
                {"title": "The Beginning", "content": f"Long ago in the ancient land of Tamil Nadu, there lived a remarkable figure known as {keyword}. The land was blessed with fertile fields, magnificent temples, and wise people who valued knowledge and culture above all else. Our story begins in this golden age, when great deeds were done and legends were born. The people spoke of {keyword} with great respect and admiration."},
                {"title": "Early Days", "content": f"From an early age, {keyword} showed signs of greatness. While other children played, {keyword} would sit and listen to the elders tell stories of ancient heroes and wise sages. There was a special light in {keyword}'s eyes - a determination to do something meaningful for the people. The teachers noticed this and gave special attention to nurturing these qualities."},
                {"title": "The Challenge", "content": f"One day, a great challenge arose that threatened the peace and happiness of the people. Many were afraid and didn't know what to do. But {keyword} stepped forward with courage and said, 'Do not worry, I will find a way to help us all.' The people were amazed at such bravery and began to hope again."},
                {"title": "The Journey", "content": f"{keyword} embarked on a difficult journey, facing many obstacles along the way. There were moments of doubt and difficulty, but {keyword} never gave up. With each challenge overcome, {keyword} grew stronger and wiser. The journey taught valuable lessons about perseverance, kindness, and the importance of helping others."},
                {"title": "Finding the Solution", "content": f"After much effort and thought, {keyword} discovered the solution to the great challenge. It required bringing people together, combining their strengths, and working as one united community. {keyword} traveled from village to village, inspiring people to join the cause and contribute their unique talents."},
                {"title": "Victory and Celebration", "content": f"Through the combined efforts of everyone, guided by {keyword}'s wisdom and leadership, the challenge was overcome! The people celebrated with great joy. There was music, dancing, and feasting that lasted for many days. Everyone thanked {keyword} for bringing them together and showing them what they could achieve."},
                {"title": "The Teachings", "content": f"{keyword} gathered the people and shared important teachings: 'Remember, our strength lies in our unity. When we help each other, no challenge is too great. Always be kind, always be brave, and never forget the wisdom of our ancestors.' These words were remembered and passed down through generations."},
                {"title": "The Legacy", "content": f"The story of {keyword} is still told today, inspiring children and adults alike. Temples and monuments stand as reminders of this great figure. Every year, people gather to celebrate and remember the lessons learned. {keyword}'s legacy teaches us that with courage, wisdom, and unity, we can overcome any obstacle and create a better world for everyone."}
            ]
        else:
            pages_data = [
                {"title": "Historical Context", "content": f"The story of {keyword} unfolds against the rich tapestry of Tamil civilization, one of the oldest continuous cultures in the world. Tamil Nadu, with its ancient temples, classical literature, and sophisticated administrative systems, provided the backdrop for remarkable achievements in art, architecture, science, and governance. It was in this environment of cultural excellence that {keyword} emerged as a significant figure, contributing to the legacy that continues to inspire millions today."},
                {"title": "Origins and Background", "content": f"The origins of {keyword} are rooted in the complex social and political landscape of ancient Tamil Nadu. The region was characterized by powerful dynasties, flourishing trade networks extending to Rome and Southeast Asia, and a vibrant intellectual tradition preserved in the Sangam literature. Understanding {keyword} requires appreciating this context of cultural sophistication and political dynamism that shaped the Tamil world."},
                {"title": "Rise to Prominence", "content": f"{keyword}'s rise to prominence was marked by a combination of exceptional abilities and favorable circumstances. The period demanded leaders who could navigate complex challenges while preserving and promoting Tamil cultural values. Through a combination of strategic thinking, cultural sensitivity, and unwavering commitment to principles, {keyword} gradually emerged as a figure of significant influence and respect."},
                {"title": "Major Achievements", "content": f"The achievements associated with {keyword} span multiple domains - from administrative innovations to cultural patronage, from military strategy to diplomatic finesse. These accomplishments were not merely personal triumphs but contributed to the broader flourishing of Tamil civilization. The impact of these achievements can be traced in the archaeological record, literary sources, and living traditions that continue to this day."},
                {"title": "Challenges and Adversity", "content": f"No significant historical figure achieves greatness without facing substantial challenges. {keyword} confronted obstacles that tested resolve, wisdom, and character. These challenges came from various quarters - political rivals, natural calamities, and the inherent difficulties of governance. The response to these challenges reveals the true measure of {keyword}'s character and capabilities."},
                {"title": "Cultural and Social Impact", "content": f"Beyond immediate political or military achievements, {keyword}'s lasting impact lies in the cultural and social sphere. The patronage of arts, support for religious institutions, and promotion of learning created conditions for cultural flourishing that outlasted any individual reign. This cultural legacy, embedded in temples, literature, and traditions, represents perhaps the most enduring contribution."},
                {"title": "Philosophy and Values", "content": f"The actions and decisions attributed to {keyword} reflect a coherent philosophy rooted in Tamil ethical traditions. Concepts like aram (righteousness), duty to subjects, respect for learning, and religious tolerance informed the approach to governance and life. These values, articulated in classical Tamil literature like the Thirukkural, found practical expression in {keyword}'s conduct."},
                {"title": "Enduring Legacy", "content": f"The legacy of {keyword} extends far beyond the immediate historical period. In temples, inscriptions, literature, and living memory, this legacy continues to shape Tamil cultural identity. Modern scholars, artists, and leaders continue to draw inspiration from this heritage. The story of {keyword} reminds us that individual actions, guided by wisdom and virtue, can create ripples that extend across centuries, inspiring future generations to strive for excellence."}
            ]
        
        pages = []
        for i, page_data in enumerate(pages_data):
            pages.append(StoryPage(
                page_number=i + 1,
                title=page_data["title"],
                content=page_data["content"],
                image_prompt=f"{keyword} - {page_data['title']}",
                image_url=theme_images[i] if i < len(theme_images) else theme_images[i % len(theme_images)],
                characters=[keyword],
                location="Tamil Nadu",
                action=page_data["title"]
            ))
        
        return TamilStoryData(
            title=f"The Story of {keyword}",
            keywords=[keyword],
            outline="Elaborate cultural story",
            pages=pages,
            moral="Wisdom, courage, and dedication to one's people create legacies that endure through the ages.",
            age_group=age_group,
            festival_connection="Pongal",
            region="Tamil Nadu",
            era="Ancient Times",
            story_type="cultural",
            historical_context="Set in the rich cultural landscape of Tamil Nadu",
            cultural_elements=["Tamil Heritage", "Cultural Values", "Historical Significance"],
            language_style="elaborate",
            educational_facts=[f"{keyword} is an important figure in Tamil cultural heritage", "Tamil civilization is one of the oldest in the world"],
            place_info={"name": "Tamil Nadu", "significance": "Cultural Heritage"},
            total_pages=len(pages)
        )

if __name__ == "__main__":
    generator = TamilStoryGenerator()
    story = generator.generate_tamil_story(["Raja Raja Chola"], "kids")
    print(f"✅ {story.title}")
    print(f"📖 {story.total_pages} pages")
    for page in story.pages:
        print(f"\n--- Page {page.page_number}: {page.title} ---")
        print(page.content[:200] + "...")