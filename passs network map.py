import matplotlib.pyplot as plt
from mplsoccer import Pitch
players=["A","B","C","D"]
x=[30,50,70,60]
y=[40,60,40,20]
PASS=[("A","B",5),
      ("B","C",3),
      ("C","D",7),
      ("A","C",10)]
#draw pitch
pitch=Pitch(pitch_type="statsbomb",line_color="white",pitch_color="grass")
fig,ax=pitch.draw()
#draw [layer position]
player_pos={}
for i in range(len(players)):
    player_pos[players[i]]=(x[i],y[i])

#draw passes
for p in PASS:
    Start=player_pos[p[0]]
    end=player_pos[p[1]]
    width=p[2]
    #draw passing laine
    pitch.lines(Start[0],Start[1],end[0],end[1],
                ax=ax,linewidth=width,color="yellow")
pitch.scatter(x,y,ax=ax,s=300,color="red")
for i in range(len(players)):
    ax.text(x[i],y[i],players[i],ha="center",va="center",color="white",fontsize=10)
plt.title("pass network map")
plt.show()

