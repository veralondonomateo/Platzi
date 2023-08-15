import matplotlib.pyplot as plt

def generate():
    labes = ['A','B','C']
    values = [200,300,100]

    fig, ax = plt.subplots()
    ax.pie(values, labels= labes)
    plt.savefig('pie.png')
    plt.close()