import sqlite3, json

DB = "votes.db"

PETS = [
    {"id": f"pet_{i:03d}", "name": name, "breed": breed, "description": desc, "image": f"https://picsum.photos/seed/pet{i}/400/500"}
    for i, (name, breed, desc) in enumerate([
        ("Luna", "Golden Retriever", "Loves fetch and belly rubs. Great with kids!"),
        ("Max", "German Shepherd", "Loyal and smart. Needs an active family."),
        ("Bella", "Labrador Mix", "Gentle soul who adores cuddles on the couch."),
        ("Charlie", "Beagle", "Curious nose, wagging tail — always an adventure."),
        ("Daisy", "Poodle", "Hypoallergenic and super smart. Loves to learn tricks."),
        ("Milo", "Husky", "Blue-eyed beauty who loves cold weather and running."),
        ("Coco", "Shih Tzu", "Lap dog extraordinaire. Perfect for apartments."),
        ("Rocky", "Rottweiler", "Big softy underneath. Loyal to the core."),
        ("Lola", "Chihuahua", "Small dog, huge personality. Rules the roost."),
        ("Buddy", "Boxer", "Playful and energetic, great with children."),
        ("Molly", "Border Collie", "Genius dog who needs a job to do."),
        ("Cooper", "Dachshund", "Long on love, short on legs. Very snuggly."),
        ("Sadie", "Cocker Spaniel", "Sweet and gentle, perfect first dog."),
        ("Tucker", "Australian Shepherd", "Merle coat, boundless energy, loves herding."),
        ("Zoe", "Bichon Frise", "Fluffy white cloud who loves everyone."),
        ("Bear", "Newfoundland", "Gentle giant with a heart of gold."),
        ("Lily", "Maltese", "Elegant and affectionate, silky coat."),
        ("Duke", "Great Dane", "Massive dog, massive love. Very gentle."),
        ("Penny", "Corgi", "Stubby legs, big ears, royal attitude."),
        ("Ace", "Dalmatian", "Spotted and speedy. Loves to run."),
        ("Ruby", "Irish Setter", "Elegant redhead who loves the outdoors."),
        ("Zeus", "Doberman", "Sleek, loyal, and very protective."),
        ("Nala", "Pit Bull Mix", "Misunderstood sweetheart who loves everyone."),
        ("Gus", "Basset Hound", "Droopy ears, lazy days, maximum charm."),
        ("Rosie", "Yorkshire Terrier", "Tiny but feisty. Loves fancy accessories."),
        ("Bruno", "Saint Bernard", "Drool and all, he's worth every wipe."),
        ("Stella", "Vizsla", "Hungarian pointer with an orange velvet coat."),
        ("Rex", "Belgian Malinois", "High drive working dog. Needs a mission."),
        ("Gracie", "Springer Spaniel", "Bouncy and joyful, loves water splashing."),
        ("Hank", "Bloodhound", "Nose for trouble, heart of gold."),
        ("Ivy", "Whippet", "Sleek racing dog who loves couch time equally."),
        ("Moose", "Bernese Mountain Dog", "Tri-color fluff mountain who loves snow."),
        ("Cleo", "Shar Pei", "Wrinkly and wise. Very loyal to one person."),
        ("Finn", "Irish Wolfhound", "Tallest of dogs, gentlest of souls."),
        ("Hazel", "Weimaraner", "Silver ghost dog with stunning amber eyes."),
        ("Otto", "Schnauzer", "Bearded gentleman with opinions about everything."),
        ("Poppy", "Cavalier King Charles", "Born for laps and royal living."),
        ("Diesel", "Cane Corso", "Massive guardian who is secretly a baby."),
        ("Willow", "Saluki", "Ancient breed, graceful as a gazelle."),
        ("Beau", "Louisiana Catahoula", "Marbled coat, glass eyes, one of a kind."),
        ("Olive", "French Bulldog", "Bat ears and snorts. Urban dog perfection."),
        ("Thor", "Akita", "Japanese noble with unwavering loyalty."),
        ("Sage", "Siberian Husky Mix", "Wolf-like beauty who talks back to you."),
        ("Piper", "Rat Terrier", "Tiny but mighty. Champion squirrel chaser."),
        ("Clyde", "Mastiff", "210 lbs of pure lap dog."),
        ("Fern", "Nova Scotia Duck Tolling Retriever", "Rare red beauty who loves to swim."),
        ("Samson", "Leonberger", "Lion-maned gentle giant. Kids adore him."),
        ("Maple", "American Eskimo", "White and fluffy with a smile always on."),
        ("Jax", "Staffordshire Bull Terrier", "Muscle and love in equal measure."),
        ("Iris", "Chinese Crested", "Partly hairless and completely lovable."),
        ("Wolf", "Alaskan Malamute", "Pack dog who needs his family always near."),
        ("Fiona", "Rhodesian Ridgeback", "African lion hound, dignified and fast."),
        ("Chip", "Jack Russell Terrier", "10 lbs of non-stop action and mischief."),
        ("Aurora", "Samoyed", "Perpetual smile, white cloud on legs."),
        ("Ranger", "Treeing Walker Coonhound", "Melodious howl, loves long hikes."),
        ("Biscuit", "Labradoodle", "Curly golden fluff, zero shedding."),
        ("Pepper", "Miniature Pinscher", "Tiny Doberman energy, fearless leader."),
        ("Coda", "Tibetan Mastiff", "Ancient guardian breed with lion's mane."),
        ("Meadow", "Flat-Coated Retriever", "Perpetual puppy energy well into adulthood."),
        ("Archie", "Otterhound", "Rare and shaggy, loves muddy water."),
        ("Lotus", "Chow Chow", "Blue-black tongue, regal and independent."),
        ("Blaze", "Redbone Coonhound", "Deep bay howl, striking mahogany coat."),
        ("Clover", "Soft Coated Wheaten Terrier", "Silky wheat coat, Irish charm."),
        ("Atlas", "Bouvier des Flandres", "Working dog built like a small tank."),
        ("Sunny", "Golden Doodle", "Fluffy, friendly, and impossibly cute."),
        ("Storm", "Belgian Tervuren", "Dark sable coat, intense and elegant."),
        ("Juniper", "American Water Spaniel", "Brown curls who was born to retrieve."),
        ("Knox", "Plott Hound", "Brindled hunter with a bawling voice."),
        ("Cinnamon", "Toy Fox Terrier", "Tiny tuxedo dog with big dog attitude."),
        ("Pax", "Harrier", "Hound between Beagle and Foxhound, great nose."),
        ("Echo", "Portuguese Water Dog", "Obama's choice. Loves to surf."),
        ("Briar", "Field Spaniel", "Rare cousin of Cocker, calm and noble."),
        ("Titan", "Black Russian Terrier", "Thick black coat, Russian powerhouse."),
        ("Wren", "English Toy Spaniel", "Domed head, pushed face, royal heritage."),
        ("Chase", "Brittany Spaniel", "Tailless bird dog with unlimited energy."),
        ("Fable", "Swedish Vallhund", "Viking Corgi. Ancient spitz herder."),
        ("Scout", "Boykin Spaniel", "South Carolina's own, chocolate brown."),
        ("Pixel", "Spitz Mix", "Fluffy fox-faced dog with perky ears."),
        ("Dune", "Sand-colored Greyhound Mix", "Ex-racer now professional napper."),
        ("Comet", "Pomeranian", "5 lbs of fur and attitude. Tiny lion."),
        ("River", "Lagotto Romagnolo", "Italian truffle hunter with curly coat."),
        ("Cedar", "Finnish Spitz", "Barking bird dog from the far north."),
        ("Opal", "Dalmatian Mix", "Spots on spots, heart of pure gold."),
        ("Jasper", "Entlebucher Mountain Dog", "Swiss herder, smallest of the mountain dogs."),
        ("Blythe", "Icelandic Sheepdog", "Only native Icelandic breed, playful spirit."),
        ("Cadet", "Muensterlaender", "German bird dog with flowy black-white coat."),
        ("Fen", "Finnish Lapphund", "Reindeer herder built for Arctic cold."),
        ("Harbor", "American Foxhound", "Washington's favorite, melodic voice."),
        ("Iggy", "Ibizan Hound", "Pharaoh Hound cousin, rose-eared beauty."),
        ("Jewel", "Azawakh", "West African sighthound, supermodel build."),
        ("Koda", "Karelian Bear Dog", "Finnish hunter of large game. Bold soul."),
        ("Larkspur", "Skye Terrier", "Floor-length coat, fearless little warrior."),
        ("Mochi", "Japanese Chin", "Cat-like dog who loves to perch up high."),
        ("Nova", "Australian Cattle Dog", "Blue heeler — tough, smart, tireless."),
        ("Onyx", "Black Labrador", "Classic, loyal, endlessly retrieving."),
        ("Quest", "Kooikerhondje", "Dutch duck decoy dog with orange-black coat."),
        ("Rain", "Laguna Sheepdog Mix", "Mop dog cousin, dreadlocked and goofy."),
        ("Serra", "Estrela Mountain Dog", "Portuguese flock guardian, devoted and calm."),
        ("Tide", "Boykin-Chesapeake Mix", "Water-loving brown retriever duo mix."),
    ], start=1)
]

def seed():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS items (
        id TEXT PRIMARY KEY,
        name TEXT,
        breed TEXT,
        description TEXT,
        image TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id TEXT,
        session_id TEXT,
        choice TEXT,
        ts DATETIME DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(item_id, session_id)
    )""")
    conn.commit()

    for p in PETS:
        c.execute("INSERT OR IGNORE INTO items VALUES (?,?,?,?,?)",
                  (p["id"], p["name"], p["breed"], p["description"], p["image"]))
    conn.commit()
    conn.close()
    print(f"Seeded {len(PETS)} pets.")

if __name__ == "__main__":
    seed()
