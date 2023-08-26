video_dictionary = {"topping ball" : "https://www.youtube.com/watch?v=EJtXvIBssf4",
                    "shanking ball" : "https://www.youtube.com/watch?v=dSAEUZLwvzg",
                    "chunk" : "https://usgolftv.com/instruction/chunking-golf-shots/",
                    "thin" : "https://www.golfdistillery.com/shot-errors/how-to-fix-thin/",
                    "heel" : "https://www.youtube.com/watch?v=Io3kYsZdpvc",
                    "toe" : "https://www.youtube.com/watch?v=hHRd-a6FOq8",
                    "hook" : "https://golfinsideruk.com/golf-hook/",
                    "slice" : "https://www.youtube.com/watch?v=wPyRs5Y5HRY",
                    "fade" : "https://www.youtube.com/watch?v=ChTSzKICYp0",
                    "draw" : "https://theleftrough.com/how-to-hit-a-draw/"}


class Golfer:

  def __init__(self, handiness):
    self.handiness = handiness
    self.storage = {}

  def main(self):
    x = input("Are you topping the ball?  ")
    if x.lower() in "yes True yea yep":
      if "top" in self.storage:
        self.storage["top"] += 1
      else:
        self.storage["top"] = 1
      video = self.get_link("topping ball")
      return (video)

    else:
      x = input("Are you shanking the ball?  ")
      if x.lower() in "yes True yea yep":
        if "shank" in self.storage:
          self.storage["shank"] += 1
        else:
          self.storage["shank"] = 1
        video = self.get_link("shanking ball")
        return(video)

      else:
        x = input("chunk or thin or neither?  ")
        if x.lower() == "chunk":
          if "chunk" in self.storage:
            self.storage["chunk"] += 1
          else:
            self.storage["chunk"] = 1
          video = self.get_link("chunk")
          return(video)
        elif x.lower() == "thin":
          if "thin" in self.storage:
            self.storage["thin"] += 1
          else:
            self.storage["thin"] = 1
          video = self.get_link("thin")
          return(video)
        else:
          x = input("Is contact on the heel or toe or center?  ")
          if x.lower() == "heel":
            if "heel" in self.storage:
              self.storage["heel"] += 1
            else:
              self.storage["heel"] = 1
            video = self.get_link("heel")
          elif x.lower() == "toe":
            if "toe" in self.storage:
              self.storage["toe"] += 1
            else:
              self.storage["toe"] = 1
            video = self.get_link("toe")
            return(video)
          else:
            x = input("Is your ball drawing, fading, or straight?  ")
            if x.lower() == "drawing":
              if "draw" in self.storage:
                self.storage["draw"] += 1
              else:
                self.storage["draw"] = 1
              video = self.get_link("draw")
              return(video)
            elif x.lower() == "fading":
              if "fade" in self.storage:
                self.storage["fade"] += 1
              else:
                self.storage["fade"] = 1
              video = self.get_link("fade")
              return(video)
            else:
              return("You seem to be hitting the ball just fine!")
        
              

  def get_link(self, string):
    frequency = {}
    string_list = string.split()
    for title in video_dictionary:
      frequency[title] = 0
      for word in string_list:
        if word in title:
          frequency[title] += 1
    if frequency == {}:
      return ("No appropriate video match")

    maximum = next(iter(frequency))
    title_lst = []
    title_lst.append(maximum)
    for title in frequency:
      if frequency[title] > frequency[maximum]:
        maximum = title
        del title_lst[0]
        title_lst.append(maximum)
      elif frequency[title] == frequency[maximum] and title != maximum:
        title_lst.append(title)

    url_lst = []
    for j in range(len(title_lst)):
      url_lst.append(video_dictionary[title_lst[j]])
    clean_up = "Here are your recommendation(s): "
    for k in range(len(url_lst)):
      clean_up += "   Title: {} and URL: {}".format(title_lst[k], url_lst[k])

    return (clean_up)

            
            
                    
                
            
            
    
            
        
  
