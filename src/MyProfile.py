class MyProfile:
  def __init__(self, name, year, majors, classes, hometown, live, clubs, classPref, pref):
    self.name = name
    self.year = year
    self.majors = majors
    self.classes = classes
    self.hometown = hometown
    self.live = live
    self.clubs = clubs
    self.classPref = classPref
    self.pref = pref

  def Year(p1, p2):
    if p1.year == p2.year:
      # if they prefer to be matched with someone in their year
      if p1.pref == 1 or p2.pref == 1:
        return 2
      return 1
    else:
      return 0
    
  def Majors(p1, p2):
    mScore = 0
    for m1 in p1.majors:
      for m2 in p2.majors:
        if m1 == m2:
          mScore = mScore + 1
    # if they prefer to be matched with someone in their major
    if p1.pref == 2 or p2.pref == 2:
      return mScore * 2
    return mScore

  def Classes(p1, p2):
    cScore = 0
    for c1 in p1.classes:
      for c2 in p2.classes:
        if c1 == c2:
          cScore = cScore + 1
        # if they are in a class the other person prefers to study with
        if c1 == p2.classPref:
          cScore = cScore + 1
        if c2 == p1.classPref:
          cScore = cScore + 1
    return cScore

  def Hometown(p1, p2):
    if p1.hometown == p2.hometown:
      # if they prefer to be matched with someone from their hometown
      if p1.pref == 4 or p2.pref == 4:
        return 2
      return 1
    return 0

  def Live(p1, p2):
    if p1.live == p2.live:
      # if they prefer to be matched with someone who lives close to them
      if p1.pref == 5 or p2.pref == 5:
        return 2
      return 1
    return 0

  def Clubs(p1, p2):
    cScore = 0
    for c1 in p1.clubs:
      for c2 in p2.clubs:
        if c1 == c2:
          cScore = cScore + 1
    # if they prefer to be matched with someone in their clubs
    if p1.pref == 6 or p2.pref == 6:
      return cScore * 2
    return cScore
  
  def Score(p1, p2):
    return p1.Year(p2) + p1.Majors(p2) + p1.Hometown(p2) + p1.Live(p2) + p1.Clubs(p2)
    
    
  # Name, Year, Major (major 2?)
  # Hometown, Living on or off campus, Prefer a certain shared class?, 
  # Interest?
  # PRefer shared clubs?
  # What do you want to be matched based on:


# p1 = MyProfile("Alice", 1, ["Computer Science", "Psychology"], "Taipei", "South", ["x"], 2)
# p2 = MyProfile("Sam", 1, ["Computer Science"], "Chicago", "South", ["b"], 4)

# print(p1.Score(p2))
