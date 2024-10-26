import csv

# Define the dataset without the first column
data = [
    ["Threatful Word/Phrase"],
    ["Help!"],
    ["Bachao!"],
    ["I'm going to hurt you"],
    ["I'm going to find you"],
    ["I'll make you pay"],
    ["I will kill you!"],
    ["You can't hide from me"],
    ["Slut"],
    ["Randi"],
    ["Bitch"],
    ["Whore"],
    ["You're going to regret this"],
    ["Don't scream"],
    ["Shut up!"],
    ["Chup kar"],
    ["Teri izzat loot lunga"],
    ["I'll ruin your life"],
    ["You think you can escape?"],
    ["Mujhe tum se baat karni hai"],
    ["I'm watching you"],
    ["You're nothing"],
    ["Useless woman"],
    ["I'll show you your place"],
    ["You're disgusting"],
    ["Worthless"],
    ["Stop talking"],
    ["Come here now"],
    ["I'll teach you a lesson"],
    ["You don't deserve respect"],
    ["I'm going to get you"],
    ["Don't act smart"],
    ["Watch what happens next"],
    ["You have no escape"],
    ["I'll take revenge"],
    ["You're mine"],
    ["Get in the car"],
    ["You should be scared"],
    ["Why don't you shut up?"],
    ["You don't deserve safety"],
    ["You're alone now"],
    ["Nobody can hear you"],
    ["You can't run"],
    ["Stop struggling"],
    ["Nobody cares about you"],
    ["I'll destroy you"],
    ["Don't try to resist"],
    ["I'll show you who the boss is"],
    ["How dare you talk back"],
    ["You're so weak"],
    ["You won't get away this time"],
    ["I'm going to take everything from you"],
    ["I'm the one in charge here"],
    ["Don't even try to escape"],
    ["I'm in control"],
    ["You will listen to me"],
    ["Nobody will believe you"],
    ["I'll break you"],
    ["You're a nobody"],
    ["I'm not letting you go"],
    ["This is your end"],
    ["You don't have a choice"],
    ["Don't make me angry"],
    ["You're mine forever"],
    ["I can do whatever I want"],
    ["I'm going to ruin your life"],
    ["You should have listened"],
    ["Nobody will find you"],
    ["Get over here"],
    ["I'll make you disappear"],
    ["Nobody can save you"],
    ["You'll pay for this"],
    ["I'll make sure you regret this"],
    ["You're worthless"],
    ["Who do you think you are?"],
    ["I'll make you suffer"],
    ["You don't stand a chance"],
    ["I'll make your life hell"],
    ["You belong to me"],
    ["I'll never let you go"],
    ["Nobody will believe your story"],
    ["You're all alone"],
    ["I'm watching your every move"],
    ["You're a liar"],
    ["I'll make sure you remember this"],
    ["I'll humiliate you"],
    ["I'll make you disappear"],
    ["I'm everywhere"],
    ["I'm not afraid of the police"],
    ["Nobody can protect you"],
    ["I'll stalk you"],
    ["You belong to me"],
    ["Your life is over"],
    ["You think you're safe?"],
    ["You're weak"],
    ["I'll make you regret meeting me"],
    ["You're in danger"],
    ["I know where you live"],
    ["You can't stop me"],
    ["I'll hurt everyone you love"],
    ["You're trapped"],
    ["I'm going to find you wherever you go"],
    ["You can't escape"],
    ["You belong to me now"],
    ["I'm always watching"],
    ["Nobody can help you"],
    ["I'll never leave you alone"],
    ["You're done"],
    ["I'm going to follow you everywhere"],
    
]



# Creating an expanded dataset for Sexual Harassment/Explicit Terms
sexual_harassment_explicit_terms = {
    'Sexual Harassment/Explicit Terms': [
        "Slut", "Whore", "Skank", "Hoe", "Cocksucker",
        "Thot", "Dildo", "Boobjob", "Gangbang", "Tits",
        "Pussylicker", "Fuckboy", "Cumslut", "Tittyfuck", "Deepthroat",
        "Assfucker", "Cocktease", "Nympho", "Fucktoy", "Meatpole",
        "Cumrag", "Dickhead", "Vaginal", "Buttfucker", "Shag",
        "Pussy", "Cunt", "Fucker", "Blowjob", "Boner",
        "Hard-on", "Hump", "Milf", "Sugar daddy", "Sugar baby",
        "Squirter", "Cumdumpster", "Pornstar", "Jerkoff", "Handjob",
        "Suck me", "Eat me", "Ballsack", "Masturbator", "Cumface",
        "Wet pussy", "Anal", "Asslicker", "Titties", "Fuckbuddy",
        "Dickslap", "Pussyfucker", "Cumguzzler", "Deep fuck", "Hardcore",
        "Fingering", "Porn", "Dirty talk", "Cockgobbler", "Cumshot",
        "Fuckhole", "Cockring", "Sextoy", "Blow", "Buttplug",
        "Doggy style", "Nipple play", "Golden shower", "Orgasm", "Wank",
        "Foot fetish", "Breast fuck", "Handcuff", "Sex slave", "Threesome",
        "Rimjob", "Grind", "Spanking", "Sex tape", "Kinky",
        "Gagging", "Choke me", "Titjob", "Squirt", "Clit",
        "BDSM", "Roleplay", "Sex doll", "Dirty slut", "Striptease",
        "Flasher", "Voyeur", "Peeping tom", "Sex addict", "Lap dance",
        "Wet dream", "Panties", "Fuck me", "Gangbang", "Tit licking",
        "Sexual favors", "Tight pussy", "Groping", "Spit roast", "Hot wax",
        "Bondage", "Ball gag", "Cuntlicker", "Suck cock", "Cock sucker",
        "Anal beads", "Fucktoys", "Strap-on", "Nude", "Wet lips",
        "Pervert", "Blow job", "Erection", "Buttfuck", "Cum eating"
    ]
}

# Converting the dataset into a DataFrame
df_sexual_harassment = pd.DataFrame(sexual_harassment_explicit_terms)

# Saving the dataset to a CSV file
csv_file_path_harassment = "/mnt/data/sexual_harassment_explicit_terms.csv"
df_sexual_harassment.to_csv(csv_file_path_harassment, index=False)

csv_file_path_harassment
# Write to CSV file without the first column
with open('harassment.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
