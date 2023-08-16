import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
  fix,ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig('bar.png')
  plt.close()

def generate_pie_chart(labels,values):
  fig,ax = plt.subplot()
  ax.pie(values,labels = labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  
    labels = ['a','b','c']
    values = [100,200,180]
    generate_pie_chart(labels,values)