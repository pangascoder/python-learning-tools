import datetime
from enum import Enum


class Zodiac(Enum):
  Aries = 'Aries'
  Taurus = 'Taurus'
  Gemini = 'Gemini'
  Cancer = 'Cancer'
  Leo = 'Leo'
  Virgo = 'Virgo'
  Libra = 'Libra'
  Scorpio = 'Scorpio'
  Sagittarius = 'Sagittarius'
  Capricorn = 'Capricorn'
  Aquarius = 'Aquarius'
  Pisces = 'Pisces'


class Person:

  def __init__(self,
               name=None,
               birthyear=None,
               birthmonth=None,
               birthdate=None):
    self.name = name
    self.birthyear = birthyear
    self.birthmonth = birthmonth
    self.birthdate = birthdate
    self.age = self.calculateAge()
    self.zodiac_sign = self.identifyAstrologicalSign()
    self.animal_year = self.identifyAnimalYear()
    self.birthstone = self.identifyBirthstone()
    self.element = self.identifyElement()
    self.fortune = self.createFortune()

  def calculateAge(self):
    today = datetime.date.today()
    age = today.year - int(self.birthyear) - (
      (today.month, today.day) < (self.birthmonth, int(self.birthdate)))

    return age

  def identifyAstrologicalSign(self):
    sign = "No match"

    full_birthdate = str(self.birthmonth) + "-" + str(self.birthdate)
    full_birthdate = datetime.datetime.strptime(full_birthdate, "%m-%d")

    if datetime.datetime.strptime(
        "03-21", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "04-19", "%m-%d"):
      sign = Zodiac.Aries
    elif datetime.datetime.strptime(
        "04-20", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "05-20", "%m-%d"):
      sign = Zodiac.Taurus
    elif datetime.datetime.strptime(
        "05-21", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "06-21", "%m-%d"):
      sign = Zodiac.Gemini
    elif datetime.datetime.strptime(
        "06-22", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "07-22", "%m-%d"):
      sign = Zodiac.Cancer
    elif datetime.datetime.strptime(
        "07-23", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "08-22", "%m-%d"):
      sign = Zodiac.Leo
    elif datetime.datetime.strptime(
        "08-23", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "09-22", "%m-%d"):
      sign = Zodiac.Virgo
    elif datetime.datetime.strptime(
        "09-23", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "10-23", "%m-%d"):
      sign = Zodiac.Libra
    elif datetime.datetime.strptime(
        "10-24", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "11-22", "%m-%d"):
      sign = Zodiac.Scorpio
    elif datetime.datetime.strptime(
        "11-23", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "12-21", "%m-%d"):
      sign = Zodiac.Sagittarius
    # Special Case
    elif datetime.datetime.strptime(
        "1899-12-22",
        "%Y-%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "1900-01-19", "%Y-%m-%d"):
      sign = Zodiac.Capricorn
    elif datetime.datetime.strptime(
        "01-20", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "02-18", "%m-%d"):
      sign = Zodiac.Aquarius
    elif datetime.datetime.strptime(
        "02-19", "%m-%d") <= full_birthdate <= datetime.datetime.strptime(
          "03-20", "%m-%d"):
      sign = Zodiac.Pisces

    return sign

  def identifyAnimalYear(self):
    animal = "No match"

    # Convert text to number to allow mathematical calculation
    birthyear = int(self.birthyear)

    if (birthyear - 2000) % 12 == 0:
      animal = 'Dragon'
    elif (birthyear - 2000) % 12 == 1:
      animal = 'Snake'
    elif (birthyear - 2000) % 12 == 2:
      animal = 'Horse'
    elif (birthyear - 2000) % 12 == 3:
      animal = 'Sheep/Goat/Ram'
    elif (birthyear - 2000) % 12 == 4:
      animal = 'Monkey'
    elif (birthyear - 2000) % 12 == 5:
      animal = 'Rooster'
    elif (birthyear - 2000) % 12 == 6:
      animal = 'Dog'
    elif (birthyear - 2000) % 12 == 7:
      animal = 'Pig'
    elif (birthyear - 2000) % 12 == 8:
      animal = 'Rat'
    elif (birthyear - 2000) % 12 == 9:
      animal = 'Ox'
    elif (birthyear - 2000) % 12 == 10:
      animal = 'Tiger'
    else:
      animal = 'Hare'

    return animal

  def identifyBirthstone(self):
    birthstone = "No match"

    print(self.birthmonth)

    if self.birthmonth == 1:
      birthstone = "Garnet"
    elif self.birthmonth == 2:
      birthstone = "Amethyst"
    elif self.birthmonth == 3:
      birthstone = "Aquamarine"
    elif self.birthmonth == 4:
      birthstone = "Diamond"
    elif self.birthmonth == 5:
      birthstone = "Emerald"
    elif self.birthmonth == 6:
      birthstone = "Alexandrite"
    elif self.birthmonth == 7:
      birthstone = "Ruby"
    elif self.birthmonth == 8:
      birthstone = "Peridot, Spinel"
    elif self.birthmonth == 9:
      birthstone = "Sapphire"
    elif self.birthmonth == 10:
      birthstone = "Tourmaline"
    elif self.birthmonth == 11:
      birthstone = "Golden Topaz, Citrine"
    elif self.birthmonth == 12:
      birthstone = "Blue Zircon, Blue Topaz, Tanzanite"

    return birthstone

  def identifyElement(self):
    element = "No match"

    if self.zodiac_sign == Zodiac.Aries or self.zodiac_sign == Zodiac.Leo or self.zodiac_sign == Zodiac.Sagittarius:
      element = "Fire"
    elif self.zodiac_sign == Zodiac.Taurus or self.zodiac_sign == Zodiac.Virgo or self.zodiac_sign == Zodiac.Capricorn:
      element = "Earth"
    elif self.zodiac_sign == Zodiac.Gemini or self.zodiac_sign == Zodiac.Libra or self.zodiac_sign == Zodiac.Aquarius:
      element = "Air"
    elif self.zodiac_sign == Zodiac.Cancer or self.zodiac_sign == Zodiac.Scorpio or self.zodiac_sign == Zodiac.Pisces:
      element = "Water"

    return element

  def createFortune(self):
    fortune = "No fortune available."

    print(self.birthdate)

    # Aries
    if self.zodiac_sign == Zodiac.Aries:
      if int(self.birthdate) % 2 == 0:
        fortune = "Your usual lazy attitude is apt to receive a burst of energy tonight, " + self.name + ". It's in your nature not to want to lift a finger, but for some reason you may be compelled to get up and get moving. You will find that when you connect with others, you're more motivated to make things happen for yourself. When you get the attention you feel you deserve, your devotion is strong."
      else:
        fortune = "It would seem that your sensitivity is in slight conflict with your actions, " + self.name + ". You continue to go through the motions and do what you planned to do, but it seems like your heart isn't in it anymore. Don't ask yourself why. It's just that you've worked hard and have been thinking hard lately. You have reached your limit and it's time for you to rest."

    # Taurus
    elif self.zodiac_sign == Zodiac.Taurus:
      if int(self.birthdate) % 2 == 0:
        fortune = "You may find your emotions difficult to deal with, " + self.name + ", especially later in the day. Consider taking an intellectual instead of emotional approach. Your feelings could send you into a drastic mood swing from one end of the spectrum to the other. The thing you really need right now - especially tonight - is balance. Tie up any loose ends to maintain more equilibrium."
      else:
        fortune = "You may have been spending or saving too much money, " + self.name + ". It's clear that a rebalancing is in order if you're to find pleasure rather than eternal frustration. It's a curious phenomenon. It's as though you have lost contact with your body. Yet it's in your body where you will ultimately find your balance. You certainly won't find it in your head!"

      # Gemini
    elif self.zodiac_sign == Zodiac.Gemini:
      if int(self.birthdate) % 2 == 0:
        fortune = "You've been stamping the ground impatiently, " + self.name + ". You're waiting for the moment to jump into new adventures with renewed vigor after your meditation of the last few months. Gemini, know that the moment has almost arrived! You now have the strategy, objective, and means at your disposal to succeed. Just a bit more work remains. Gather your strength and get ready for action!"
      else:
        fortune = "Communication with others could be extremely rewarding, " + self.name + ", especially later in the day. Project more of your energy outward and join others in projects that you might otherwise try to tackle on your own. Things should flow smoothly as long as you take a lighthearted, optimistic approach. Move forward with projects instead of just contemplating their completion."

    # Cancer
    elif self.zodiac_sign == Zodiac.Cancer:
      if int(self.birthdate) % 2 == 0:
        fortune = "If you find yourself tired and irritable now, " + self.name + ", you should know that this is normal. You may have had a few months that were a little too studious. Would you like to continue with the same rhythm? Be careful that your ambitions don't lead you to physical exhaustion. If you get sick, you will be even more frustrated. So be wise and take care of your own basic needs."
      else:
        fortune = "Make sure you solidify your affairs early in the day, " + self.name + ", because the sparks are going to fly after sunset. People might try to throw you off balance with fast talk and fancy ideas. You need to make sure you're on solid ground before you take the next step upward. Balance your emotions so you don't take your frustration out on others. Focus on your goals."

    # Leo
    elif self.zodiac_sign == Zodiac.Leo:
      if int(self.birthdate) % 2 == 0:
        fortune = "This is going to be a good moment to look elsewhere, " + self.name + ". You should do just as the artist does when he has worked on a painting for too long, which is take a step back. You need to see some people, travel, go to the theater, and clear your head. This is never easy for you, but don't hesitate. You will realize afterward that it was the best thing for you to do."
      else:
        fortune = "Things are looking up for you, " + self.name + ", especially later in the day. Pieces should be coming together and things flowing into place naturally. You will find that your outward-directed energy is better balanced now. You should connect with others using your keen wit, strong will, and sheer intelligence. Take your time to do the things you need to do. Don't rush."

    # Virgo
    elif self.zodiac_sign == Zodiac.Virgo:
      if int(self.birthdate) % 2 == 0:
        fortune = "This is the right moment to extricate yourself from relationships that have seen their day, " + self.name + ". This won't be easy, but you must. In your professional and private lives, you're too hesitant to get out of distasteful situations or obligations. You're afraid of hurting people or making them mad. But in the end, you're hurting yourself. Give more weight to your own needs and follow your own path."
      else:   
        fortune = "The energy is apt to pick up in your life today, " + self.name + ". You may be asked to report to duty. Don't make promises you can't keep. Your words will be taken seriously, and you shouldn't mislead people into thinking that something is going to happen when you know it isn't. You know how that situation will turn out. Trust yourself, regardless of the circumstances."

    # Libra
    elif self.zodiac_sign == Zodiac.Libra:
      if int(self.birthdate) % 2 == 0:
        fortune = "You took off like a bullet a few days ago, " + self.name + ", making great progress in a short amount of time. But now you're grappling with doubts that are undermining all your energy. Reflecting on the events of the past few days, it's obvious that you were somewhat reckless in your headlong pursuit of your goals. Don't give up! Just rethink your strategy."
      else:
        fortune = "There's extra aggression in your world today, " + self.name + ". Realize that this is probably due more to your reaction to a situation than to the situation itself. It could be that you're in conflict with someone just because he or she wants harmony while you have a propensity to fight. This paradox is likely to be detrimental to your psyche unless you try to change it."

    # Scorpio
    elif self.zodiac_sign == Zodiac.Scorpio:
      if int(self.birthdate) % 2 == 0:
        fortune = "There is some likelihood that thoughts of your love life will haunt you today, " + self.name + ". Perhaps you're intrigued by the idea of exploring certain realms of your relationship that remain secret, but you're unsure how to communicate this to your mate. Perhaps you're still testing the waters, waiting until you're sure of how you feel. In any case, you may decide to proceed!"
      else:
        fortune = "Your mood may take a bizarre twist today, " + self.name + ", as you calm your desire to fight for something. You're probably more interested in enjoying the beauty of something rather than trying to keep it for yourself. Allowing someone or something else to be free is the best gift you can give. Keep the lines of communication open and you will find that everything falls into place as it should."

    # Sagittarius
    elif self.zodiac_sign == Zodiac.Sagittarius:
      if int(self.birthdate) % 2 == 0:
        fortune = self.name + ", today more than ever you will yearn to escape from the daily routine. You're thirsty for new sights and sounds, new faces and places. However, you're well aware that you must juggle your desires with your professional or domestic obligations. It isn't always easy, but you should trust your imagination to suggest a way to amicably settle this conflict."
      else:
        fortune = "Things are going to get better and better for you as the day progresses, " + self.name + ". Try to get your grounded, practical, and logical self collected during the day so you have the evening to socialize and commune with close friends, if possible. Balance is going to be a key issue for you today, so make sure you keep things in check before any one part of your life gets out of hand."

    # Capricorn
    elif self.zodiac_sign == Zodiac.Capricorn:
      if int(self.birthdate) % 2 == 0:
        fortune = "Finally, you're on the mend, " + self.name + ". The minor ailments that have been dragging you down lately are beginning to disappear, and you're about to regain all of your physical energy. However, if you overindulge, your energy levels are likely to plummet again. If nothing else, you will have learned a valuable lesson about the importance of moderation, especially now. Don't overdo it!"
      else:
        fortune = "There may be a bit of aggravation in a part of your life that's urging you to get up and do something, " + self.name + ". It could be that you're getting overly emotional about a certain issue, and that you need to consider more of the cold, hard facts of what's really going on. You could be missing something obvious simply because you're so caught up in your emotional drama."

    # Aquarius  
    elif self.zodiac_sign == Zodiac.Aquarius:
      if int(self.birthdate) % 2 == 0:
        fortune = "Do you feel a little under the weather, " + self.name + "? It's possible, considering all the emotional turmoil you've been through lately. It takes time to recover from those storms. As you know, the work itself isn't what gets you down but rather your worries about the future that drain your energy. Give yourself a break today. Take some time for rest and recuperation."
      else:
        fortune = "You may feel a bit stodgy today, " + self.name + ", but things are going to pick up tonight. There will be a great deal of air to fuel your fire, and you're ready to burn! You could be like a desert of dry sagebrush just ready to be set alight. The whole mountainside is about to go up in a beautiful blaze of glory. You're ready to shine like the brilliant star that you are."

    # Pisces
    elif self.zodiac_sign == Zodiac.Pisces:
      if int(self.birthdate) % 2 == 0:
        fortune = "There is some likelihood that the mood at home is fraught with tension, " + self.name + ". Did you dare to express some contrary intellectual opinion? In any case, it looks like your self-confidence is stronger than usual right now. Go ahead and express any complaints or opinions you may have been keeping to yourself. But try and do it gently, especially where your family is concerned."
      else:
        fortune = "Get things taken care of in the morning, " + self.name + ", so you can be carefree and laid back in the evening. It's important for you to square things away in your head so you can communicate important information to others later. Feel free to take an unconventional approach. It's important to march to the beat of your own drum and not anyone else's."

    return fortune
